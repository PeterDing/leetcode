# Leetcode

There are some scripts to crawl leetcode problems and to convert these problems to markdown format.

## Usage

- Crawl problems

```bash
cd spider
python3 leetcode_spider.py
```

`leetcode_spider.py` crawls leetcode problems then stores at `data` directory.

- Convert problems to markdown format

```bash
cd spider
python3 generate_problemset.py
```

`generate_problemset.py` converts leetcode problems to `problems` directory.

[Here](problems/README.md) is an index of problems.
