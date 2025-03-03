#gfhdthev
#лабораторная работа #1


#импортируем библиотеки
import math
import matplotlib.patches
import matplotlib.pyplot as plt


#создаем класс
class Oktagon:
    def __init__(self, a): #инициализация всех переменных
        self.k = (1+math.sqrt(2))
        self.corcer = 135
        self.a = a

    def plo(self): #находим площадь октагона
        self.square = 2*self.k*self.a**2
        print(f'Площадь октагона {self.square}')

    def per(self): #находим периметр октагона
        self.perim = 8*self.a
        print(f'Периметр октагона {self.perim}')

    def opis_okr(self): #находим радиум и площадь описанной окружности
        self.square = 2*self.k*self.a**2
        self.bol_r = math.sqrt(self.square/2/math.sqrt(2))
        self.bol_s = 3.14*self.bol_r**2
        print(f'Радиус описанной окружности {self.bol_r}')
        print(f'Площадь описанной окружности {self.bol_s}')

    def vpis_okr(self): #находим радиум и площадь описанной окружности
        self.square = 2*self.k*self.a**2
        self.mal_r = math.sqrt(self.square/8/(math.sqrt(2)-1))
        self.mal_s = 3.14*self.mal_r**2
        print(f'Радиус вписанной окружности {self.mal_r}')
        print(f'Площадь вписанной окружности {self.mal_s}')
    
    def ris(self): #выводим графики на экран
        self.square = 2*self.k*self.a**2
        self.mal_r = math.sqrt(self.square/8/(math.sqrt(2)-1))
        self.bol_r = math.sqrt(self.square/2/math.sqrt(2))

        plt.xlim(-20, 20)
        plt.ylim(-20, 20)
        plt.grid()
        axes = plt.gca()

        polygon_1 = matplotlib.patches.Polygon([(self.mal_r, self.a/2),  #создаем октагон
                                                (self.mal_r, -self.a/2),
                                                (self.a/2, -self.mal_r),
                                                (-self.a/2, -self.mal_r),
                                                (-self.mal_r, -self.a/2),
                                                (-self.mal_r, self.a/2), 
                                                (-self.a/2, self.mal_r), 
                                                (self.a/2, self.mal_r)], 
                                                fill = False, color = 'green')

        circle1 = matplotlib.patches.Circle((0, 0), radius=self.bol_r, fill = False, color = 'red')  #описанная окружность
        circle2 = matplotlib.patches.Circle((0, 0), radius=self.mal_r, fill = False, color = 'black') #вписанная окружность
        axes.add_patch(circle1)
        axes.add_patch(circle2)
        axes.add_patch(polygon_1)
        plt.show()

    def __del__(self): #деинициализация
        print('Октагон удален')