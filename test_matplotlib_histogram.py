from matplotlib.font_manager import FontProperties
from collections import Counter
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']  # X 轴可以显示中文
mpl.rcParams['axes.unicode_minus'] = False  # X 轴可以显示中文

font = FontProperties(fname='SIMYOU.TTF', size=14)
f3 = open('commont_philips.txt', 'r').read()
nowords = ['x', 'uj', 'a', 'ul', 'p', 'd', 'v', 'zg', 'm', 'ug', 'i', 'f', 'ad', 'nz', 'r', 'r', 'ns', 'q', 't', 'c']

wods = [x.word for x in psg.cut(f3) if len(x.word) >= 2 and (x.flag) not in nowords]
word_count = Counter(wods)
print(word_count)

x = [x[0] for x in word_count.most_common(20)]  # 统计top20个关键字
y = [x[1] for x in word_count.most_common(20)]  # 统计top20个关键字出现的次数
fig = plt.figure()
plt.grid(False)
# c = np.random.randint(0,1,len(y))
plt.bar(x, y, color='lightskyblue')
plt.xlabel('评论项目', FontProperties=font)
plt.ylabel('评论数量', FontProperties=font)
plt.title('京东评论柱状图', FontProperties=font)
plt.show()