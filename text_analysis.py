# Импортирую библиотеку для получения аргументов из командной строки
import argparse
# Импортирую библиотеку для использования черпахи и создания визуального экрана
import turtle
# Импортирую библиотеку регулярных вырожений, для получения отдельных слов
import re
import random
#from itertools import cycle

r = 120

def get_arguments():
    """изъятие данных"""
    parser = argparse.ArgumentParser(
    description='Получаем вариант диаграммы, текст для диаграммы, цвета.',
    epilog='type=column or circle, text=любой текс,colors=red,blue,gren,yellow'
    )
    parser.add_argument(
    '--type', dest='type_d', help='Введите тип диаграммы столцы и круговые '
    )
    parser.add_argument(
    '--string',
    dest="str1", nargs='+', help='Строка для проверки значений '
    )
    return parser.parse_args()

def legend_draw(y,key,val):
    """Рисуем легенду

    Значение аргументов
    y    -- значение y по оси координат
    key  -- ключ в словаре
    val  -- значение ключа

    """
    turtle.penup()
    b = turtle.heading()
    s = turtle.pos()
    turtle.goto(300, y)
    turtle.write((str(key) + " - " + str(val)), align="left",font=("Ariel",19,"bold"))
    turtle.setposition(s)
    turtle.setheading(b)
    turtle.pendown()

def draw_diagram(rad, my_dict_too, len_word, my_dict_items):
    """Рисуем диаграму 

    Значение аргументов
    red         -- радиус для построения круга
    my_dict_too -- словарь, в котором ключ - слово из текста , значение - кол-во повторов этого слова в тексте
    sektor      -- Размер одного сектора

    """
    # Определяем размер сектора
    sektor = 360 / len(len_word)
    turtle.circle(rad)
    midl = (0,120)
    ty =200
    for i,y in my_dict_items.items():
        turtle.colormode(255)
        turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        legend_draw(ty,i,y)        
        turtle.begin_fill()
        turtle.circle(rad,my_dict_too[i]*sektor)
        b = turtle.heading()
        s = turtle.pos()
        turtle.lt(90)
        turtle.forward(rad)
        turtle.goto(midl)
        turtle.home()
        turtle.goto(midl)
        turtle.end_fill()
        turtle.penup()
        turtle.setposition(s)
        turtle.setheading(b)
        ty -=30

def draw_axis():
    """Рисуем ось координат"""
    turtle.lt(90)
    turtle.goto(0,300)
    turtle.stamp()
    turtle.write("Y", align="right",font=("Ariel",19,"bold"))
    turtle.rt(90)
    turtle.home()
    turtle.goto(300,0)
    turtle.write("X", align="center",font=("Ariel",19,"bold"))    
    turtle.stamp()
    turtle.lt(90)
    turtle.home

def draw_axis_fill(my_dict_for_axis,word_):
    """Заполняем значение на оси координат

    Значение аргументов
    my_dict_too   -- словарь
    word_         -- количество слов в словаре 
    """
    turtle.penup()
    x = 15
    one_sector = 20 / len(word_)
    turtle.goto(x,5)
    y_there_drow =300
    for key,value in my_dict_for_axis.items():
        turtle.pensize(10)
        turtle.pendown()
        turtle.colormode(255)
        turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        legend_draw(y_there_drow,key, value)
        turtle.forward(value*15)        
        turtle.penup()
        x+=15
        turtle.goto(x,5)
        ty-=30

def main():

    args = get_arguments()
    words = ""
    tes = set()
    # Создаем объект черепаха
    turtle1 = turtle.Turtle()    
    # Цикл для передачи значений из list в строку
    for i in args.str1:
        words += (i + " ").lower()
    # Работаем со строкой ,Получаем список слов без знаков припенания
    word = re.findall(r'\w+', words)
    # Создаем словарь и вносим кол-во входов в значение ключей
    # Список наполняем в случае нахождения новых аргументов 
    my_dict = {}
    for er in re.findall(r'\w+', words):
        if er in tes:
            my_dict[er] += 1
        else:
            my_dict[er] = 1
            tes.add(er)

    if args.type_d == "d":
        draw_diagram(r, my_dict, word, my_dict)
    else:
        draw_axis()
        draw_axis_fill(my_dict,word)

    turtle.done()


if __name__ == '__main__':
    main()