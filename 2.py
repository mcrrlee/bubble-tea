import matplotlib.pyplot as plt
x = np.arange(1,12)
y = [22,20,14,12,11,6,5,4,3,2,1]
mueang = ['KOI Thé','Ochaya','Mikucha','Mr. Shake','Kamu','Coco','ATM','The alley','Dakashi','Moma’s','CHA BAR']
ax = plt.gca(xticks=x) 
ax.set_xticklabels(mueang,rotation=10) 
plt.bar(x,y)
plt.show()