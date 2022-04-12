import webbrowser
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from datetime import datetime
from translate import Translator
import requests
import time

now = datetime.now()

Form, Window = uic.loadUiType("G://3 курс//Практика//Проект//pogoda.ui") #загрузка окна "Погода"

app = QApplication([])
pogoda = Window()
form = Form()
form.setupUi(pogoda)

Form1, Window1 = uic.loadUiType("G://3 курс//Практика//Проект//glavnoeokno.ui") #загрузка главного окна

global glavnoeokno
glavnoeokno = Window1()
glavnoeokno.setObjectName("MainWindow1")
form1 = Form1()
form1.setupUi(glavnoeokno)
glavnoeokno.show()

Form2, Window2 = uic.loadUiType("G://3 курс//Практика//Проект//podscazka.ui") #загрузка окна "Подсказка"

global podscazka
podscazka = Window2()
form2 = Form2()
form2.setupUi(podscazka)

Form3, Window3 = uic.loadUiType("G://3 курс//Практика//Проект//nastroika.ui") #загрузка окна "Настройки"

global nastroika
nastroika = Window3()
form3 = Form3()
form3.setupUi(nastroika)

#методы для смены темы программы в зависимости от погоды
def pasmurno():
    pogoda.setStyleSheet("background-color:rgb(149, 147, 150); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color:rgb(149, 147, 150); font: 12pt, Comic Sans MS;")

def dogh():
    pogoda.setStyleSheet("background-color:rgb(104, 159, 193); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color:rgb(104, 159, 193); font: 12pt, Comic Sans MS;")

def yasno():
    pogoda.setStyleSheet("background-color:rgb(255, 213, 140); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color:rgb(255, 213, 140); font: 12pt, Comic Sans MS;")

def groza():
    pogoda.setStyleSheet("background-color:rgb(114, 114, 170); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color: rgb(114, 114, 170); font: 12pt, Comic Sans MS;")

def sneg():
    pogoda.setStyleSheet("background-color:rgb(255, 250, 250); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color:rgb(255, 250, 250); font: 12pt, Comic Sans MS;")

def tyman():
    pogoda.setStyleSheet("background-color:rgb(236, 240, 241); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color:rgb(236, 240, 241); font: 12pt, Comic Sans MS;")

def pog():
    pogoda.setStyleSheet("background-color:rgb(207, 212, 255); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color:rgb(207, 212, 255); font: 12pt, Comic Sans MS;")

