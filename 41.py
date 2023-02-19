x1,y1,x2,y2 = input().split(" ")
x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)

x1,x2 = min(x1,x2),max(x1,x2)
y1,y2 = min(y1,y2),max(y1,y2)#变成左下角和右上角的坐标

x3, y3, x4, y4 = input().split(" ")
x3, y3, x4, y4 = int(x3),int(y3),int(x4),int(y4)

x3,x4 = min(x3,x4),max(x3,x4)
y3,y4 = min(y3,y4),max(y3,y4)#变成左下角和右上角的坐标

#计算重叠部分
if (x2<=x3 or x4<=x1) and (y2<=y3 or y4<=y1):
    print(0)#不重叠
else:
    length = min(x2,x4)-max(x1,x3)
    width = min(y2,y4)-max(y1,y3)
    print(length*width)