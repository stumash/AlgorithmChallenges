let powerset xs =
    let rec powerset' xs acc =
        match xs with
        | [] -> acc
        | h::t -> powerset' t @@ (List.map (fun ls -> h::ls) acc)@acc in
    powerset' xs [[]]

(* helpers *)
let zip xs ys =
    let rec zip' xs ys acc =
        match xs,ys with
        | h1::t1, h2::t2 -> zip' t1 t2 ((h1,h2)::acc)
        | _ -> acc
    in
    List.rev @@ zip' xs ys []

(* length of longest increasing subsequence *)
let len_lis ns =
    let ns = max_int::ns in
    let list_max = List.fold_left max 0 in
    let f memo n =
        let ns_ms = zip ns @@ List.rev memo in
        let valid_ms = List.map snd @@ List.filter (fun (n',m') -> n'<n) ns_ms in
        (1 + list_max valid_ms)::memo in
    list_max @@ List.fold_left f [] ns
