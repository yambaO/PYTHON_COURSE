import requests
import json
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Posts"

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
json_data = response.text
data = json.loads(json_data)

#create a new Spreadsheet

for row, post in enumerate(data, 1):
    for column, post_value in enumerate(post.values(), 1):
     ws.cell(row=row, column=column, value=str(post_value))
# save our spreadsheet

wb.save("/Users/yamba/Python_course/week_3/spreadsheets/demo_W3D3.xlsx")