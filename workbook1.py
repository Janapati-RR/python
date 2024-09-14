import xlsxwriter
workbook1 = xlsxwriter.workbook("test1123.xlsx")
worksheet1 = workbook1.add_worksheet("firstsheet")
worksheet1.write("0","0","test")
workbook1.close()