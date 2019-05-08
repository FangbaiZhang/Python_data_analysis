# -*- coding: cp936 -*-

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#figsize:��Ӣ��Ϊ��λ�Ŀ�ߣ�ȱʡֵΪ rc figure.figsize (1Ӣ�����2.54����)
fig=plt.figure(figsize=(16,12))
ax=Axes3D(fig)
#����X,Y��ֵ
#arange([start,] stop[, step,], dtype=None)����start��stopָ���ķ�Χ�Լ�step�趨�Ĳ���������һ�� ndarray**: dtype
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
#���øߵ�ֵ
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)
#��ͼ��rstride,cstride���ú��ݷ�����ܶȳ̶ȣ�������ɫ
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap="rainbow")
#����ͶӰ�ȸ���ͼ��zdir�����ĸ�����Ͷ������ͶӰλ���Ƕ��٣�ͶӰ��ɫ��ʲô
ax.contourf(X,Y,Z,zdir='z',offset=1,cmap="rainbow")
ax.set_zlim=(-2,2)
plt.show()