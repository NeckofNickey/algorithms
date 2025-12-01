from turtle import *
tracer(0) # отключаем анимацию
m = 50 # масштаб
screensize(2000, 2000) # размер экрана

# базовый поворот, чтобы черепашка была повернута вдоль оси y
left(90)

# алгоритм из задания для движения черепахи
for _ in range(7):
    forward(10 * m)
    right(120)

# расставляем точки
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*m, y*m)
        dot(5, 'red')

done()



