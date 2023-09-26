import os

# 当前工作路径
currentWorkPath = os.getcwd()
print("current work path:\t", currentWorkPath)

# 源文件完整路径
currentFilePath = os.path.abspath(__file__)
print("current file path:\t", currentFilePath)

# 源文件所在目录
currentFileDir = os.path.dirname(currentFilePath)
print("current file dir:\t", currentFileDir)

# 文件名，包含完整路径，不包含后缀
file_name_path = os.path.splitext(currentFilePath)[0]
print("current file name and path:\t", file_name_path)

# 文件后缀
file_extension = os.path.splitext(currentFilePath)[1]
print("current file extension:\t\t", file_extension)

# 文件名，不包含路径，包含后缀
file_name_ext = os.path.basename(currentFilePath)
print("current file name and ext:\t", file_name_ext)

# 文件名，不包含路径，不包含后缀
file_name = os.path.splitext(os.path.basename(currentFilePath))[0]
print("current file name:\t\t", file_name)

#-------------------------------------------------------------------------
# 只读方式打开一个文件
fd = os.open(currentFilePath, os.O_RDONLY)
# 获取文件大小
file_size = os.fstat(fd).st_size
# 读取文件内容
file_contents = os.read(fd, file_size)
# 将字节数据转换为字符串
file_contents_str = file_contents.decode('utf-8')
# 关闭文件描述符
os.close(fd)
print("file size: %d\n%s" %(file_size, file_contents_str))