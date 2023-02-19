#计算相隔多少天
# datetime 库
import datetime as dt
one_list = [int(i) for i in input().split(" ")] #第一个时间
two_list = [int(i) for i in input().split(" ")] #第二个时间
one_time = dt.datetime(one_list[0],one_list[1],one_list[2]) #字符串变时间
two_time = dt.datetime(two_list[0],two_list[1],two_list[2])
print(one_time)
print((two_time-one_time).days)