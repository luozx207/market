import xlrd
import xlwt

def read(file,flag):
    taocans = ['新套餐']
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    rows = table.nrows
    cols = table.ncols
    temp = table.col_values(0)#对应excel表中电话号码的列（从0开始）
    phones = [str(x).split('.')[0] for x in temp]
    peoples = table.col_values(1)#对应excel表中登记人的列
    tcs = table.col_values(4)
    for i in range(1,len(tcs)):
        if flag=='0':
            if '-' in tcs[i]:
                taocans.append(tcs[i].split('-')[1][:-1])
            elif tcs[i]=="腾讯大王卡":
                taocans.append(tcs[i])
        else:
            taocans.append(tcs[i])

    return phones,peoples,taocans

def write(result):
    file=xlwt.Workbook()
    table = file.add_sheet('sheet1')
    for i in range(len(result)):
        table.write(i,0,result[i][0])
        table.write(i,1,result[i][1])
        table.write(i,2,result[i][2])
    file.save('result.xls')


if __name__=="__main__":
    phones,peoples,tcs=read("D:/自动受理数据.xlsx")
    print (type(tcs[0]))
    for tc in tcs:
        print(tc)
