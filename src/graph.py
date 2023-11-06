import matplotlib.pyplot as plt
import numpy as np

ax = plt.gca()

#Titles
plt.title("Передача сообщений на различных уровнях коммуникационной среды")
plt.xlabel("Размер сообщения, MB", fontsize=12)
plt.ylabel("Среднее время передачи сообщения, с", fontsize=12)

#Data to plot
x = np.array(["2", "4", "8", "16", "32", "64"])

y = np.array([0.0000498756, 0.0001505816, 0.0002973489, 0.0005997650, 0.0011810359, 0.0024281442])
y2 = np.array([0.0000813688, 0.0001380975, 0.0002983796, 0.0005857213, 0.0011547149, 0.0023957227])
y3 = np.array([0.0001815466, 0.0002174860, 0.0004350159, 0.0007529949, 0.0013160692, 0.0026938401])

plt.plot(x, y,linestyle='-', marker='o', color="#228B22", alpha = 0.80, label='Уровень оперативной памяти')
plt.plot(x, y2,linestyle='-', marker='o', color="#6A5ACD", alpha = 0.70, label='Межпроцессорный уровень')
plt.plot(x, y3,linestyle='-', marker='o', color="#FA8072", alpha = 0.70, label='Сетевой увроень')

plt.ylim(0, 0.0027) #Пределы отображения на оси y
ax.grid(axis = 'both') #Сетка для обеих осей
ax.set_xticks(x)
plt.legend()
plt.show()