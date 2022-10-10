import json
import xlwt
import sys
import os
from collections import defaultdict

if sys.argv[1] == "help":
  print("Usage:\n\tjsonToExcel.py json_file.json")
  sys.exit(1)

if not os.path.exists(sys.argv[1]):
  print("Cannot open " + sys.argv[1])
  sys.exit(1)

file_name = sys.argv[1]
file_extenstion = file_name.split(".")[-1]

if not file_extenstion in ("json"):
  print("The extension of JSON file is incorrect")
  sys.exit(1)

file = open(file_name)
json_text = file.read()

try:
  imported_json = defaultdict(json.loads(json_text))
except:
  print("The content of the JSON file is incorrect")
  sys.exit(1)

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("json exported")

columns = list(imported_json[0].keys())

i = 0
for column in columns:
  worksheet.write(0, i, column)
  i += 1

j = 1
for row in imported_json:
  i = 0
  for column in columns:
    worksheet.write(j, i, row[column])
    i += 1
  j += 1

try:
  workbook.save(file_name.split(".")[0] + ".xls")
  sys.exit(0)
except:
  print("Cannot create the xls file")
  sys.exit(1)
