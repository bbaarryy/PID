from PID import PID
from DynamicModel import MassSpringDamper
import matplotlib.pyplot as plt
import numpy as np

#Подготовка к началу действия регулятора

#предельно маленькое время для отслеживания изменений системы
micro_time = 0.01

#создание PID-регулятора(вытаскиваем из класса)
reg = PID(15, 3, 0.01, micro_time, -10, 10)

#создание физической модели(вытаскиваем из класса)
model = MassSpringDamper(1, 1, 1, micro_time=micro_time)

T = 20#до какого момента времени мы будем всё исполнять
t = np.arange(0, T, micro_time)#создание массива с временными остановками
F = 0#изначально сила  - 0

need = 10#нужое число , к которому мы стремимся (в данном случае 10)
x_des = need * np.ones(len(t))

model_x = []#массив с изменениями координаты

P_hist, D_hist, I_hist,F_arr = [], [], [],[]#история изменения частей P ,I ,D PID-регулятора а также силы

#начало процесса
for i in range(len(t)):
    model_x.append(model.update(F))#добавление координаты
    F = -reg.update(model_x[-1], x_des[i])#изменение силы при помощи PID-регулятора
    F_arr.append(F)#добавление к истории сил
    #также и самих частей регулятора(для наглядности)
    P_hist.append(reg.proportionality)
    D_hist.append(reg.diff)
    I_hist.append(reg.integral)
#Строим графики!!!
fig, (ax1, ax2,ax3) = plt.subplots(ncols=3, figsize=[10, 13])#
ax1.plot(t, model_x, label="real x")
ax1.plot(t, x_des, label="x desired")
ax1.grid()
ax3.plot(t, F_arr, label="F")
ax3.grid()
ax2.plot(t, P_hist, label="P")
ax2.plot(t, D_hist, label="D")
ax2.plot(t, I_hist, label="I")
ax2.grid()
#добавление легенд
ax1.legend()
ax1.plot()
ax2.legend()
ax2.plot()
ax3.legend()
ax3.plot()
#показ графиков
plt.show()
