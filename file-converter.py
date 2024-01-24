import sys
import os
import markdown


print(sys.argv)
if not sys.argv[1] == "markdown":
    raise ValueError("コマンドが不正" + sys.argv[1])
inputfile = sys.argv[2]
if not os.path.isfile(inputfile):
    raise ValueError("入力ファイルなし" + inputfile)
if not os.access(inputfile, os.R_OK):
    raise PermissionError("入力ファイルが読み取り不可" + inputfile)

contents = ""

with open(inputfile, "r", encoding="utf-8") as f:
    contents = f.read()

htmlContent = markdown.markdown(contents)

outputFileName = inputfile = sys.argv[3]
# outputpathにファイルを作成
with open("output/" + outputFileName + ".html", "w", encoding="utf-8") as f:
    f.write(htmlContent)
