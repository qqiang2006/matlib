#coding=utf8
from matplotlib.font_manager import FontManager, FontProperties
import subprocess
import matplotlib.pyplot as plot
import  sqlite3
import  time
#datatime=('January','February','March','April','May','June','July','August','September','October','November','December')
datatime=('Jul','Aug')
#操作数据库
for i in datatime:
    database_name="ershoufang"+'_'+i+'_13_2017'
    data_base_ershoufang = sqlite3.connect('/Users/lihuixian/PycharmProjects/lianjia/%s.db'%database_name)
    cu=data_base_ershoufang.cursor()
    cu.execute('select * from house_num')
    #[(u'\u6000\u67d4', 1), (u'\u4e1c\u57ce', 867)]
    print cu.fetchall()

def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

if __name__ == '__main__':
    list1 = [[4.13,5.13,6.13,7.13,8.13,9.13,10.13],[130,3234,345,332,556,34,66],[13,324,345,33,556,34,66]]
    plot.ylabel('num')
    plot.xlabel("data")
    i=0
    while i <2:
        plot.plot(list1[0], list1[i+1])
        i+=1
    plot.title('二手房房源数量', fontproperties=getChineseFont())
    plot.show()
