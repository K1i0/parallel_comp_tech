import matplotlib.pyplot as plt
import numpy as np

ax = plt.gca()

#Titles
plt.title("Передача сообщений на различных уровнях коммуникационной среды")
plt.xlabel("Размер сообщения, MB", fontsize=12)
plt.ylabel("Среднее время передачи сообщения, с", fontsize=12)

#Data to plot
x = np.array(["2", "4", "8", "16", "32", "64"])

y = np.array([0.0000412563, 0.0001459172, 0.0002609572, 0.0006084881, 0.0011748465, 0.0024209911])
y2 = np.array([0.0000502218, 0.0001486962, 0.0002706839, 0.0005952951, 0.0011555086, 0.0024129899])
y3 = np.array([0.0001217021, 0.0002632520, 0.0003907947, 0.0007432661, 0.0013322021, 0.0027103880])

plt.plot(x, y,linestyle='-', marker='o', color="#228B22", alpha = 0.80, label='Уровень оперативной памяти')
plt.plot(x, y2,linestyle='-', marker='o', color="#6A5ACD", alpha = 0.70, label='Межпроцессорный уровень')
plt.plot(x, y3,linestyle='-', marker='o', color="#FA8072", alpha = 0.70, label='Сетевой увроень')

plt.ylim(0, 0.0027) #Пределы отображения на оси y
ax.grid(axis = 'both') #Сетка для обеих осей
ax.set_xticks(x)
plt.legend()
plt.show()