def printButtonPressed(): #обработка кнопки "Поиск" на окне "Погода
    pogoda.setFixedSize(414, 549)
    form.pushButton_3.setText("Подробнее")
    cityName = str(form.lineEdit.text())
    apiKey = "98c4111b69ad59a17100bc1e4de1033a"
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    completeUrl = baseUrl + "appid=" + apiKey + "&q=" + cityName
    response = requests.get(completeUrl, params={'lang': 'ru'})
    data = response.json() #получение погодных данных
    if data["cod"] != "404":
        y = data["main"]
        temperature = y["temp"] - 273.15
        temperature = str(round(temperature)) + "°C"
        z = data["weather"]
        weather = str(z[0]["description"])
        if weather == "пасмурно" or weather == "небольшая облачность" or weather == "переменная облачность": #вставка картинки и смена темы окон программы в зависимости от прогноза погоды
            pixmap = QPixmap("G://3 курс//Практика//Проект//облачно.png")
            form.label_6.setPixmap(pixmap)
            pasmurno()
        elif weather == "небольшой дождь" or weather == "небольшой проливной дождь" or weather == "дождь" or weather == "небольшая морось" or weather == "сильный дождь" or weather == "проливной дождь":
            pixmap = QPixmap("G://3 курс//Практика//Проект//дождь.png")
            form.label_6.setPixmap(pixmap)
            dogh()
        elif weather == "туман" or weather == "мгла" or weather == "плотный туман":
            pixmap = QPixmap("G://3 курс//Практика//Проект//туман.png")
            form.label_6.setPixmap(pixmap)
            tyman()
        elif weather == "снег" or weather == "сильный снег" or weather == "небольшой снег" or weather == "снегопад":
            pixmap = QPixmap("G://3 курс//Практика//Проект//снег.png")
            form.label_6.setPixmap(pixmap)
            sneg()
        elif weather == "ясно":
            pixmap = QPixmap("G://3 курс//Практика//Проект//солнце.png")
            form.label_6.setPixmap(pixmap)
            yasno()
        elif weather == "гроза" or weather == "гроза с дождём" or weather == "гроза с небольшим дождём" or weather == "гроза с сильным дождём":
            pixmap = QPixmap("G://3 курс//Практика//Проект//гроза.png")
            form.label_6.setPixmap(pixmap)
            groza()
        else:
            pixmap = QPixmap("G://3 курс//Практика//Проект//погода.png")
            form.label_6.setPixmap(pixmap)
            pog()
        form.lineEdit_5.setText(cityName.title())
        form.lineEdit_4.setText(weather.capitalize())
        form.line.setText(temperature)
        form.lineEdit_2.setText("Атмосферное давление: " + str(y["pressure"]) + " ГПа")
        form.lineEdit_3.setText("Влажность: " + str(y["humidity"]) + "%")
        form.lineEdit_6.setText("Скорость ветра: " + str(data['wind']['speed']) + " м/с")
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        form.lineEdit_7.setText("Время восхода солнца: " + str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(sunrise))))
        form.lineEdit_8.setText("Время захода солнца: " + str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(sunset))))
        translator = Translator(to_lang="Russian")
        den = str(now.strftime("%a"))
        den = translator.translate(den)
        form.lineEdit_11.setText(data['sys']['country'])
        form.lineEdit_9.setText(den + " " + (str(time.strftime('%d-%m-%Y %H:%M', time.localtime()))))
        form.lineEdit.clear()
        feels = y["feels_like"] - 273.15
        feels = str(round(feels)) + "°C"
        form.line_2.setText("Ощущается как "+ feels) #вывод прогноза погоды на экран
    else:
        oshibka = QMessageBox()
        oshibka.setStyleSheet("""
                QMessageBox{font: 14 pt Comic Sans MS;} 
                QPushButton{font: 14 pt Comic Sans MS;} 
                """)
        oshibka.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
        oshibka.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//ошибка.png"))
        oshibka.setText("Неверно введен город.\nПопробуйте еще раз!")
        oshibka.setWindowTitle("Ошибка")
        oshibka.exec_() #сообщение об ошибке при неверном вводе города

def podcazki(): #обработка кнопки "Получить подсказки"
    pogoda.close()
    podscazka.show()
    weather = str(form.lineEdit_4.text().lower())
    if weather == "пасмурно" or weather == "небольшая облачность" or weather == "переменная облачность": #подсказка в зависимости от погоды
        #pixmap = QPixmap("G://3 курс//Практика//Проект//осень.png")
        form2.pushButton.setIcon(QIcon("G://3 курс//Практика//Проект//осень.png"))
        form2.pushButton_2.setText("Подумайте о наряде!")
    elif weather == "небольшой дождь" or weather == "небольшой проливной дождь" or weather == "дождь" or weather == "небольшая морось" or weather == "сильный дождь" or weather == "проливной дождь":
        #pixmap = QPixmap("G://3 курс//Практика//Проект//осень.png")
        form2.pushButton.setIcon(QIcon("G://3 курс//Практика//Проект//осень.png"))
        form2.pushButton_2.setText("Не забудьте зонтик!")
    elif weather == "туман" or weather == "мгла" or weather == "плотный туман":
        #pixmap = QPixmap("G://3 курс//Практика//Проект//осень.png")
        form2.pushButton.setIcon(QIcon("G://3 курс//Практика//Проект//осень.png"))
        form2.pushButton_2.setText("Будьте аккуратны!")
    elif weather == "снег" or weather == "сильный снег" or weather == "небольшой снег" or weather == "снегопад":
        #pixmap = QPixmap("G://3 курс//Практика//Проект//зима.png")
        form2.pushButton.setIcon(QIcon("G://3 курс//Практика//Проект//зима.png"))
        form2.pushButton_2.setText("Оденьтесь потеплее!")
    elif weather == "ясно":
        #pixmap = QPixmap("G://3 курс//Практика//Проект//тепло.png")
        form2.pushButton.setIcon(QIcon("G://3 курс//Практика//Проект//тепло.png"))
        form2.pushButton_2.setText("Стоит подумать, что надеть!")
    elif weather == "гроза" or weather == "гроза с дождём" or weather == "гроза с небольшим дождём" or weather == "гроза с сильным дождём":
        #pixmap = QPixmap("G://3 курс//Практика//Проект//осень.png")
        form2.pushButton.setIcon(QIcon("G://3 курс//Практика//Проект//осень.png"))
        form2.pushButton_2.setText("Будьте осторожны!")
    else:
        #pixmap = QPixmap("G://3 курс//Практика//Проект//тепло.png")
        form2.pushButton.setIcon(QIcon("G://3 курс//Практика//Проект//тепло.png"))
        form2.pushButton_2.setText("Подумайте о вашем наряде!")

