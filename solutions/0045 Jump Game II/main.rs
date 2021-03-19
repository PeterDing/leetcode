pub fn jump(nums: Vec<i32>) -> i32 {
    let N = nums.len();
    if N < 2 {
        return 0;
    }

    let mut step = 0;
    let mut cur_index = 0usize;
    loop {
        if cur_index + nums[cur_index] as usize >= N - 1 {
            step += 1;
            break;
        }

        let mut next_index = 0;
        let mut max_jump_to = 0;
        for (ii, e) in nums[cur_index + 1..cur_index + 1 + nums[cur_index] as usize]
            .iter()
            .enumerate()
        {
            let max_jump_to_here = ii + cur_index + 1 + *e as usize;
            if max_jump_to_here >= max_jump_to {
                max_jump_to = max_jump_to_here;
                next_index = ii + cur_index + 1;
            }
        }

        cur_index = next_index;
        step += 1;
    }

    return step;
}

pub fn main() {
    // let a = jump(vec![2, 3, 1, 1, 4]);
    // let a = jump(vec![0]);
    // let a = jump(vec![1, 2]);
    let a = jump(vec![2, 3, 0, 1, 4]);
    // let a = jump(vec![1, 2, 3]);
    println!("{}", a);
}
