import json
import os
import urllib

import html2text

from leetcode_spider import DATA_FILE

from util import to_format

PROBLEMSET_DIR = '../problems/'

README_TEMPLATE = open('README_TEMPLATE.md').read()
SOLUTION_TEMPLATE = open('SOLUTION_TEMPLATE.md').read()

DIFFICULTIES = {
    1: 'Easy',
    2: 'Medium',
    3: 'Hard',
}


def load_data():
    return json.load(open(DATA_FILE))


def generate_problemset(data):
    changed = False
    dirs = []
    for problem_id, info in data.items():
        title = info['title']
        dir_name = '{:0>4} {}'.format(problem_id, title)

        dirs.append(dir_name)

        problem_dir = os.path.join(PROBLEMSET_DIR, dir_name)
        if not os.path.exists(problem_dir):
            os.makedirs(problem_dir)

        readme_path = os.path.join(problem_dir, 'README.md')

        difficulty = DIFFICULTIES[info['level']]
        tags = ', '.join(info['tags'])
        if info['json']:
            desc = info['description']
        else:
            cn = info['description']
            cn = to_format(cn)
            desc = '```\n{}\n```'.format(cn)

        similar_problems = ''
        for prob in info['similar_problems']:
            line = '- [{}] [{}]({})\n\n'.format(
                prob['difficulty'], prob['title'], prob['titleSlug']
            )
            similar_problems += line

        url = info['url']
        readme = README_TEMPLATE.format(
            problem_id=problem_id,
            title=title,
            difficulty=difficulty,
            tags=tags,
            desc=desc,
            similar=similar_problems,
            url=url
        )
        with open(readme_path, 'w') as g:
            g.write(readme)

        if info['solution']:
            solution = SOLUTION_TEMPLATE.format(
                problem_id=problem_id,
                title=title,
                difficulty=difficulty,
                tags=tags,
                desc=desc,
                similar=similar_problems,
                solution=info['solution'],
                url=url
            )
            solution_path = os.path.join(problem_dir, 'leetcode-solution.md')
            with open(solution_path, 'w') as g:
                g.write(solution)

        changed = True

    dirs.sort()
    if changed:
        readme_path = os.path.join(PROBLEMSET_DIR, 'README.md')
        readme = ''.join(['- [{}]({})\n'.format(d, urllib.parse.quote(d)) for d in dirs])
        with open(readme_path, 'w') as g:
            g.write(readme)


def main():
    data = load_data()
    generate_problemset(data)


if __name__ == '__main__':
    main()
