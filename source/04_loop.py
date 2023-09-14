#---------------------------------------------
# while循环
nums = [1, 2, 3, 4, 5]
while len(nums) > 0:
    num = nums.pop() # 将列表的最后一个元素弹出
    if(num % 2 == 0):
        print(num, " is even")
    else:
        print(num, " is odd")

#---------------------------------------------
# while使用else
count = 0
while count < 5:
    print(count, "is less than 5")
    count += 1
else:
    print(count, "is not less than 5")

#---------------------------------------------
# for循环遍历列表（字符串）
myStr = "hello world"
for word in myStr:
    print(word)

#---------------------------------------------
# for通过序列索引迭代
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('current fruit: %s', fruits[index])

for index in range(5):
    print('%d is current number'% index) # 注意连接字符串需要使用'%'，而不是','

#---------------------------------------------
# for循环迭代区间，包含前面的5，不包含后面的9
for num in range(5, 9):
    print(num)

#---------------------------------------------
# for循环使用else
for num in range(10):
    if num % 2 == 0:
        print("%d is even"% num)
else: # for循环执行完会执行else
    print("for loop is end")