import pandas as pd
from pandas import DataFrame
#数据预处理
#读取excel文件
read_excel_file=pd.read_excel('C:\\Users\\Administrator\\Desktop\\微信小程序.xlsx')
#用DataFrame处理excel表格
DF=DataFrame(read_excel_file,columns=['人气','小程序名称','分类','小程序介绍','标签'])
DF_sort=DF[['人气']].sort_index()
DF_more_ten_thousand=DF_sort[DF_sort['人气']>10000]
merge=pd.merge(DF_more_ten_thousand,DF,on='人气')
to_excel=merge.to_excel('C:\\Users\\Administrator\\Desktop\\预处理.xlsx')