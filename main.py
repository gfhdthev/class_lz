from oktagon import Oktagon #импортируем класс

def main(): #создаем функцию 
    first = Oktagon(8) #добавляем объект
    first.plo() #используем все методы
    first.per()
    first.opis_okr()
    first.vpis_okr()
    first.ris()

if __name__ == '__main__': #проверяем на прямой запуск
    main() #запускаем функцию