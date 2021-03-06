import os, glob, json
import os.path as op

myPath = op.dirname(op.realpath(__file__))
mdF = open(op.join(myPath, "index.md"), "w")
serverRoot = "https://rexrainbow.github.io/C3RexDoc/repo/"

l = """\
|Icon|Download|
|----|--------|
"""
mdF.write(l)

names = glob.glob(op.join(myPath, "*.c3addon"))
for p in names:
    name = op.split(p)[1]
    l = """|<img src="{server}{iconName}" width="40" heigh="40">|[{name}]({server}{name})|\n""".format(
        name=name,         
        server=serverRoot,
        iconName=name.replace("c3addon", "png")
        )

    mdF.write(l)

l = """  \n{idx} addons  \n""".format(
    idx=len(names)
)
mdF.write(l)
l = """  \n[Icon](https://icons8.com/)"""
mdF.write(l)

mdF.close()