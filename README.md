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

