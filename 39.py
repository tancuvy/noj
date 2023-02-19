# 使用Lambda 函数 自定义规则
# eval(expression)，expression：字符串表达式，可为算法，也可为input函数等。作用：接收运行一个字符串表达式，返回表达式的结果值。
res = lambda s:eval(s.replace("/","//")) # replace (old,new) 用新的代替老的 整除代替除  
print(res(input()))