textfield = form.lineEdit
textfield.setFocus()
form.pushButton.clicked.connect(printButtonPressed)
textfield.returnPressed.connect(form.pushButton.click)
form.pushButton_2.clicked.connect(podcazki)
form.pushButton_3.clicked.connect(lambda: webbrowser.open('https://www.gismeteo.by/catalog/')) #ссылка для получения подробной информации, обработки кнопки "Подробнее"
form2.pushButton.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/watch?v=pXlWrfSusuI')) #ссылка для перехода и просмотра видео прогноза погоды, обработка кнопки-картинки на окне "Подсказка"
form2.pushButton_2.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/watch?v=pXlWrfSusuI'))

def spravka(): #вывод справки (информация о программе) для окон программы
    spravka = QMessageBox()
    spravka.setStyleSheet("""
        QMessageBox{font: 14 pt Comic Sans MS;} 
        QPushButton{font: 14 pt Comic Sans MS;} 
        """)
    spravka.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
    spravka.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//информация.png"))
    spravka.setText("Программа: «Программное средство «Alex.Погода»».\n\nРазработчик: Коробова Александра Николаевна, учащаяся группы 9К9392.\n\nПреподаватель: Василькова Анастасия Николаевна.")
    spravka.setWindowTitle("Справка")
    spravka.exec_()

def pomosh(): #вывод помощи для работы с программой для пользователя
    pomosh = QMessageBox()
    pomosh.setStyleSheet("""
            QMessageBox{font: 14 pt Comic Sans MS;} 
            QPushButton{font: 14 pt Comic Sans MS;} 
            """)
    pomosh.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
    pomosh.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//помощь.png"))
    pomosh.setText("Для того, чтобы получить погодные данные на определенной области следует:\n\n1. На главном окне нажмите кнопку «Поиск прогноза погоды».\n"
                    "2. В окне «Погода» введите город, прогноз погоды которого Вы хотите узнать.\n3. Нажмите кнопку «Поиск» или Enter, чтобы получить погодные данные.\n4. Просмотрите информацию на окне «Погода», а для получения дополнительной информации нажмите кнопку «Получить подсказки» или перейдите по ссылке «Подробнее».\n\n"
                   "Для того, чтобы получить справку, содержащую информацию о программе, выберите на панели меню, находящейся вверху окна программы, элемент «Справка».\n\n"
                   "Для того, чтобы сменить тему приложения, выберите на панели меню, находящейся вверху главного окна программы, элемент «Настройки».\n\n"
                   "Для выхода из приложения выберите на панели меню, находящейся вверху окна программы, элемент «Выход». Подтвердите выход.")
    pomosh.setWindowTitle("Помощь")
    pomosh.exec_()

def nastroiki(): #переход к окну "Настройки"
    glavnoeokno.close()
    nastroika.show()

