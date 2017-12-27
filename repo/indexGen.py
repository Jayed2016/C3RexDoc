import os, glob, json
import os.path as op

myPath = op.dirname(op.realpath(__file__))
mdF = open(op.join(myPath, "index.md"), "w")
serverRoot = "https://rexrainbow.github.io/C3RexDoc/repo/"

l = """\
|Index|Icon|Addon name|
|-----|----|----------|\
"""
mdF.write(l)

names = glob.glob(op.join(myPath, "*.c3addon"))
for idx, p in enumerate(names):
    name = op.split(p)[1]
    l = """|{idx}|<img src="{server}{iconName}" width="50" heigh="50">|[{name}]({server}{name})|\n""".format(
        idx=idx+1, 
        name=name,         
        server=serverRoot,
        iconName=name.replace("c3addon", "png")
        )

    mdF.write(l)

mdF.close()