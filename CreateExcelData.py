#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import xlwt
import xlrd
from xlutils.copy import copy
import datetime


class CreateExcelData(object):
    """创建Excel"""
    # path:"excel/xxx.xls"
    def __init__(self, sheetname, path):
        #super(CreateExcelData, self).__init__()
        self.style = xlwt.XFStyle()
        self.excel = None
        self.excelSheet =None
        self.sheetname = sheetname
        self.path = path
        self.set_style()
        self.excel_and_sheet_name()

    # style
    def set_style(self):
        font = xlwt.Font()
        font.name = "Times New Roman"
        font.height = 220
        font.bold = False
        font.colour_index = 4

        borders = xlwt.Borders()
        borders.left = 6
        borders.right = 6
        borders.top = 6
        borders.bottom = 6

        self.style.font = font
        self.style.borders = borders

    # param 1.str 2.[strname1,strname2]
    def excel_and_sheet_name(self):
        if os.path.exists(self.path):  # 判断是否存已经存在文件
            print("文件存在，打开已经存在的文件")
            self.isExistExcel = True
            TC_workbook = xlrd.open_workbook(r"NewCreateWorkbook.xls",formatting_info=True)
            try:
                self.excel = copy(TC_workbook)
                self.excelSheet = self.excel.sheet_by_name(self.sheetname)
                
            except IOError as identifier:
                print("打开文件失败，因为sheet不存在")
            return
        else:  # 创建excel
            print("创建excel表")
            self.excel = xlwt.Workbook()
            self.excelSheet = self.excel.add_sheet(self.sheetname)
            
    #写入excel
    def write_to_excel(self, y, x, data):   
        self.excelSheet.write(y, x, data)

    # 表头
    def write_titel(self,data):
        cur_row = 0
        for item in data:
            self.write_to_excel(0, cur_row, item)
            cur_row += 1
    #参数：titleData 表头 data：内容
    def write_content(self, data, titleData=None, cur_y=2, cur_x=0,isSave=True):
        if titleData:
            self.write_titel(titleData)

        for itemlist in data:
            for item in itemlist:
                self.write_to_excel(cur_y, cur_x,item)
                cur_x += 1
            cur_x = 0
            cur_y += 1 

        if isSave:
            self.save_excel()

    def save_excel(self):
        self.excel.save(self.path)
        print("创建excel表成功")


if __name__ == '__main__':
    now = datetime.datetime.now()
    name = now.strftime('%Y-%m-%d')
    excel = CreateExcelData("content","excel/"+name+".xlsx")
    # excel.write_to_excel(0,0,"开学")
    #excel.write_to_excel(0,1, "开学la")
    # excel.save_excel()
    data = [["kai","xew"],["fuck","you"]]
    print(data)
    titledata = ["888","999"]
    excel.write_content(data,titledata)

