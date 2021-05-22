impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        if nums.len() == 0 {
            return;
        }

        nums.reverse();

        let mut i = 0usize;
        let mut hitted = false;

        while i < nums.len() - 1 {
            if nums[i] <= nums[i + 1] {
                i += 1;
                continue;
            }
            hitted = true;

            let t = nums[i + 1];

            for j in 0..i + 1 {
                if nums[j] > t {
                    let tmp = nums[i + 1];
                    nums[i + 1] = nums[j];
                    nums[j] = tmp;
                    break;
                }
            }
            nums[0..i + 1].reverse();
            break;
        }

        if hitted {
            nums.reverse();
        }
    }
}
