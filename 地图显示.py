# Author: Jiaci LIU


from pyecharts import Style
from pyecharts import Geo


city = []
with open('xiezheng.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            city.append(row.split(',')[2].replace('\n', ''))


def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result


data = []
for item in all_list(city):
    data.append((item, all_list(city)[item]))
    style = Style(
        title_color='#fff',
        title_pos='center',
        width=1200,
        height=600,
        background_color="#404a59"
    )


geo = Geo('小白粉丝人群地理地图', "数据来源：恋习小白", **style.init_style)
attr, value = geo.cast(data)
# geo.add_coordinate('广安', 30.01, 105.56)
geo.add("", attr, value,
        visual_range=[0, 20],
        visual_text_color='#fff',
        symbol_size=20,
        is_visualmap=True,
        is_piecewise=True,
        visual_split_number=4)

geo.render()
