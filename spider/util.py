import re


def to_format(cn):
    cn = cn.replace('\r', '\n')
    cn = re.sub(r'\n+', r'\n', cn, flags=re.M)
    return cn
