from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import random

Window.clearcolor = (1.0, .9, .5, 1)

class MyApp(App):
    def build(self):

        box = BoxLayout(orientation ="vertical",
                        padding = 10,
                        spacing =10)

        label1 = Label(text ="Не знаешь чем заняться?\nВыбери любую категорию занятий и получишь совет!",
                       font_size = 50,
                       color ="blue",
                       halign="center")

        btn1 = Button(text ="Спорт",
                      background_color= [.52, .23, .12, 1],
                      background_normal=" ",
                      font_size = 50)

        btn1.bind(on_press = self.btn1_press)

        btn2 = Button(text="Книги",
                      background_color=[.52, .23, .88, 1],
                      background_normal=" ",
                      font_size=50)

        btn2.bind(on_press = self.btn2_press)


        btn3 = Button(text="Фильмы",
                      background_color=[.62, .63, .12, 1],
                      background_normal=" ",
                      font_size=50)

        btn3.bind(on_press = self.btn3_press)


        btn4 = Button(text="Страны",
                      background_color=[.122, .83, .82, 1],
                      background_normal=" ",
                      font_size=50)

        btn4.bind(on_press = self.btn4_press)


        btn5 = Button(text="Развлечения",
                      background_color=[1.0, .0, .0, 1],
                      background_normal=" ",
                      font_size=50)

        btn5.bind(on_press = self.btn5_press)


        btn6 = Button(text="Изучения",
                      background_color=[.213, .93, .33, 1],
                      background_normal=" ",
                      font_size=50)

        btn6.bind(on_press = self.btn6_press)


        box.add_widget(label1)
        box.add_widget(btn1)
        box.add_widget(btn2)
        box.add_widget(btn3)
        box.add_widget(btn4)
        box.add_widget(btn5)
        box.add_widget(btn6)

        return box

    def btn1_press(self, instence):
        sport = ["Сыграй в бадминтон", "Сыграй в баскетбол", "Сыграй в бейсбол", "Займись боксом",
                 "Сыграй в волейбол", "Займись плаванием", "Сыграй в теннис", "Сыграй в футбол",
                 "Займись фехтованием", "Займись дзюдо", "Займись греблей на байдарках и каноэ",
                 "Займись легкой атлетикой"]
        instence.text = random.choice(sport) + "\n(Спорт)"
        instence.halign = "center"
    def btn2_press(self, instence):
        books = ["Прочитай «Властелин колец» Джон Р. Р. Толкин", "Прочитай «Гордость и предубеждение» Джейн Остин",
                 "Прочитай «Тёмные начала» Филип Пулман", "Прочитай «Автостопом по галактике» Дуглас Адамс",
                 "Прочитай «Гарри Поттер и Кубок огня» Джоан Роулинг", "Прочитай «Убить пересмешника» Харпер Ли",
                 "Прочитай «Винни Пух» Алан Александр Милн", "Прочитай «1984» Джордж Оруэлл",
                 "Прочитай «Лев, колдунья и платяной шкаф» Клайв Стэйплз Льюис", "Прочитай «Джейн Эйр» Шарлотта Бронте",
                 "Прочитай «Уловка-22» Джозеф Хеллер", "Прочитай «Грозовой перевал» Эмили Бронте"]
        instence.text = random.choice(books) + "\n(Книги)"
        instence.halign = "center"


    def btn3_press(self, instence):
        movies = ["Посмотри «Побег из Шоушенка»","Посмотри «Крёстный отец»","Посмотри «Тёмный рыцарь»",
                  "Посмотри «Список Шиндлера»","Посмотри «Криминальное чтиво»",
                  "Посмотри «Форрест Гамп»","Посмотри «Бойцовский клуб»","Посмотри «Начало»",
                  "Посмотри «Матрица»","Посмотри «Семь»","Посмотри «Молчание ягнят»","Посмотри «Интерстеллар»"]
        instence.text = random.choice(movies) + "\n(Фильмы)"
        instence.halign = "center"

    def btn4_press(self, instence):
        countries = ["Посети Японию","Посети Австралию","Посети США","Посети Канаду",
                     "Посети Латвию","Посети Египет","Посети Мексику","Поосети ОАЭ","Посети Испанию",
                     "Посети Бразилию","Посети Данию","Посети Финляндию"]
        instence.text = random.choice(countries) + " \n(Страны)"
        instence.halign = "center"

    def btn5_press(self, instence):
        entertainment = ["Сходи в музей", "Послушай музыку", "Погуляй с другом/подругой", "Сходи в парк",
                         "Сходи на аттракционы", "Прыгни с парашютом", "Потанцуй", "Пой песни", "Займись йогой",
                         "Выгуляй домашнего животного", "Помедетируй"]
        instence.text = random.choice(entertainment) + "\n(Развлечения)"
        instence.halign = "center"

    def btn6_press(self, instence):
        study = ["Изучи психологию","Обучись видеомонтажу","Изучи программирование",
                 "Изучи иностранный язык", "Обучись трейдингу", "Обучись SMM","Обучись таргетингу",
                 "Обучись арбитражу", "Обучись маркетингу", "Обучись 3Д-моделированию"]
        instence.text = random.choice(study) + "\n(Изучения)"
        instence.halign = "center"

if __name__ == "__main__":
    MyApp().run()