from example.commons import Faker

# 使用Faker,按住ctrl查看方法的源码
# choose: 从以下七个品类(每个品类有七样东西)中选择七样东西，clothes,drinks,phones,fruits,animal,dogs,week
# values：值取20-150的随机整数

x_data = Faker.choose()
y_data = Faker.values()
print(x_data)
print(y_data)

# 结果x是一个字符串组成的列表，结果y是整数组成的列表
# 每次运行会随机得到不同的结果

