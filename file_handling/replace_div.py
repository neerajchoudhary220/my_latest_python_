f = r"files/input.txt"
outputFile = r"files/output.txt"

f = open(f)
outputFile = open(outputFile,'a')
for line in f.readlines():
    div_replace = line.replace("</div>","<br></div>")
    outputFile.write(div_replace)

print("done")