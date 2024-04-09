import sys

from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QInputDialog

from src.project import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        # загрузка интерфейса

        self.setupUi(self)

        # сделаем кнопки кликабельными

        self.pushButton.clicked.connect(self.rotate)
        self.pushButton_2.clicked.connect(self.change_light)
        self.pushButton_3.clicked.connect(self.change_color)
        self.pushButton_4.clicked.connect(self.black_white)
        self.pushButton_5.clicked.connect(self.frame)
        self.pushButton_6.clicked.connect(self.load)
        self.pushButton_7.clicked.connect(self.saveas)
        self.fname = ""
        self.pixmap = ""

    def super_red(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def super_green(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def super_blue(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def return_light(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open(self.fname)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def rotate_90_right(self):

        # загружаем картинку и поворачиваем ее

        im = Image.open("assets/new.jpg")
        im2 = im.transpose(Image.ROTATE_90)

        # cохраняем новую картинку

        im2.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def rotate_90_left(self):

        # загружаем картинку и поворачиваем ее

        im = Image.open("assets/new.jpg")
        im2 = im.transpose(Image.ROTATE_270)

        # cохраняем новую картинку

        im2.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def negative(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 255 - r, 255 - g, 255 - b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def lightning_50(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r + r // 2, g + g // 2, b + b // 2

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def darkening_50(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r - r // 2, g - g // 2, b - b // 2

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def violet(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r + r // 2, g, b + b // 2

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def light_blue(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g + g // 2, b + b // 2

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def yellow(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r + r // 2, g + g // 2, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def negative1(self):

        # даем выбор какую картинку сделать чёрно-белой и изменяем в ней пиксели

        photo, ok_pressed = QInputDialog.getItem(
            self, "Выберите какую картинку сделать чёрно-белой", "Какую картинку сделать чёрно-белой?",
            ("от изначальной картинки", "от новой картинки"), 0, False)
        if ok_pressed:
            if photo == "от изначальной картинки":
                im = Image.open(self.fname)
            else:
                im = Image.open("assets/new.jpg")
        else:
            im = Image.open(self.fname)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                sr = (r + b + g) // 3
                pixels[i, j] = sr, sr, sr

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def negative2(self):

        # даем выбор какую картинку сделать чёрно-белой и изменяем в ней пиксели

        photo, ok_pressed = QInputDialog.getItem(
            self, "Выберите какую картинку сделать чёрно-белой", "Какую картинку сделать чёрно-белой?",
            ("от изначальной картинки", "от новой картинки"), 0, False)
        if ok_pressed:
            if photo == "от изначальной картинки":
                im = Image.open(self.fname)
            else:
                im = Image.open("assets/new.jpg")
        else:
            im = Image.open(self.fname)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, r, r
        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def negative3(self):

        # даем выбор какую картинку сделать чёрно-белой и изменяем в ней пиксели

        photo, ok_pressed = QInputDialog.getItem(
            self, "Выберите какую картинку сделать чёрно-белой", "Какую картинку сделать чёрно-белой?",
            ("от изначальной картинки", "от новой картинки"), 0, False)
        if ok_pressed:
            if photo == "от изначальной картинки":
                im = Image.open(self.fname)
            else:
                im = Image.open("assets/new.jpg")
        else:
            im = Image.open(self.fname)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = g, g, g

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def negative4(self):

        # даем выбор какую картинку сделать чёрно-белой и изменяем в ней пиксели

        photo, ok_pressed = QInputDialog.getItem(
            self, "Выберите какую картинку сделать чёрно-белой", "Какую картинку сделать чёрно-белой?",
            ("от изначальной картинки", "от новой картинки"), 0, False)
        if ok_pressed:
            if photo == "от изначальной картинки":
                im = Image.open(self.fname)
            else:
                im = Image.open("assets/new.jpg")
        else:
            im = Image.open(self.fname)
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = b, b, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def frame_black(self, k=20):

        # загружаем картинку и создаем на ней рамку

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if i < k or j < k or i > x - k or j > y - k:
                    pixels[i, j] = 0, 0, 0
                else:
                    pixels[i, j] = r, g, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def frame_white(self, k=20):

        # загружаем картинку и создаем на ней рамку

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if i < k or j < k or i > x - k or j > y - k:
                    pixels[i, j] = 255, 255, 255
                else:
                    pixels[i, j] = r, g, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def frame_gradient(self, k=20):

        # загружаем картинку и создаем на ней рамку

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if i < k or j < k or i > x - k or j > y - k:
                    if i < k // 5 or j < k // 5 or i > x - k // 5 or j > y - k // 5:
                        pixels[i, j] = r - r // 4 * 3, g - g // 4 * 3, b - b // 4 * 3
                    elif i < k // 5 * 2 or j < k // 5 * 2 or i > x - k // 5 * 2 or j > y - k // 5 * 2:
                        pixels[i, j] = r - r // 3 * 2, g - g // 3 * 2, b - b // 3 * 2
                    elif i < k // 5 * 3 or j < k // 5 * 3 or i > x - k // 5 * 3 or j > y - k // 5 * 3:
                        pixels[i, j] = r - r // 2, g - g // 2, b - b // 2
                    elif i < k // 5 * 4 or j < k // 5 * 4 or i > x - k // 5 * 4 or j > y - k // 5 * 4:
                        pixels[i, j] = r - r // 3, g - g // 3, b - b // 3
                    else:
                        pixels[i, j] = r - r // 5, g - g // 5, b - b // 5
                else:
                    pixels[i, j] = r, g, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def rotate(self):

        # загружаем файл и берем из него названия для выбора поворота

        self.label_2.setText("")  # это нужно для стирания ошибки
        file = open("assets/rotation.txt", encoding="utf8")
        a, b, c = file.readlines()
        a, b, c = a[:-1], b[:-1], c

        # даем выбор поворота

        pov, ok_pressed = QInputDialog.getItem(
            self, "Выберите поворот", "Какой сделать поворот?",
            (a, b, c), 0, False)
        file.close()
        try:
            if ok_pressed:
                if pov == a:
                    self.rotate_90_right()
                elif pov == b:
                    self.rotate_90_left()
                else:
                    self.rotate_180()
            else:
                raise Exception
        except Exception:

            # если неправильно ввели выводим ошибку

            self.label_2.setText("Неправильный ввод. Попробуйте еще раз.")

    def rotate_180(self):

        # загружаем картинку и поворачиваем ее

        im = Image.open("assets/new.jpg")
        im2 = im.transpose(Image.ROTATE_180)

        # cохраняем новую картинку

        im2.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def change_light(self):

        # загружаем файл и берем из него названия для выбора освещенности

        self.label_2.setText("")  # это нужно для стирания ошибки
        file = open("assets/light.txt", encoding="utf8")
        a, b, c, d, e = file.readlines()
        a, b, c, d, e = a[:-1], b[:-1], c[:-1], d[:-1], e

        # даем выбор освещенности

        svet, ok_pressed = QInputDialog.getItem(
            self, "Выберите свет", "Какой сделать свет?",
            (a, b, c, d, e), 0, False)
        file.close()
        try:
            if ok_pressed:
                if svet == a:
                    self.lightning_50()
                elif svet == b:
                    self.darkening_50()
                elif svet == c:
                    self.negative()
                elif svet == d:
                    self.return_light()
                else:

                    # если выбрали с коэффициентом, то запрашиваем коэффициент

                    kof, ok_pressed2 = QInputDialog.getInt(
                        self, "Введите коэффициент", "Какой коэффициент?",
                        20, - 255, 255, 1)
                    if ok_pressed2:
                        self.light_with_coeff(kof)
                    else:
                        raise Exception
            else:
                raise Exception

            # если неправильно ввели выводим ошибку

        except Exception:
            self.label_2.setText("Неправильный ввод. Попробуйте еще раз.")

    def change_color(self):

        # загружаем файл и берем из него названия для выбора цвета

        self.label_2.setText("")  # это нужно для стирания ошибки
        file = open("assets/color.txt", encoding="utf8")
        a, b, c, d, e, f, g, h, i, j = file.readlines()
        a, b, c, d, e, f, g, h, i, j = a[:-1], b[:-1], c[:-1], d[:-1], e[:-1], f[:-1], g[:-1], h[:-1], i[:-1], j

        # даем выбор цвета

        tsvet, ok_pressed = QInputDialog.getItem(
            self, "Выберите свет", "Какой сделать свет?",
            (a, b, c, d, e, f, g, h, i, j), 0, False)
        file.close()
        try:
            if ok_pressed:
                if tsvet == a:
                    self.violet()
                elif tsvet == b:
                    self.light_blue()
                elif tsvet == c:
                    self.yellow()
                elif tsvet == d:
                    self.red()
                elif tsvet == e:
                    self.blue()
                elif tsvet == f:
                    self.green()
                elif tsvet == g:
                    self.super_red()
                elif tsvet == h:
                    self.super_blue()
                elif tsvet == i:
                    self.super_green()
                else:
                    self.return_light()
            else:
                raise Exception

        # если неправильно ввели выводим ошибку

        except Exception:
            self.label_2.setText("Неправильный ввод. Попробуйте еще раз.")

    def black_white(self):

        # загружаем файл и берем из него названия для выбора варианта чёрно-белого

        self.label_2.setText("")  # это нужно для стирания ошибки
        file = open("assets/blackwhite.txt", encoding="utf8")
        a, b, c, d = file.readlines()
        a, b, c, d = a[:-1], b[:-1], c[:-1], d

        # даем выбор варианта чёрно-белого

        bw, ok_pressed = QInputDialog.getItem(
            self, "Выберите один из вариантов чёрно-белого", "Какой сделать вариант чёрно-белого?",
            (a, b, c, d), 0, False)
        file.close()
        try:
            if ok_pressed:
                if bw == a:
                    self.negative4()
                elif bw == b:
                    self.negative3()
                elif bw == c:
                    self.negative1()
                else:
                    self.negative2()
            else:
                raise Exception

        # если неправильно ввели выводим ошибку

        except Exception:
            self.label_2.setText("Неправильный ввод. Попробуйте еще раз.")

    def frame(self):

        # загружаем файл и берем из него названия для выбора с коэффициентом или нет

        self.label_2.setText("")  # это нужно для стирания ошибки
        file = open("assets/frame1.txt", encoding="utf8")
        a, b = file.readlines()
        a, b = a[:-1], b

        # даем выбор с коэффициента или нет

        r1, ok_pressed = QInputDialog.getItem(
            self, "Выберите один из вариантов рамки", "Сделать с указанием коэффициента или нет?",
            (a, b), 0, False)
        try:
            if ok_pressed:

                # загружаем файл и берем из него названия для выбора цвета рамки

                file = open("assets/frame2.txt", encoding="utf8")
                a, b, c, d = file.readlines()
                a, b, c, d = a[:-1], b[:-1], c[:-1], d
                if r1 == "без указания коэффициента":

                    # даем выбор цвета рамки

                    r2, ok_pressed2 = QInputDialog.getItem(
                        self, "Выберите один из вариантов рамки", "Какую рамку вы хотите?",
                        (a, b, c, d), 0, False)
                    if ok_pressed2:
                        if r2 == a:
                            self.frame_black()
                        elif r2 == b:
                            self.frame_white()
                        elif r2 == d:
                            self.frame_gradient()
                        else:
                            self.frame_with_coeff()
                    else:
                        raise Exception
                else:

                    # загружаем файл и берем из него названия для выбора цвета рамки

                    file = open("assets/frame2.txt", encoding="utf8")
                    a, b, c, d = file.readlines()
                    a, b, c, d = a[:-1], b[:-1], c[:-1], d

                    # даем выбор цвета рамки

                    r2, ok_pressed2 = QInputDialog.getItem(
                        self, "Выберите один из вариантов рамки", "Какую рамку вы хотите?",
                        (a, b, c, d), 0, False)
                    if ok_pressed2:

                        # загружаем картинку и спрашиваем коэффициент

                        im = Image.open(self.fname)
                        x, y = im.size
                        kof, ok_pressed3 = QInputDialog.getInt(
                            self, "Введите коэффициент", "Какой коэффициент?",
                            20, 0, min(x, y), 1)
                        if ok_pressed3:
                            if r2 == "черную":
                                self.frame_black(kof)
                            elif r2 == "белую":
                                self.frame_white(kof)
                            elif r2 == d:
                                self.frame_gradient(kof)
                            else:
                                self.frame_with_coeff(kof)
                        else:
                            raise Exception
                    else:
                        raise Exception
            else:
                raise Exception

        # если неправильно ввели выводим ошибку

        except Exception:
            self.label_2.setText("Неправильный ввод. Попробуйте еще раз.")

    def red(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r + r // 2, g, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def green(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g + g // 2, b

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def blue(self):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b + b // 2

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def random(self, k=30):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        k = int(k)
        print(k)
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r - k, g - k, b - k

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def light_with_coeff(self, k):

        # загружаем картинку и изменяем в ней пиксели

        im = Image.open("assets/new.jpg")
        pixels = im.load()
        x, y = im.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r + k, g + k, b + k

        # cохраняем новую картинку

        im.save("assets/new.jpg")
        self.pixmap = QPixmap("assets/new.jpg")
        self.label.setPixmap(self.pixmap)

    def frame_with_coeff(self, k=20):

        # загружаем картинку и даем выбор коэффициента

        self.label_2.setText("")
        k1, ok_pressed = QInputDialog.getInt(
            self, "Введите количество красного", "Какое количество красного?",
            0, 0, 255, 1)
        k2, ok_pressed2 = QInputDialog.getInt(
            self, "Введите количество зеленого", "Какое количество зеленого?",
            0, 0, 255, 1)
        k3, ok_pressed3 = QInputDialog.getInt(
            self, "Введите количество синего", "Какое количество синего?",
            0, 0, 255, 1)
        try:
            if not ok_pressed:
                raise Exception
            if not ok_pressed2:
                raise Exception
            if not ok_pressed3:
                raise Exception

            # загружаем картинку

            im = Image.open("assets/new.jpg")
            pixels = im.load()
            x, y = im.size
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    if i < k or j < k or i > x - k or j > y - k:
                        pixels[i, j] = k1, k2, k3
                    else:
                        pixels[i, j] = r, g, b

            # cохраняем новую картинку

            im.save("assets/new.jpg")
            self.pixmap = QPixmap("assets/new.jpg")
            self.label.setPixmap(self.pixmap)

        # если неправильно ввели выводим ошибку

        except Exception:
            self.label_2.setText("Неправильный ввод. Попробуйте еще раз.")

    def saveas(self):
        self.label_2.setText("")
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Какое имя дать файлу?")
        name = name + ".jpg"
        try:
            if ok_pressed:
                im = Image.open("assets/new.jpg")
                im.save(name)
                im = Image.open("assets/new.jpg")
                pixels = im.load()
                x, y = im.size
                for i in range(x):
                    for j in range(y):
                        pixels[i, j] = 240, 240, 240
                im.save("assets/new.jpg")
                self.pixmap = QPixmap("assets/new.jpg")
                self.label.setPixmap(self.pixmap)
            else:
                raise Exception

        # если неправильно ввели выводим ошибку

        except Exception:
            self.label_2.setText("Неправильный ввод. Попробуйте еще раз.")

    def load(self):
        self.label_2.setText("")

        # создадим выбор картинки и вставим ее на экран
        try:
            self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            self.pixmap = QPixmap(self.fname)
            self.label.setPixmap(self.pixmap)
            im = Image.open(self.fname)

            # создаем новую картинку, в которую будем записывать итоговую картинку

            im.save("assets/new.jpg")
        except Exception:
            self.label_2.setText("Неправильный ввод. Попробуйте еще раз.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
