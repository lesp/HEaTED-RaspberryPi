import matplotlib.pyplot as plt
x = [10, 11, 12, 13]
y = [17.4, 6.2, 19.1, 22.9]
plt.plot(x,y, 'r', linewidth=6.0)
plt.axis([10,15,0,25])
plt.ylabel('Temperature in C')
plt.xlabel('Time in Hours')
file = open("data.txt","w")
for data in x:
    file.write(str(data))
    file.write(",")
file.write("\n")
for data in y:
    file.write(str(data))
    file.write(",")
file.close()
plt.show()
