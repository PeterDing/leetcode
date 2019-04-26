# -*- coding=utf-8 -*-

# python3

import json
import sys
import os
import argparse
import requests
import html2text

from hide_problem import get_hide_problems

from util import to_format

DATA_FILE = '../data/leetcode_problems.json'
OUT_FILE = '../data/leetcode_problems.md'

API_URL = 'https://leetcode.com/graphql'
DATA = '{"operationName":"questionData","variables":{"titleSlug":"%s"},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    solution {\n      id\n      url\n      content\n      contentTypeId\n      canSeeDetail\n      rating {\n        id\n        count\n        average\n        userRating {\n          score\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}'.replace(
    '\n', r'\n'
)
PROBLEM_URL = 'https://leetcode.com/problems/'

HEADERS = {
    'accept-encoding': 'gzip',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5',
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'authority': 'leetcode.com',
    'content-type': 'application/json',
}


class LeetcodeProblems:

    def __init__(self):
        if os.path.exists(DATA_FILE):
            problem_infos = json.load(open(DATA_FILE))
            self.problem_infos = {int(i): v for i, v in problem_infos.items()}
        else:
            self.problem_infos = {}

        self.hide_problems = get_hide_problems(set(self.problem_infos.keys()))

        headers = {
            'authority': 'leetcode.com',
            'user-agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'accept':
                'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6,ja;q=0.5',
        }
        res = requests.get('https://leetcode.com/', headers=headers)
        self.cookies = res.cookies

    def _save_data(self):
        with open(DATA_FILE, 'w') as g:
            json.dump(self.problem_infos, g, indent=4, ensure_ascii=False, sort_keys=True)

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
            raw_question_id = info['stat']['question_id']
            question_id = info['stat']['frontend_question_id']
            title_slug = info['stat']['question__title_slug'] \
                or info['stat']['question__article__slug']
            paid_only = info['paid_only']
            problem_url = PROBLEM_URL + title_slug
            origin_json = None
            tags = []
            similar_problems = []
            solution = None

            if question_id in self.problem_infos:
                if 'paid_only' not in self.problem_infos[question_id]:
                    self.problem_infos[question_id]['paid_only'] = paid_only
                continue

            if paid_only:
                if question_id in self.hide_problems:
                    description = self.hide_problems[question_id]
                else:
                    print(' ! need to pay: {}, {}'.format(question_id, problem_url))
                    continue
            else:
                headers = dict(HEADERS)
                headers['referer'] = problem_url
                csrftoken = self.cookies.get('csrftoken')
                headers['x-csrftoken'] = csrftoken
                data = DATA % title_slug
                try:
                    res = requests.post(API_URL, headers=headers, cookies=self.cookies, data=data)
                except Exception:
                    print(' ! request error:', title_slug)
                    self._save_data()
                    continue

                if not res.ok:
                    print('request error: {}, response: {}'.format(title_slug, res.text))
                    self._save_data()
                    continue

                js = res.json()
                description = js['data']['question']['content']

                if js['data']['question']['topicTags']:
                    for item in js['data']['question']['topicTags']:
                        tags.append(item['name'])
                origin_json = res.text

                similar_problems = json.loads(
                    js['data']['question'].get('similarQuestions') or '[]'
                )
                solution = (js['data']['question']['solution'] or {}).get('content')

            problem = {
                'title': title,
                'level': level,
                'raw_question_id': raw_question_id,
                'question_id': question_id,
                'description': description,
                'solution': solution,
                'tags': tags,
                'url': problem_url,
                'slug': title_slug,
                'paid_only': paid_only,
                'similar_problems': similar_problems,
                'json': origin_json,
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

        text_template = '<h2># {question_id} - {title}</h2>\n\n' \
            '<hr>' \
            '<p>Difficulty: <b>{level}</b>; Tags: {tags}</p>\n\n' \
            '<br>' \
            '{description}\n' + '<br>\n' * self.args.line
        text = ''
        for info in infos:
            desc = info['description']
            if not info['json']:
                desc = '```\n{}```'.format(desc)
            info['description'] = desc
            text += text_template.format(**info)

        with open(OUT_FILE, 'w') as g:
            g.write(text)

    def run(self):
        self.get_problems_info()
        self._save_data()

        print('find %s problems.' % len(self.problem_infos))
        #  self.to_text()


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
