from glob import glob

paths = sorted(glob("0*/solute.py"))

with open("summary.md", "w") as fd:
    for path in paths:
        cn = open(path).read()

        title, _ = cn.split("\n", 1)
        title = title.strip("# ")

        fd.write(f"- **{title}**\n")
        fd.write("  ```python\n")
        fd.write("  " + cn.replace("\n", "\n  "))
        fd.write("  ```\n\n")
