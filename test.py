#! /usr/bin/env python
# -*- coding: utf-8 -*-
#python使用excel 方法
import xlwt
import xlrd
from datetime import  datetime
from xlutils.copy import copy

def set_style(font_name,font_height,bold=False):
    style=xlwt.XFStyle()
    
    font=xlwt.Font()
    font.name=font_name         # 'Times New Roman'
    font.height=font_height
    font.bold=bold
    font.colour_index=4
    
    borders=xlwt.Borders()
    borders.left=6
    borders.right=6
    borders.top=6
    borders.bottom=6
    
    style.font=font
    style.borders=borders
    return style

def write_to_excel_xlwt():
    '''Write content to a new excel'''
    new_workbook=xlwt.Workbook()
    new_sheet=new_workbook.add_sheet("SheetName_test")
    new_sheet.write(0,0,"hello") 
    #write cell with style
    new_sheet.write(0,1,"world",set_style("Times New Roman", 220, True))  
    
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    new_sheet.write(1, 0, 1234.56, style0)
    new_sheet.write(1, 1, datetime.now(), style1)
    
    #write cell with formula
    new_sheet.write(2,0,5)
    new_sheet.write(2,1,8)
    new_sheet.write(3,0, xlwt.Formula("A3+B3"))

    new_workbook.save(r"NewCreateWorkbook.xls")         #if change to xlsx,then open failed
   


def read_excel_xlrd():
    '''Read Excel with xlrd'''
    #file
    TC_workbook=xlrd.open_workbook(r"NewCreateWorkbook.xls")

    #sheet
    all_sheets_list=TC_workbook.sheet_names()
    print("All sheets name in File:",all_sheets_list)
    
    first_sheet=TC_workbook.sheet_by_index(0)
    print("First sheet Name:",first_sheet.name)
    print("First sheet Rows:",first_sheet.nrows)
    print("First sheet Cols:",first_sheet.ncols)
    
    second_sheet=TC_workbook.sheet_by_name("SheetName_test")
    print("Second sheet Rows:",second_sheet.nrows)
    print("Second sheet Cols:",second_sheet.ncols)
    
    first_row=first_sheet.row_values(0)
    print("First row:",first_row)
    first_col=first_sheet.col_values(0)
    print("First Column:",first_col)
    
    # cell
    cell_value=first_sheet.cell(1,0).value
    print("The 1th method to get Cell value of row 2 & col 1:",cell_value)
    cell_value2=first_sheet.row(1)[0].value
    print("The 2th method to get Cell value of row 2 & col 1:",cell_value2)
    cell_value3=first_sheet.col(0)[1].value
    print("The 3th method to get Cell value of row 2 & col 1:",cell_value3)


def write_to_existed_file():
    '''Write content to existed excel file with xlrd&xlutils&xlwt'''
    rb = xlrd.open_workbook(r"NewCreateWorkbook.xls",formatting_info=True)

    wb = copy(rb)
    ws = wb.get_sheet(0) #sheet:写入读写，wb，rb：用于保存
    
    font=xlwt.Font()
    font.name="Times New Roman"
    font.height=220
    font.bold=False
    
    borders = xlwt.Borders()
    borders.left = xlwt.Borders.THIN
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 2
    
    cell_style = xlwt.XFStyle()
    cell_style.font = font
    cell_style.borders = borders
    cell_style.pattern = pattern
    
    ws.write(10,5,"hello world",cell_style)
    wb.save(r"NewCreateWorkbook.xls")

if __name__=="__main__":
    #write_to_excel_xlwt()
    #read_excel_xlrd()
    write_to_existed_file()