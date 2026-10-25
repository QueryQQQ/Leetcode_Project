# 本代码主要提供了1.字符串读取每个字符方法 2.字典方法判断赋值字符串 3.字符串切片方法读取多个字符
s = input("请输入一串罗马字符，范围0-3500")
# 将多字符判断浓缩进表里，前面判断了，后面就加上差值即可
d = {
    'I': 1,
    'IV': 3,
    'V': 5,
    'IX': 8,
    'X': 10,
    'XL': 30,
    'L': 50,
    'XC': 80,
    'C': 100,
    'CD': 300,
    'D': 500,
    'CM': 800,
    'M': 1000,
}
count = 0
current_num = 0
for i in range(len(s)):
    current_num += d[s[i]]# 字典按键取值
    pointer = s[max(i,0):i+2]# 这一行规定切片开始和结束位置，使用max是不让i-1跳出0的范围
    # 还要规定查询不到的情况,查的到就有组合值pointer查不到就用current_num
    # get(key,default)函数可以通过key从d中找到对应值，如key不存在返回default
    count += d.get(pointer,current_num)
print(count)