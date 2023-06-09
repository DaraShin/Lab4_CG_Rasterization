# Лабораторная 4. Базовые растровые алгоритмы
# Автор
Шинкевич Дарья, 13 группа, вариант 20
# Описание
Графическое приложение на python. 
Реализованы следующие алгоритмы растеризации прямой и окружности:
* пошаговый алгоритм;
* алгоритм ЦДА;
* алгоритм Брезенхема;
* алгоритм Брезенхема (окружность).
![image](https://user-images.githubusercontent.com/78850433/235091959-326af76a-1a45-45ba-b5f4-e4942a4d3097.png)


# Установка и запуск
```
  git clone git@github.com:DaraShin/Lab4_CG_Rasterization.git
  cd Lab4_CG_Rasterization/src/
  pip install pyinstaller
  pyinstaller --onefile -w main.py
  cd .\dist
  main.exe
```
# Docker
Ссылка на репозиторий DockerHub : https://hub.docker.com/r/dariashin/computer-graphics-lab4  
Для запуска контейнера использовать [docker-compose.yml](https://github.com/DaraShin/Lab4_CG_Rasterization/blob/master/docker-compose.yml)

# Временные харатеристики алгоритмов
Для прямой, заданной точками (0, 0) и (1000000, 1000000) получила время работы алгоритмов:  
Пошаговы алгоритм: 1.11 с  
Алгоритм ЦДА: 1.35 с  
Алгоритм Брезенхема: 0.92 с  
Время работы алгоритма Брезенхема для окружности радиуса 1000000 с центром в точке (0, 0): 4.38 с  

# Пример вычислений
Рассмотрим работу алгоритмов растеризации прямой на примере прямой x1=0, y1=0, x2=7, x3=4  
## Пошаговый алгоритм
Прямая будет задана уравнением y = kx + b, k = (4-0)/(7-0) = 4/7 = 0.5714, b = 0, y = 4x/7
Точки прямой, полученные алгоритмом:  
1. x = x1 = 0, y = y1 = 0  
2. x = 1, y = 1*4/7=0.57=1  
3. x = 2, y = 2*4/7=1.14=1  
4. x = 3, y = 3*4/7=1.71=2  
5. x = 4, y = 4*4/7=2.29=2  
6. x = 5, y = 5*4/7=2.86=3  
7. x = 6, y = 6*4/7=3.43=3  
8. x = 7, y = 7*4/7=4  

## Алгоритм ЦДА
Dx = 7-0 = 7, Dy = 4 - 0 = 4  
L = max {Dx, Dy} = 7  
Точки прямой, полученные алгоритмом:  
1. x = x1 = 0, y = y1 = 0  
2. x = x + Dx / L = 0 + 7 / 7 = 1, y = y + Dy / L = 0 + 4 / 7 = 0.57 = 1  
3. x = 1 + 7/7 = 2, y = 0.57 + 4/7 = 1.14=1  
3. x = 2 + 7/7 = 3, y = 1.14 + 4/7 = 1.71=2  
3. x = 3 + 7/7 = 4, y = 1.71 + 4/7 = 2.29=2  
3. x = 4 + 7/7 = 5, y = 2.29 + 4/7 = 2.86=3  
3. x = 5 + 7/7 = 6, y = 2.86 + 4/7 = 3.43=3  
3. x = 6 + 7/7 = 7, y = 3.43 + 4/7 = 4  
  
## Алгоритм Брезенхема
1. x = 0, y = 0  
   e = 4/7 - 0.5 = 0.0714 > 0  
2. x = 1, y = 1  
   e = e + 4/7 - 1 = -0.3571 < 0  
3. x = 2, y = 1  
   e = e + 4/7 = 0.2143 > 0  
4. x = 3, y = 2  
   e = e + 4/7 - 1 = -0.2143 < 0  
5. x = 4, y = 2  
   e = e + 4/7 = 0.3571 > 0  
6. x = 5, y = 3  
   e = e + 4/7 - 1 = -0.0714 < 0  
7. x = 6, y = 3  
   e = e + 4/7 = 0.5 > 0  
8. x = 7, y = 4  

## Алгоритм Брезенхема для окружности
Рассмотрим на примере окружности радиуса R = 5 с центром в точке (0,0):  
1. x = 0, y = R = 5, e = 3 - 2 * R = -7 < 0   
Добавляем точки (0,5), (0,-5), (5,0), (-5,0)  
2. e = e + 4x + 6 = -1 < 0, x = 1, y = 5  
Добавляем точки (1,5), (1,-5), (-1,5), (-1,-5), (5,1), (-5,1), (5,-1), (-5,-1)  
3. e = e + 4x + 6 = 9 > 0, x = 2, y = 5  
Добавляем точки (2,5), (-2,5), (2,-5), (-2,-4), (5,2),  (-5,2), (5,-2), (-5,-2) 
4. e = e + 4(x-y) + 10 = 7 > 0, x = 3, y = 4  
Добавляем точки (3,4), (-3,4), (3,-4), (-3,-4), (4,3),  (-4,2), (4,-3), (-4,-3) 

























