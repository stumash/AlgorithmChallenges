let mergesort xs =
    let merged xs ys =
        let rec merged' xs ys acc =
            match xs,ys with
            | [],[] -> acc
            | xs,[] -> (List.rev xs) @ acc
            | [],ys -> (List.rev ys) @ acc
            | hx::tx, hy::ty ->
                if hx < hy then merged' tx ys (hx::acc)
                else merged' xs ty (hy::acc) in
        List.rev @@ merged' xs ys [] in
    let rec mergesort' xs =
        match xs with
        | [] | [_] -> xs
        | _ ->
            let mid = (List.length xs) / 2 in
            let lo_half, hi_half = (Core.List.take xs mid), (Core.List.drop xs mid) in
            merged (mergesort lo_half) (mergesort hi_half) in
    mergesort' xs
