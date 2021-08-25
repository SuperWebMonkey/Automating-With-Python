#  https://www.youtube.com/watch?v=7YS6YDQKFh0 , on 11:00

from openpyxl import Workbook, load_workbook

wb = load_workbook('excel-files/jobs.xlsx')
ws = wb.active
print(ws)
