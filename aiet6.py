import matplotlib.pyplot as plt

activity=['eat','sleep','work','play']

slices=[3,7,8,6]

color=['r','m','g','b']

plt.pie(slices,labels=activity,colors=color,startangle=90,shadow=True,explode=(0.5,0.5,1.0,0),autopct='%1.2f%%')
plt.legend()
plt.show()
