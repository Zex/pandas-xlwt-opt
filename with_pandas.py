#!/usr/bin/env python

def create_xls(xlsname, sheetname):
    from pandas import DataFrame

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

    xls = DataFrame(data)
    xls.to_excel(xlsname, sheetname, index=False)
#    print xls.to_html(index=False)

if __name__ == '__main__':
    create_xls('all-log-pandas.xls', 'user-info')
