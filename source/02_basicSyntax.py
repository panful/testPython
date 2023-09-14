# '#'开头的单行是注释

"""
三个引号包围的都是注释
"""

#-------------------------------------------------
# 判断语句
if 1:
 print("1")
if True:
 print("True")

#-------------------------------------------------
# 定义数字
myInt = 666
myFloat = 666.0

print(myInt)
print(myFloat)

#-------------------------------------------------
# 定义字符串
word = 'word'
sentence = "这是一个句子"
paragraph = """这是一个段落，
第二条语句"""

print(word)
print(sentence)
print(paragraph)

#-------------------------------------------------
# 字符串操作，字符串索引从0开始
word1_3 = word[1:3]                 # 第1个和第2个字符
print(word1_3)

word2 = word[2]                     # 第2个字符
print(word2)

word_2 = word[-3]                   # 负号表示反向操作，正向操作的第0个元素和反向操作的-N相同，N表示字符串长度
print(word_2)

string_add = sentence + paragraph   # 字符串相加
print(string_add)

string_multi = sentence * 3         # 字符串重复操作，3表示次数
print(string_multi)

#-------------------------------------------------
# 列表
myListStr = ['abc', 'def', 'ghi', 'opq', 'xyz']
myListInt = [111, 222, 333, 444]

print(myListStr)                # 打印整个列表
print(myListStr[1])             # 打印列表的第1个元素
print(myListStr[1:3])           # 打印列表的第1个和第2个元素
print(myListInt + myListStr)    # 打印两个列表的和

myListInt[1] = 666              # 修改列表的元素
print(myListInt)

#-------------------------------------------------
# 元组，类似列表，但是不能修改元组的值
myTuple = ('abc', 'xyz', '123', '789')

print(myTuple)  # 打印整个元组

#-------------------------------------------------
# 字典
myDict1 = {}            # 构造一个字典，稍后赋值
myDict1[111] ='111'
myDict1['xyz'] = 'xyz'
myDict1[22.2] = 22.2

print(myDict1[22.2])    # 打印键值为22.2的值
myDict1[22.2] = '3333'  # 修改键值为22.2对应的值
print(myDict1[22.2])

myDict2 = {'a':'aaa', 'b':'bbb', 'c':'ccc'} # 构造一个字典并赋值
print(myDict2['a'])

#-------------------------------------------------
# 数据类型转换
strInt = '123'
str2Int = int(strInt)   # 字符串转换为int，如果字符串含有非数字则编译报错
strHex = hex(str2Int)   # int转换为16进制字符串
int2Str = str(str2Int)  # int转换为字符串

print(strInt)
print(str2Int)
print(strHex)
print(int2Str)
