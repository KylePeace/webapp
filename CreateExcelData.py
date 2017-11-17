#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xlwt
import xlrd
from datetime import  datetime
from xlutils.copy import copy
import os

class CreateExcelData(object):
    """创建Excel"""
    #path:"excel/xxx.xls"
    def __init__(self,sheetname,path):
        super(CreateExcelData, self).__init__()
        self.style = xlwt.XFStyle()
        self.excel = None
        self.excel_and_sheet_name(sheetname)
        self.set_style()
        self.path = path
        
    def set_style(self):
        font=xlwt.Font()
        font.name="Times New Roman"         
        font.height=220
        font.bold=False
        font.colour_index=4
      
        borders=xlwt.Borders()
        borders.left=6
        borders.right=6
        borders.top=6
        borders.bottom=6

        self.style.font=font
        self.style.borders=borders

    #param 1.str 2.[strname1,strname2]
    def excel_and_sheet_name(self,path,sheetname):
        if os.path.exists(path): #判断是否存已经存在文件
            print("文件存在，打开已经存在的文件")
            TC_workbook=xlrd.open_workbook(r"NewCreateWorkbook.xls")
            try:
                self.excel = TC_workbook.sheet_by_name(sheetname)
            except IOError as identifier:
                print("打开文件失败，因为sheet不存在")
            return
        else: #创建excel     
            new_workbook=xlwt.Workbook()
            for value in sheetname:
                new_sheet=new_workbook.add_sheet(value) 
            self.excel = new_workbook

    def write_to_excel(self,x,y,data):
        '''Write content to a new excel'''
    
        new_sheet=self.excel.add_sheet("SheetName_test")
        new_sheet.write(0,0,"hello") 
        new_sheet.write(0,1,"world",self.style)  
        
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
        style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
        new_sheet.write(1, 0, 1234.56, style0)
        new_sheet.write(1, 1, datetime.now(), style1)
        
        #write cell with formula
        new_sheet.write(2,0,5)
        new_sheet.write(2,1,8)
        new_sheet.write(3,0, xlwt.Formula("A3+B3"))

        new_workbook.save(r"excel/NewCreateWorkbook.xls")         #if change to xlsx,then open failedCreateExcelData

    def save_excel():
        self.excel.save(self.path)