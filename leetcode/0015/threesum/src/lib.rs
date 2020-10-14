#[cfg(test)]
mod tests {
    use std::collections::HashMap;
    use std::collections::HashSet;

    fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();

        let mut counts = HashMap::new();
        for n in &nums {
            *counts.entry(*n).or_insert(0) += 1
        }

        let len = nums.len();
        let mut so_far: HashSet<Vec<i32>> = HashSet::new();
        for i in 0..len {
            for j in (i + 1)..len {
                let (n1, n2) = (nums[i], nums[j]);
                let n3 = -(n1 + n2);
                if let Some(count) = counts.get(&n3) {
                    if n3 >= n2 {
                        let count_needed =
                            1 + if n2 == n3 { 1 } else { 0 } + if n1 == n3 { 1 } else { 0 };
                        if n3 > n2 || *count >= count_needed {
                            so_far.insert(vec![n1, n2, n3]);
                        }
                    }
                }
            }
        }

        so_far.into_iter().collect()
    }

    // [-1,-1,0,1,2,-4]

    #[test]
    fn test1() {
        assert!(test_input_and_output(
            vec![-1, 0, 1, 2, -1, -4],
            vec![vec![-1, -1, 2], vec![-1, 0, 1]]
        ));
    }

    #[test]
    fn test2() {
        assert!(test_input_and_output(
            vec![-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
            vec![
                vec![-4, -2, 6],
                vec![-4, 0, 4],
                vec![-4, 1, 3],
                vec![-4, 2, 2],
                vec![-2, -2, 4],
                vec![-2, 0, 2]
            ]
        ));
    }

    fn test_input_and_output(vecin: Vec<i32>, vecout: Vec<Vec<i32>>) -> bool {
        let mut result = three_sum(vecin);
        result.sort();

        let mut desired = vecout;
        desired.sort();

        result == desired
    }
}
