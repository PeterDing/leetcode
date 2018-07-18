# -*- coding=utf-8 -*-

import os
import re

import requests
import html2text

URL = 'http://www.cnblogs.com/grandyang/p/4606334.html'


def collect_problems(no_hided_ids):
    problems = {}

    html = requests.get(URL).text

    ids = re.findall(r'>(\d+)</td', html)
    trs = re.split(r'>\d+</td', html)[1:]
    assert len(ids) == len(trs)

    for i in range(len(ids)):
        if '$' not in trs[i]:
            continue

        key = int(ids[i])

        if key in no_hided_ids:
            continue

        mod = re.search(r'"(http://www\.cnblogs\.com/grandyang/.+?)"', trs[i])
        if not mod:
            continue
        url = mod.group(1)
        cn = requests.get(url).text
        description = search_problems(cn)
        if key in problems:
            continue
        problems[key] = description
    return problems


def search_problems(cn):
    _, t = cn.split('id="cnblogs_post_body"', 1)
    t = t[t.find('>') + 1:]
    ls = []
    chunks = t.split('\n')
    for chunk in chunks:
        if '。' in chunk or '，' in chunk:
            break
        ls.append(chunk)
    html = ''.join(ls)

    desc = html2text.unescape(html2text.html2text(html))
    desc = re.sub(r' +\n+', '\n', desc)
    desc = desc.strip()
    return desc


def get_hide_problems(no_hided_ids):
    problems = collect_problems(no_hided_ids)
    return problems
