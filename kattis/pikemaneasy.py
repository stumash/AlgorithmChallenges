from heapq import heapify, heappop

def main():
    tokens = (int(x) for x in input().split(' '))
    n = next(tokens)
    t_tot = next(tokens)

    tokens = (int(x) for x in input().split(' '))
    a = next(tokens)
    b = next(tokens)
    c = next(tokens)
    dur_0 = next(tokens)

    def durlist():
        dur = dur_0
        retval = [dur]
        count = 1
        while (count < n):
            dur = (a * dur + b) % c + 1
            retval.append(dur)
            count += 1
        return retval

    durs = durlist()
    heapify(durs)

    count = 0
    pen = 0
    t = heappop(durs)
    while (t <= t_tot):
        count += 1
        pen += t
        if (count < n):
            t += heappop(durs)
        else:
            break

    print(count, pen % 1000000007)

if __name__ == "__main__":
    main()
