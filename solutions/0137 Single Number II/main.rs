impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let majority_repeat_num = 3;
        let minority_repeat_num = 1usize;

        // `counts` stores numbers which represent as following,
        // If the j-th bit of counts[i] is 1, there are `majority_repeat_num - i` bits at the j-th
        // position for now.
        let mut counts: Vec<i32> = vec![];
        for _ in 0..majority_repeat_num {
            counts.push(0);
        }

        for e in nums {
            let mut e = e;
            for i in 0..majority_repeat_num - 1 {
                // mask represents the increasing of new counts[i]
                let mask = counts[i + 1] & e;
                // update counts[i]
                counts[i] |= mask;
                // remove these bits of counts[i + 1] which used as above
                counts[i + 1] ^= mask;
                // remove these bits of e which used as above
                e ^= mask;
            }
            // add rest of bit of e to count[-1]
            counts[majority_repeat_num - 1] |= e;
        }

        // counts[majority_repeat_num - minority_repeat_num] is the result
        let r = counts[majority_repeat_num - minority_repeat_num];
        r
    }
}
