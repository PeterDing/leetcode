# -*- coding=utf-8 -*-

# python3

import json
import sys
import re
import os
import argparse
import requests
from lxml import html as lxml_html

import html

from hide_problem import get_hide_problems


DATA_FILE = '../data/leetcode_problems.json'
OUT_FILE = '../data/leetcode_problems.txt'


class LeetcodeProblems(object):

    def __init__(self):
        if os.path.exists(DATA_FILE):
            problem_infos = json.load(open(DATA_FILE))
            self.problem_infos = {int(i): v for i, v in problem_infos.items()}
        else:
            self.problem_infos = {}

        self.hide_problems = get_hide_problems()

    def _save_data(self):
        with open(DATA_FILE, 'w') as g:
            json.dump(self.problem_infos, g,
                      indent=4,
                      ensure_ascii=False,
                      sort_keys=True)

    def get_problems_info(self):
        leetcode_url = 'https://leetcode.com/api/problems/all/'
        res = requests.get(leetcode_url)
        if not res.ok:
            print('request error')
            self._save_data()
            sys.exit()
        infos = res.json()
        for info in infos['stat_status_pairs']:
            title = info['stat']['question__title']
            level = info['difficulty']['level']
            question_id = info['stat']['question_id']

            if question_id in self.problem_infos:
                continue

            uri = info['stat']['question__title_slug'] or info['stat']['question__article__slug']
            problem_url = 'https://leetcode.com/problems/{}/description/'.format(uri)
            if info['paid_only']:
                if question_id in self.hide_problems:
                    description = self.hide_problems[question_id]
                    tags = []
                else:
                    print(' ! need to pay: {}, {}'.format(question_id, problem_url))
                    continue
            else:
                try:
                    res = requests.get(problem_url)
                except Exception:
                    self._save_data()
                    continue

                if not res.ok:
                    print('request error: {}'.format(info))
                    self._save_data()
                    continue

                tree = lxml_html.fromstring(res.text)

                description = tree.xpath('//meta[@name="description"]/@content')
                if description:
                    description = description[0]
                else:
                    description = tree.xpath('//meta[@property="og:description"]/@content')[0]
                description = html.unescape(description.strip())
                tags = tree.xpath('//div[@id="tags-topics"]/a/text()')

            problem = {
                'title': title,
                'level': level,
                'question_id': question_id,
                'description': description,
                'tags': tags
            }
            self.problem_infos[question_id] = problem

            print('get - {}: {}'.format(question_id, title))


    def to_text(self):
        if self.args.index:
            key = 'question_id'
        elif self.args.title:
            key = 'title'
        elif self.args.tag:
            key = 'tags'
        elif self.args.level:
            key = 'level'
        else:
            key = 'question_id'

        pm_infos = list(self.problem_infos.values())

        infos = sorted(pm_infos, key=lambda i: i[key])

        text_template = '## {question_id} - {title}\n' \
            '~{level}~  {tags}\n' \
            '{description}\n' + '\n' * self.args.line
        text = ''
        for info in infos:
            if self.args.rm_blank:
                info['description'] = re.sub(r'[\n\r]+', r'\n', info['description'])
            text += text_template.format(**info)

        with open(OUT_FILE, 'w') as g:
            g.write(text)

    def run(self):
        self.get_problems_info()
        self._save_data()

        print('find %s problems.' % len(self.problem_infos))
        self.to_text()


def handle_args(argv):
    p = argparse.ArgumentParser(description='extract all leecode problems to location')
    p.add_argument('--index', action='store_true', help='sort by index')
    p.add_argument('--level', action='store_true', help='sort by level')
    p.add_argument('--tag', action='store_true', help='sort by tag')
    p.add_argument('--title', action='store_true', help='sort by title')
    p.add_argument('--rm_blank', action='store_true', help='remove blank')
    p.add_argument('--line', action='store', type=int, default=10, help='blank of two problems')
    p.add_argument('-r', '--redownload', action='store_true', help='redownload data')
    args = p.parse_args(argv[1:])
    return args


def main(argv):
    args = handle_args(argv)
    x = LeetcodeProblems()
    x.args = args
    x.run()

if __name__ == '__main__':
    argv = sys.argv
    main(argv)
