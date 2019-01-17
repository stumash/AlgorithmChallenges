let powerset xs =
    let rec powerset' xs acc =
        match xs with
        | [] -> acc
        | h::t -> powerset' t @@ (List.map (fun ls -> h::ls) acc)@acc in
    powerset' xs [[]]
