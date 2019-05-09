import numpy as np
from matplotlib import  pyplot as plt

# 创建文件路径
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
# 加载打开文件
t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

#选择喜欢书比50万小的数据
t_uk = t_uk[t_uk[:,1]<=10000]

t_uk_comment = t_uk[:,-1]
t_uk_like = t_uk[:,1]



plt.figure(figsize=(20,8),dpi=80)
plt.scatter(t_uk_like,t_uk_comment)
plt.title('Comments VS Likes')
plt.xlabel("Likes", fontsize=14)
plt.ylabel("Comments", fontsize=14)

plt.show()
