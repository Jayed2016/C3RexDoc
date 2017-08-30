import os, glob, json
import os.path as op

myPath = op.dirname(op.realpath(__file__))
mdF = open(op.join(myPath, "index.md"), "w")
serverRoot = "https://rexrainbow.github.io/C3RexDoc/repo/"

for f in glob.glob(op.join(myPath, "*.c3addon")):
  name = op.split(f)[1]
  mdF.write("- [{name}]({server}{name})  \n".format(name=name, server=serverRoot))

mdF.close()