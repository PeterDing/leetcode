fn search(v: &Vec<i32>, start: i32, end: i32, target: i32, rs: &mut Vec<i32>) {
    if v[start as usize] == target || v[end as usize] == target {
        let i = {
            if v[start as usize] == target {
                start
            } else {
                end
            }
        };

        let mut s = i;
        loop {
            if v[s as usize] != target {
                s += 1;
                break;
            }
            if s == 0 {
                break;
            }
            s -= 1;
        }

        let mut e = i;
        loop {
            if v[e as usize] != target {
                e -= 1;
                break;
            }
            if e == v.len() as i32 - 1 {
                break;
            }
            e += 1;
        }

        println!("{}, {}", s, e);

        for ii in s..e + 1 {
            rs.push(ii as i32);
        }

        return;
    }

    if start + 1 == end {
        return;
    };

    let mid = (start + end) / 2;
    println!("mid: {}", mid);
    if v[mid as usize] <= target {
        search(v, mid, end, target, rs);
    } else {
        search(v, start, mid, target, rs);
    }
}

pub fn main() {
    let v = vec![1, 2, 3, 3, 5, 5, 6, 6, 33, 33, 89, 100];
    let target = 6;
    let mut r = vec![];
    search(&v, 0, (v.len() - 1) as i32, target, &mut r);

    println!("{:?}", r);
}
