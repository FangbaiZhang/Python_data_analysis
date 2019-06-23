# 参考博文：
# matplotlib命令与格式：标题(title)，标注(annotate)，文字说明(text)
# https://blog.csdn.net/u011318077/article/details/93173473

import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
t = "This is a really long string"

plt.text(4, 1, t, ha='left', rotation=15, wrap=True)

plt.text(6, 5, t, ha='left', rotation=15, wrap=True)

plt.text(5, 5, t, ha='right', rotation=-15, wrap=True)

plt.text(5, 10, t, fontsize=18, style='oblique', ha='center', va='top', wrap=True)

plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)

plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)

plt.show()