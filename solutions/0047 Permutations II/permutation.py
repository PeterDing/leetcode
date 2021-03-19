def perm(nums):
    if len(nums) < 2:
        return [nums]

    rs = []
    e_set = set()
    for i, e in enumerate(nums):
        if e in e_set:
            continue
        for l in perm(nums[:i] + nums[i + 1:]):
            rs.append([e, *l])
        e_set.add(e)
    return rs


a = [1, 2, 3, 4]
ls = perm(a)
print(f'-> {len(ls)}')
for i in ls:
    print(i)
