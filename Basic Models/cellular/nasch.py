# -*- coding: utf-8 -*-

from matplotlib.font_manager import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

matplotlib.rcParams['axes.unicode_minus'] = False
np.random.seed(0)
fig = plt.figure(figsize=(6, 6), facecolor='white')
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
path=2000#path为道路长度
n=20#n为车辆数目
v0=60
ltv=120
p=0.3#p是慢化概率
times=3000#迭代时间
x = np.random.rand(n) * path
x.sort()
v = np.ones(n) * v0
size=np.ones(100)*100
y=np.random.random([len(x),1])[:,0]*100
tmp=np.zeros([len(x),2])
tmp[:,0]=x
tmp[:,1]=y
scat = ax.scatter(tmp[:,0],tmp[:,1] , s=size)
def update(i):

    # x保存每辆车在道路上的位置，随机初始化
    global path, n, v0, ltv, p, times, x, v,size
    # 模拟每辆车
    for i in range(n):
            # 计算当前车与前车的距离，周期型边界
        if x[(i + 1) % n] > x[i]:
            d = x[(i + 1) % n] - x[i]
        else:
            d = path - x[i] + x[(i + 1) % n]
            # 根据距离计算下一秒的速度
        if v[i] < d:
            if np.random.rand() > p:
                v[i] += 1
            else:
                v[i] -= 1
        else:
            v[i] = d - 1
        # 对速度进行控制
    v = v.clip(0, ltv)

    # 位置更新
    x += v
    x = x % path
    l=x.reshape(len(x),1)
    tmp=np.zeros([len(x),2])
    tmp[:,0]=x
    tmp[:,1]=0
    scat.set_offsets(tmp)
    scat.set_sizes(size)
    return scat,

ani = animation.FuncAnimation(fig, update, interval=100, blit=True)
plt.show()
