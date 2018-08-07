# Author: Jiaci LIU

import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

comment = []

with open('xiezheng.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            comment.append(row.split(',')[4].replace('\n', ''))

comment_after_split = jieba.cut(str(comment), cut_all=False)

wl_space_split = ''.join(comment_after_split)

# 导入背景图
background_image = plt.imread('D://Users//32861//Desktop//CostModel-V1//xihongshi.jpg')
stopwords = STOPWORDS.copy()

# 可以加多个屏蔽词
stopwords.add('电影')
stopwords.add('一部')
stopwords.add('一个')
stopwords.add('不错')
stopwords.add('一般般')
stopwords.add('一般般吧')
stopwords.add('一般')
stopwords.add('还行吧')
stopwords.add('挺')
stopwords.add('没有')
stopwords.add('什么')
stopwords.add('有点')
stopwords.add('这部')
stopwords.add('这个')
stopwords.add('不是')
stopwords.add('还可以')
stopwords.add('还行')
stopwords.add('超级帅')
stopwords.add('非常')
stopwords.add('感觉')


# 设置云参数
# 参数分别指字体、背景颜色、最大词的大小、使用给定图作为背景形状

wc = WordCloud(width=1024, height=768, background_color='white',
               mask=background_image, font_path='C:\simhei.ttf',
               stopwords=stopwords,
               max_font_size=400,
               random_state=50)
wc.generate_from_text(wl_space_split)
img_colors = ImageColorGenerator(background_image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()

# 保存到本地
wc.to_file('D://Users//32861//Desktop//CostModel-V1')