def tema(): #смена темы программы
    glavnoeokno.setStyleSheet("background-color: rgb(109, 112, 134); font: 12pt, Comic Sans MS;")
    pogoda.setStyleSheet("background-color: rgb(109, 112, 134); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color: rgb(109, 112, 134); font: 12pt, Comic Sans MS;")
    nastroika.setStyleSheet("background-color: rgb(109, 112, 134); font: 12pt, Comic Sans MS;")

def sbros(): #смена темы на светлую
    form3.radioButton.setChecked(False)
    glavnoeokno.setStyleSheet("background-color:  rgb(207, 212, 255); font: 12pt, Comic Sans MS;")
    pogoda.setStyleSheet("background-color:  rgb(207, 212, 255); font: 12pt, Comic Sans MS;")
    podscazka.setStyleSheet("background-color:  rgb(207, 212, 255); font: 12pt, Comic Sans MS;")
    nastroika.setStyleSheet("background-color:  rgb(207, 212, 255); font: 12pt, Comic Sans MS;")

form3.pushButton.clicked.connect(tema)
form3.radioButton.toggled.connect(sbros)

def perehodnastroika(): #переход с окна "Настройки" к главному окну
    nastroika.close()
    glavnoeokno.show()

def exitnastroika(): #выход из программы (окно "Настройки")
    exitnastroika = QMessageBox()
    exitnastroika.setStyleSheet("""
            QMessageBox{font: 14 pt Comic Sans MS;} 
            QPushButton{font: 14 pt Comic Sans MS;} 
            """)
    exitnastroika.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
    exitnastroika.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//выход.png"))
    exitnastroika.setWindowTitle("Выход")
    exitnastroika.setText("Вы уверены, что хотите выйти?")
    exitnastroika.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    exitnastroika.button(exitnastroika.Yes).setText("Да")
    exitnastroika.button(exitnastroika.No).setText("Нет")
    returnValue = exitnastroika.exec()
    if returnValue == QMessageBox.Yes:
        nastroika.close()

def pomoshnastroika(): #вывод помощи для работы с окном "Настройки" для пользователя
    pomoshnastroika = QMessageBox()
    pomoshnastroika.setStyleSheet("""
                QMessageBox{font: 14 pt Comic Sans MS;} 
                QPushButton{font: 14 pt Comic Sans MS;} 
                """)
    pomoshnastroika.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
    pomoshnastroika.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//помощь.png"))
    pomoshnastroika.setText("Для того, чтобы сменить тему приложения, нажмите на окне «Настройки» кнопку «Сменить тему».\n\n"
                            "Чтобы сменить темную тему на светлую следует нажать на окне «Настройки» кнопку «Сбросить все».\n\n"
                            "Для перехода на главное окно выберите на панели меню, находящейся вверху окна программы, элемент «Главное окно».\n\n"
                            "Для получения справки, содержащей информацию о программе, выберите на панели меню, находящейся вверху окна программы, элемент «Справка».\n\n"
                            "Для выхода из приложения выберите на панели меню, находящейся вверху окна программы, элемент «Выход». Подтвердите выход.")
    pomoshnastroika.setWindowTitle("Помощь")
    pomoshnastroika.exec_()

form3.action.triggered.connect(perehodnastroika)
form3.action_2.triggered.connect(spravka)
form3.action_3.triggered.connect(pomoshnastroika)
form3.action_4.triggered.connect(exitnastroika) #действия меню окна "Настройки"

def exitpogoda(): #выход из программы (окно "Погода")
    exitpogoda = QMessageBox()
    exitpogoda.setStyleSheet("""
                    QMessageBox{font: 14 pt Comic Sans MS;} 
                    QPushButton{font: 14 pt Comic Sans MS;} 
                    """)
    exitpogoda.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
    exitpogoda.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//выход.png"))
    exitpogoda.setWindowTitle("Выход")
    exitpogoda.setText("Вы уверены, что хотите выйти?")
    exitpogoda.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    exitpogoda.button(exitpogoda.Yes).setText("Да")
    exitpogoda.button(exitpogoda.No).setText("Нет")
    returnValue = exitpogoda.exec()
    if returnValue == QMessageBox.Yes:
        pogoda.close()

