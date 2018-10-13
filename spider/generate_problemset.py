import json
import os
import urllib

from leetcode_spider import DATA_FILE

PROBLEMSET_DIR = '../problems/'

README_TEMPLATE = open('README_TEMPLATE.md').read()

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
        if os.path.exists(problem_dir):
            continue

        os.makedirs(problem_dir)

        readme_path = os.path.join(problem_dir, 'README.md')
        if os.path.exists(readme_path):
            continue

        difficulty = DIFFICULTIES[info['level']]
        tags = ', '.join(info['tags'])
        desc = info['description']
        url = info['url']
        readme = README_TEMPLATE.format(
            problem_id=problem_id,
            title=title,
            difficulty=difficulty,
            tags=tags,
            desc=desc,
            url=url)
        with open(readme_path, 'w') as g:
            g.write(readme)

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
