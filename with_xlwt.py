#!/usr/bin/env python

def create_xls(xlsname, sheetname):
    import xlwt

    data = {}
    data['userid'] = [23,4,36,14,1,63,123]
    data['useremail'] = [
        'x3sd@sfsf.com',
        'x5sd@sfsf.com',
        'x2sd@sfsf.com',
        'x4sd@sfsf.com',
        'xasd@sfsf.com',
        'x35sd@sfsf.com',
        'x234sd@sfsf.com',
    ]

    xls = xlwt.Workbook()
    xls.add_sheet(sheetname)

    xls.get_sheet(0).write(0, 0, 'userid')
    xls.get_sheet(0).write(0, 1, 'useremail')

    for x in enumerate(zip(data['userid'], data['useremail'])):
        xls.get_sheet(0).write(x[0]+1, 0, str(x[1][0]))
        xls.get_sheet(0).write(x[0]+1, 1, str(x[1][1]))

    xls.save(xlsname)

def import_xls(xlsname, sheetname):
    import xlrd

    xls = xlrd.open_workbook(xlsname)
    sheet = xls.sheet_by_name(sheetname)
   
    for x in zip(sheet.col(0), sheet.col(1)):
        print x[0].value, '\t', x[1].value

if __name__ == '__main__':
    create_xls('all-log-xlwt.xls', 'user-info')
    #import_xls('all-log-xlwt.xls', 'user-info')
