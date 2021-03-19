pub fn main() {
    let mut a = 43261596u32;
    let mut r = 0u32;
    let m = 1u32;
    for _ in 0..32 {
        let one = m & a;
        r = r << 1;
        if one == 1u32 {
            r += 1;
        }
        a = a >> 1;
    }
    println!("{}", r);
    println!("{}", 1 << 3);
}
