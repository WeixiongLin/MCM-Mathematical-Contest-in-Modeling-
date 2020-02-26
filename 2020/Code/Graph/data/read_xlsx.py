#coding:utf-8
#all_data.xlsx把3个工作表合在一起了，但是打开很慢，主要因为fullevents比较大，
#所以还是拆成了三个xlsx文件
import xlrd
##################一、excel的读取操作xlrd######################
data =xlrd.open_workbook(r"matches.xlsx")
#0.打开excel操作
table = data.sheets()[0]       #通过索引顺序获取
table = data.sheet_by_index(0) #通过索引顺序获取
table = data.sheet_by_name(u'matches')#通过名称获取
 
#1. 获取excel sheet对象
table1 =data.sheets()[0]
table2=data.sheet_by_index(0)
table3=data.sheet_by_name(U"matches")
print(table1)
#<xlrd.sheet.Sheet object at 0x00000131D1B1BCF8>

#2. 获取sheet的行与列数量.
rows=table1.nrows
col =table1.ncols
print("行数为%s \n列数为%s"%(rows,col))

#3. 获取整行和整列的数据.
row =table1.row_values(0)
col =table1.col_values(2)
print(row)

#4.获取单元格数据
cell_a1 =table1.cell_value(0,0)
cell_x =table1.cell_value(2,3) #(第三行，第四列数据) 
print(cell_a1)
