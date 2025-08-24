import matplotlib.pyplot as plt
x = ['party1','party2','party3']
y = [56,78,90]
plt.bar(x,y,width=0.1,color=['green','red','orange'])
plt.xlabel('Party')
plt.ylabel('Vote')
plt.title('Vote Graph')
plt.show()