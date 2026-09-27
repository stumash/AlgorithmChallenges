# Citizen App — System Design

## Requirements

- Users submit "something happened near me" reports (category, location, optional media).
- Users see a stream of nearby incidents on a map, both by pulling (map open) and via push (app closed).
- Duplicate reports of the same real-world incident should merge, not spam the map with N markers.
- Abuse/spam resistance (rate limiting, coordinated fake-report detection).
- Old incidents age out; storage shouldn't grow unbounded.

## Architecture

```mermaid
flowchart TB
    subgraph Client
        App[Mobile App]
    end

    App -- "POST /reports" --> API[Ingest API]
    API --> Dirty[(Dirty Reports Table)]

    Job[Clustering/Dedup Batch Job] -- reads unprocessed rows --> Dirty
    Job -- lease/lock per partition --> Lock[(Partition Lock Table)]
    Job -- writes/updates --> Clean[(Clean Incidents Table)]
    Job -- new/updated incident --> Queue[[Notification Queue - Kafka]]

    Queue --> NotifWorker[Notification Worker]
    NotifWorker -- lookup subscribers near incident --> Subs[(Subscriptions Table)]
    NotifWorker -- send push --> APNs[APNs / FCM]
    APNs --> App

    App -- "GET /incidents?bbox= or cell=" --> ReadAPI[Read API]
    ReadAPI -- geo+time query --> Clean

    Job -.timeout exceeded.-> OnCall[Page On-Call]
```

## Report submission -> notification (sequence)

```mermaid
sequenceDiagram
    participant U as User (reporter)
    participant API as Ingest API
    participant D as Dirty Table
    participant J as Clustering Job
    participant C as Clean Table
    participant Q as Kafka Queue
    participant N as Notification Worker
    participant P as APNs/FCM
    participant O as Other Users (subscribed)

    U->>API: POST /reports {category, lat, lng, ts}
    API->>D: insert raw report
    API-->>U: 202 Accepted

    Note over J: runs on a fixed interval, one job per (category, region) partition
    J->>D: read unprocessed rows for partition
    J->>C: match against open incidents (category + radius, no time cutoff)
    alt match found
        J->>C: update incident (report_count++, last_seen, severity)
    else no match
        J->>C: create new incident (status=open)
    end
    J->>D: mark rows processed (same tx as clean write)
    J->>Q: publish incident-updated event

    Q->>N: consume event
    N->>N: find subscribers near incident location
    N->>P: send push payload per device token
    P->>O: deliver notification
```

## Read path (map polling)

```mermaid
sequenceDiagram
    participant U as User (viewer)
    participant R as Read API
    participant C as Clean Table (PostGIS)

    Note over U: poll every ~20s while app open,<br/>~5min in background
    U->>R: GET /incidents?lat=&lng=&radius= (or cell id)
    R->>C: ST_DWithin + status=open query
    C-->>R: incidents in range
    R-->>U: incident list
```

## Key entities (rough shape, not final schema)

```
reports (dirty, append-only ingest)
  id, user_id, category, lat, lng, media_url, created_at, processed (bool)

incidents (clean, source of truth for reads/notifications)
  id, category, lat, lng, first_seen, last_seen, status (open/closed),
  report_count, severity

subscriptions
  device_token, user_id, area (geo-cell or bounding box), created_at

job_locks
  partition_key (category+region), holder_id, lease_expires_at
```

## Open design decisions still worth stress-testing

- Batch interval / job timeout tuning (currently: target 5 min, page on-call if exceeded).
- Incident "closed" threshold per category (quiet-period before an incident stops matching new reports).
- Coordinated-abuse detection signal (device fingerprint / IP clustering / trust score) — currently unspecified.
- Cold storage / TTL policy for closed incidents.
