import os, glob, json
import os.path as op

myPath = op.dirname(op.realpath(__file__))
mdF = open(op.join(myPath, "index.md"), "w")
serverRoot = "https://rexrainbow.github.io/C3RexDoc/addons/"

l = """\
|Icon|Download|
|----|--------|
"""
mdF.write(l)

names = [ name for name in os.listdir(myPath) if os.path.isdir(os.path.join(myPath, name)) ]
for p in names:
    name = op.split(p)[1]
    l = """|<img src="{server}/{name}/icon.png" width="40" heigh="40">|[{name}]({server}/{name}/addon.json)|\n""".format(
        name=name,         
        server=serverRoot
        )

    mdF.write(l)

l = """  \n{idx} addons  \n""".format(
    idx=len(names)
)
mdF.write(l)
l = """  \n[Icon](https://icons8.com/)"""
mdF.write(l)

mdF.close()