def perehodpogoda(): #закрытие окна "Погода" и переход к главному окну
    pogoda.close()
    glavnoeokno.show()

form.action.triggered.connect(perehodpogoda)
form.action_2.triggered.connect(spravka)
form.action_3.triggered.connect(pomosh)
form.action_4.triggered.connect(exitpogoda) #действия меню окна "Погода"

def perehodglavnoeokno():  #закрытие главного окна и переход к окну "Погода"
    glavnoeokno.close()
    pogoda.show()

def exitglavnoeokno(): #выход из программы (главное окно)
    exitglavnoeokno = QMessageBox()
    exitglavnoeokno.setStyleSheet("""
        QMessageBox{font: 14 pt Comic Sans MS;} 
        QPushButton{font: 14 pt Comic Sans MS;} 
    """)
    exitglavnoeokno.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
    exitglavnoeokno.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//выход.png"))
    exitglavnoeokno.setWindowTitle("Выход")
    exitglavnoeokno.setText("Вы уверены, что хотите выйти?")
    exitglavnoeokno.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    exitglavnoeokno.button(exitglavnoeokno.Yes).setText("Да")
    exitglavnoeokno.button(exitglavnoeokno.No).setText("Нет")
    returnValue = exitglavnoeokno.exec()
    if returnValue == QMessageBox.Yes:
        glavnoeokno.close()

form1.pushButton_4.clicked.connect(perehodglavnoeokno)
form1.action.triggered.connect(spravka)
form1.action_2.triggered.connect(pomosh)
form1.action_3.triggered.connect(nastroiki)
form1.action_4.triggered.connect(exitglavnoeokno) #действия меню главного окна

def perehodpodscazka(): #закрытие окна "Подсказка" и переход к окну "Погода"
    podscazka.close()
    pogoda.show()

def pomoshpodscazka(): #вывод помощи для работы с окном "Подсказка" для пользователя
    pomoshpodscazka = QMessageBox()
    pomoshpodscazka.setStyleSheet("""
                        QMessageBox{font: 14 pt Comic Sans MS;} 
                        QPushButton{font: 14 pt Comic Sans MS;} 
                        """)
    pomoshpodscazka.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
    pomoshpodscazka.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//помощь.png"))
    pomoshpodscazka.setText("Нажмите на картинку, расположенную на окне «Подсказка», чтобы получить дополнительную информацию.\n\n"
                            "Для перехода к окну «Погода» выберите на панели меню, находящейся вверху окна программы, элемент «Погода».\n\n"
                            "Для получения справки, содержащей информацию о программе, выберите на панели меню, находящейся вверху окна программы, элемент «Справка».\n\n"
                            "Для выхода из приложения выберите на панели меню, находящейся вверху окна программы, элемент «Выход». Подтвердите выход.")
    pomoshpodscazka.setWindowTitle("Помощь")
    pomoshpodscazka.exec_()

def exitpodscazka(): #выход из программы (окно "Подсказка")
    exitpodscazka = QMessageBox()
    exitpodscazka.setStyleSheet("""
                            QMessageBox{font: 14 pt Comic Sans MS;} 
                            QPushButton{font: 14 pt Comic Sans MS;} 
                            """)
    exitpodscazka.setWindowIcon(QIcon("G://3 курс//Практика//Проект//иконка.png"))
    exitpodscazka.setIconPixmap(QPixmap("G://3 курс//Практика//Проект//выход.png"))
    exitpodscazka.setWindowTitle("Выход")
    exitpodscazka.setText("Вы уверены, что хотите выйти?")
    exitpodscazka.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    exitpodscazka.button(exitpodscazka.Yes).setText("Да")
    exitpodscazka.button(exitpodscazka.No).setText("Нет")
    returnValue = exitpodscazka.exec()
    if returnValue == QMessageBox.Yes:
        podscazka.close()

form2.action.triggered.connect(perehodpodscazka)
form2.action_2.triggered.connect(spravka)
form2.action_3.triggered.connect(pomoshpodscazka)
form2.action_4.triggered.connect(exitpodscazka) #действия меню окна "Подсказка"

app.exec_()



