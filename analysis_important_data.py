import pandas as pd
from pandas import DataFrame
import jieba
import numpy
from matplotlib.font_manager import  FontProperties
from pylab import *
import matplotlib.pyplot as plt
#数据进一步清洗
read_excel=pd.read_excel('C:\\Users\\Administrator\\Desktop\\预处理.xlsx')
DF=DataFrame(read_excel,columns=['人气','分类'])
df_to_dict=DF.to_dict(orient="list")
df=df_to_dict['分类']
df_clean_first=[str(i) for i in df]
df_clean_second=''.join(df_clean_first)
segment=jieba.lcut(df_clean_second)
words_df = pd.DataFrame({'segment':segment})
#print(words_df.ix[:10])
stopwords=pd.read_csv('E:\\pycharm_object\\chineseStopWords.txt',index_col=False,quoting=3,sep='\t',names=['stopword'],encoding='ISO-8859-1')
words_df=words_df[~words_df.segment.isin(stopwords)]
words_stat=words_df.groupby(by=['segment'])['segment'].agg({'计数':numpy.size})
words_stat=words_stat.reset_index().sort_values(by=['计数'],ascending=False)
word_frequence={x[0]:x[1] for x in words_stat.values}
print(word_frequence)
word_frequence_list=[]
word=[]
count=[]
for key in word_frequence:
    temp=(key,word_frequence[key])
    word.append(key)
    count.append(word_frequence[key])
    word_frequence_list.append(temp)
#柱状图可视化
mpl.rcParams['font.sans-serif']=['SimHei'] # X 轴可以显示中文
mpl.rcParams['axes.unicode_minus']= False # X 轴可以显示中文
font = FontProperties(fname= r'C:\Windows\Fonts\FZSTK.TTF',size=14)
# x = [word.most_common(20)]  # 统计top20个关键字
# y = [count.most_common(20)]  # 统计top20个关键字出现的次数
plt.bar(word[:10], count[:10], color='lightskyblue')#显示前十分类
plt.xlabel('出现词语', FontProperties=font)
plt.ylabel('出现次数', FontProperties=font)
plt.title('人气前一万分类词频分析', FontProperties=font)
plt.show()