open Core.Fn

let powerset xs =
    let rec powerset' xs acc =
        match xs with
        | [] -> acc
        | h::t -> powerset' t @@ (List.map (fun ls -> h::ls) acc)@acc in
    powerset' xs [[]]

(* length of longest increasing subsequence *)
let len_lis xs =
    let len = List.length xs in
    let rev = List.rev xs in
    let memo = Hashtbl.create (((len * len) / 2) + (len / 2)) in
    let rec dp i j revi revj =
        if i = 0 then 1 else
        if Hashtbl.mem (i,j) then Hashtbl.find (i,j) else
        let x = dp (i-1) j () () in
        let y = if  then dp (i-1) () () () else 0 in
        let ans = max x (1+y) in
        Hashtbl.add memo (i,j) ans; ans
    in
    dp (len-1) (len-1) rev rev
