size = 1000


import numpy.random as npr

rn1 = npr.rand(size,2)
rn2 = npr.randn(1000)
print rn2
rn3 = npr.randint(0,10,size)
rang = [0, 10, 20, 30, 40]
rn4 = npr.choice(rang, size=size)

import matplotlib.pyplot as plt

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2,figsize=(10,10))
ax1.hist(rn1,bins=25,stacked=True)
ax1.set_title('rand')
ax1.set_ylabel('frequency')
ax1.grid(True)
ax2.hist(rn2,bins=25)
ax2.set_title('randn')
ax2.grid(True)
ax3.hist(rn3,bins=25)
ax3.set_title('randint')
ax3.grid(True)
ax4.hist(rn4,bins=25)
ax4.set_title('choice')
ax4.grid(True)
plt.show()

