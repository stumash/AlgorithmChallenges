open Core

(* all_extractions [1; 2; 3] -> [
 *     (3, [1; 2]);
 *     (2, [1; 3]);
 *     (1, [2; 3])
 * ] *)
let all_extractions xs =
    let rec all_extractions' acc pre xs =
        match xs with
        | [] -> acc
        | h::t -> all_extractions' ((h, pre@t)::acc) (pre@[h]) t
    in
    all_extractions' [] [] xs

(* permutations [1; 2; 3] -> [
 *     [3; 2; 1];
 *     [3; 1; 2];
 *     [2; 3; 1];
 *     [2; 1; 3];
 *     [1; 3; 2];
 *     [1; 2; 3]
 * ]
 * *)
let rec permutations = function
    | [] -> []
    | [h] -> [[h]]
    | xs ->
        let exts = all_extractions xs in
        List.concat (List.map exts (fun (h, t) ->
            List.map (permutations t) (fun p -> h::p)
        ))
