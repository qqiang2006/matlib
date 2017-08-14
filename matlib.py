#coding=utf8
from matplotlib.font_manager import FontManager, FontProperties
import subprocess
import matplotlib.pyplot as plot
import matplotlib
import  sqlite3
import  time,sys
reload(sys)
#sys.setdefaultencoding('utf8')
#datatime=('January','February','March','April','May','June','July','August','September','October','November','December')
all_area=('海淀','昌平','大兴','东城','朝阳','顺义','西城','丰台','房山','门头沟','平谷','怀柔','延庆','密云','燕郊')
matalib_list=[[4.13, 6.13,7.13,8.13]]
datatime=('Apr','Jul','Jun','Aug')
#操作数据库
area=[]
for j in all_area:
    area_num_data = []
    for i in datatime:
        database_name="ershoufang"+'_'+i+'_13_2017'
        data_base_ershoufang = sqlite3.connect('D:\Python scripts\matlib\%s.db'%database_name)
        cu=data_base_ershoufang.cursor()
        cu.execute('select num from house_num where area_name="%s"'%j)
        #[(u'\u6000\u67d4', 1), (u'\u4e1c\u57ce', 867)]
        #print cu.fetchall()[0][0]
        area_num_data.append(cu.fetchall()[0][0])
    matalib_list.append(area_num_data)
    area.append(j)
# print matalib_list
#print type(area[0])
font = {'family' : 'DFKai-SB',
        'weight' : 'bold'}
plot.rc('font', **font)  # pass in the font dict as kwargs
plot.rc('axes',unicode_minus=False)
plot.ylabel('num')
plot.xlabel("data")
i=0
while i <len(matalib_list)-1:
    plot.plot(matalib_list[0], matalib_list[i+1],label='rf')
    plot.legend()
    i+=1
plot.title('number')
plot.show()
