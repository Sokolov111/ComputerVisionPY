import cv2

#  Путь к фото
imgDir = "./dir/person4.jpeg"

# загрузить фото
imgLoad = cv2.imread(imgDir)

# Изменить размер фото
width = 550
f = float(width) / imgLoad.shape[1]
imgSize =  (width, int(imgLoad.shape[0] * f))
res = cv2.resize(imgLoad, imgSize, interpolation = cv2.INTER_AREA)

# Ообразить фото в окне
# cv2.imshow("Show Img" , res)

# Вырезать фрагмент изображения
crop = res[420:550, 150:280]
# cv2.imshow("Crop Img" , crop)

# Сохранить вырезанный фрагмент
# cv2.imwrite("cropImg.png", crop)


# Черно - белый фильтр
# задаем границы диапазона:
# нижнюю
# low_color = (0,0,150)
# low_color = (25,100,175)
# и верхнюю 56 страница
# high_color = (255,255,255)
# high_color = (35,255,255)
# only_object = cv2.inRange(res, low_color,
#  high_color)

# вывод отфильтрованного изображения на экран
# cv2.imshow('only object', only_object)


# Найти изображение по маске
hsv_img = cv2.cvtColor(imgLoad, cv2.COLOR_BGR2HSV)


import cv2
# связываем видеопоток камеры с переменной capImg
capImg = cv2.VideoCapture(0)

while(True):
    # получаем кадр из видеопотока,
    # кадры по очереди считываются в переменную frame
    ret, frame = capImg.read()
    # показываем кадр в окне ’Video’
    #
    # организуем выход из цикла по нажатию клавиши,
    # ждем 30 миллисекунд нажатие, записываем код
    # нажатой клавиши
    #
    # нижняя граница - это темный ненасыщенный цвет
    color_low = (0,0,150)
    # верхняя граница - это яркий насыщенный цвет
    color_high = (255,255,255)
    # наложение цветовой маски на HSV-изображение,
    # результат присваиваем переменной only_object
    only_object = cv2.inRange(frame, color_low,color_high)

    # вычисляем моменты отфильтрованного HSV-изображения
    moments = cv2.moments(only_object, 1)
    # вычисляем сумму x-координат всех точек пятна
    x_moment = moments['m01']
    # вычисляем сумму y-координат всех точек пятна
    y_moment = moments['m10']
    # вычисляем общее число всех точек пятна
    area = moments['m00']
    # вычисляем среднее значение координаты x объекта
    if area != 0:
        x = int(x_moment / area)
        y = int(y_moment / area)
    else:
        # Обработка случая, когда площадь равна нулю (например, можно установить x в 0 или какое-то другое значение)
        x = 0
        y = 0

    # x = float(x_moment / area)
    # вычисляем среднее значение координаты y объекта

    # выводим надпись на изображение
    cv2.putText(frame, "Target", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2,cv2.LINE_AA , False)
    # выводим координаты объекта
    cv2.putText(frame, "%d, %d" % (x,y), (x,y+30),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    # выводим картинку в окне found
    cv2.imshow('found', frame)

    # cv2.imshow('Video', frame)

    key_press = cv2.waitKey(30)
    # если код нажатой клавиши совпадает с кодом
    # «q»(quit - выход),
    if key_press == ord('q'):
        # то прервать цикл while
        break
# освобождаем память от переменной capImg
capImg.release()
# закрываем все окна opencv
cv2.destroyAllWindows()

# не закрывать окно
cv2.waitKey(0)


