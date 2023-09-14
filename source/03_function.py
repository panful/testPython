#-----------------------------------------------
# 定义一个函数
def MyPrint(str):
    print(str)
    return

# 调用一个函数
MyPrint("abc")

#-----------------------------------------------
def MyPrint2(name, age):
   "打印任何传入的字符串"
   print("Name:\t", name)
   print("Age:\t", age)
   return
 
#以任意顺序传递实参
MyPrint2(age = 50, name = "miki")

#-----------------------------------------------
# 函数参数的默认值
def MyPring3(arg = "default arg"):
    print(arg)

MyPring3("assign arg")  # 指定一个参数
MyPring3()              # 使用默认参数

#-----------------------------------------------
# 定义lambda
sum = lambda a, b : a + b

# 调用lambda
print("10 + 20 = ", sum(10, 20))