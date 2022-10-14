# def register(login):
#             cur.execute(f'SELECT * FROM Logi WHERE login="{login}";')
#             value = cur.fetchall()
#             if value != []:
#                 print('Такоe имя уже используется!')
#                 return(1)



#             elif value == []:
#                 while True:
#                     passw = (input('Пароль(Минимум 6 символов):'))
#                     parol2 = len(passw)
#                     if parol2 >= 6:
#                         cur.execute(f"INSERT INTO Logi (login, passw) VALUES ('{login}', '{passw}')")
#                         db.commit()
#                         print('Вы успешно зарегистрированы!')
#                         db.commit()
#                         break
#                     else:
#                         print("Неправильный пароль")
#             cur.close()

# for i in range(3):
#     login = input("Login ")
#     # register(login)
#     if register(login) != 1:
#         break


# class One:
#     param1 = ['a', 'b']

# class Two:
#     i = One()
#     print(i.param1)


# from _typeshed import Self


# class Example:
#     ...

#     def OnSliderScroll(self, e):
#         id_slider = e.GetId()
#         obj = e.GetEventObject()
#         VARIABLE = obj.GetValue()
#         tty = str(val)+str(id_slider)
#         self.txt1.SetLabel(str(VARIABLE))
#         Example1.VARIABLE = VARIABLE


# class Example1:
#     ...

#     def OnPaint(self, e):    
#         dc = wx.PaintDC(self)
#         dc.SetPen(wx.Pen('#d4d4d4'))

#         dc.SetBrush(wx.Brush('#c56c00'))
#         dc.DrawRectangle(10, 7, 90, Example1.VARIABLE)


import starpusher
import sql1
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3
db = sqlite3.connect('C:/Users/kng/Desktop/AAAA/GAMEbd.db')
cur = db.cursor()


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui",self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)
        
        

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)

    

    # def show_window_2(self):
    #     show_window_2 = Client()
    #     widget.addWidget(show_window_2)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

    # def vrach(self):
    #     vrach = Vrach()
    #     widget.addWidget(vrach)
    #     widget.setCurrentIndex(widget.currentIndex()+1)
    
    # def gvrach(self):
    #     vrach = G_Vrach()
    #     widget.addWidget(vrach)
    #     widget.setCurrentIndex(widget.currentIndex()+1)
    
    # def register(self):
    #     register = Register()
    #     widget.addWidget(register)
    #     widget.setCurrentIndex(widget.currentIndex()+1)

    # def admin(self):
    #     admin = Admin()
    #     widget.addWidget(admin)
    #     widget.setCurrentIndex(widget.currentIndex()+1)


# class p():
#     def __init__(self): 
#         self.s = 55



    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        login = user

        if len(user)==0 or len(password)==0:
            self.error.setText("Пожалуйста, введите все поля.")

        else:
            parol = str(password)
            output = sql1.login(login,parol)
            if output == 1:

                starpusher.main(login)

            else:
                self.error.setText("Неверное имя пользователя или пароль")

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)
        self.close()
    def signupfunction(self):

        user = self.emailfield.text()
        password = self.passwordfield.text()
        login = user
        confirmpassword = self.confirmpasswordfield.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Пожалуйста, заполните все поля ввода.")

        elif password!=confirmpassword:
            self.error.setText("Пароли не совпадают")
        else:
            m = sql1.proverkalogin(login)
            if m == 1:
                self.error.setText("Такой ник уже используется.")

            elif m == 2:   
                login = user
                parol = str(password)  
                sql1.register(login,parol)
                starpusher.main(login)
                



            


# class FillProfileScreen(QDialog):
#     def __init__(self):
#         super(FillProfileScreen,self).__init__()
#         loadUi("fillprofile.ui",self)
#         self.signup.clicked.connect(self.fio)
#         self.image.setPixmap(QPixmap('zub.jpg'))

#     def fio(self):
#         firstname = self.firstname.text()
#         lastname = self.lastname.text()
#         login = self.username.text()
#         data_r = self.birthday.text()
#         fi = firstname + lastname
#         fio_klienta = fi
#         # print(data_r)
#         sql1.register2(login,fio_klienta,data_r)
#         LoginScreen.show_window_2(self)
# # class two(p):
# #     pass

# # x = two()
# # print(x.s)

# class Client(QDialog):

#         # super(Client,self).__init__()
#         # loadUi("client.ui",self)
#     def __init__(self):
#         super(Client,self).__init__()
#         loadUi("client.ui",self)
#         self.tableWidget.setColumnWidth(0, 200)
#         self.tableWidget.setColumnWidth(1, 180)
#         self.tableWidget.setColumnWidth(2, 180)
#         self.tableWidget.setColumnWidth(3, 120)
#         self.tableWidget.setColumnWidth(4, 100)
#         self.tableWidget.setHorizontalHeaderLabels(["Дата Приёма","Фио Клиента","Фио Врача","Услуга","Колличество"])
#         self.loaddata()

#     def loaddata(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table4 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget.setRowCount(20)
#         for row in results:
#             self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
#             self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
#             self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(sql1.koll2(tablerow+1)))
#             tablerow+=1
#         # login = FillProfileScreen.fio()
#         login = 'kng33'
        
#         self.loginlabel.setText(login)


# class Vrach(QDialog):
#     def __init__(self):
#         super(Vrach, self).__init__()
#         loadUi("tabletutorial.ui",self)
#         self.tableWidget.setColumnWidth(0, 200)
#         self.tableWidget.setColumnWidth(1, 180)
#         self.tableWidget.setColumnWidth(2, 180)
#         self.tableWidget.setColumnWidth(3, 120)
#         self.tableWidget.setColumnWidth(4, 100)
#         self.tableWidget.setHorizontalHeaderLabels(["Дата Приёма","Фио Клиента","Фио Врача","Услуга","Колличество"])
#         self.loaddata()

#     def loaddata(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table4 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget.setRowCount(20)
#         for row in results:
#             self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
#             self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
#             self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(sql1.koll2(tablerow+1)))
#             tablerow+=1


# class G_Vrach(QDialog):
#     def __init__(self):
#         super(G_Vrach, self).__init__()
#         loadUi("tabletutorial2.ui",self)
#         self.ready.clicked.connect(self.dobavit)
#         self.ready_2.clicked.connect(self.delete)
#         self.tableWidget.setColumnWidth(0, 200)
#         self.tableWidget.setColumnWidth(1, 180)
#         self.tableWidget.setColumnWidth(2, 180)
#         self.tableWidget.setColumnWidth(3, 120)
#         self.tableWidget.setColumnWidth(4, 100)
#         self.tableWidget.setHorizontalHeaderLabels(["КодВрача","Фио Врача","Должность","Логин"])
#         self.loaddata()
#         self.tableWidget2.setColumnWidth(0, 200)
#         self.tableWidget2.setColumnWidth(1, 180)
#         self.tableWidget2.setColumnWidth(2, 180)
#         self.tableWidget2.setHorizontalHeaderLabels(["Фио Клиента","Дата Рождения","Лет"])
#         self.loaddata2()
#         self.tableWidget3.setColumnWidth(0, 200)
#         self.tableWidget3.setColumnWidth(1, 180)
#         self.tableWidget3.setColumnWidth(2, 180)
#         self.tableWidget3.setColumnWidth(3, 120)
#         self.tableWidget3.setColumnWidth(4, 100)
#         self.tableWidget3.setHorizontalHeaderLabels(["Дата Приёма","Фио Клиента","Фио Врача","Услуга","Колличество"])
#         self.loaddata3()
#         self.tableWidget_2.setColumnWidth(0, 200)
#         self.tableWidget_2.setColumnWidth(1, 180)
#         self.tableWidget_2.setHorizontalHeaderLabels(["Название","Стоимость"])
#         self.loaddata4()
        
#     # def dobavit(self):
#     #     sql1.dobavit_vracha()

#     # def delete(self):
#     #     sql1.delete_table4(argument,chto_delete)

#     def loaddata(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table2 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget.setRowCount(20)
#         for row in results:
#             self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[3]))
#             self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
#             tablerow+=1
#             #
#     def loaddata2(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = ('SELECT * FROM table3')

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget2.setRowCount(40)
#         for row in results:
#             self.tableWidget2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(sql1.age(tablerow+1)))
#             tablerow+=1

#     def loaddata3(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table4 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget3.setRowCount(20)
#         for row in results:
#             self.tableWidget3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
#             self.tableWidget3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
#             self.tableWidget3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(sql1.koll2(tablerow+1)))
#             tablerow+=1

#     def loaddata4(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table5 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget_2.setRowCount(20)
#         for row in results:
#             self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(sql1.koll(tablerow+1)))
#             tablerow+=1
            
#     def dobavit(self):
#         dobavit_vrach = Dobavit()
#         widget.addWidget(dobavit_vrach)
#         widget.setCurrentIndex(widget.currentIndex()+1)

#     def delete(self):
#         dobavit_vrach = Delete()
#         widget.addWidget(dobavit_vrach)
#         widget.setCurrentIndex(widget.currentIndex()+1)
    
# class Register(QDialog):
#     def __init__(self):
#         super(Register, self).__init__()
#         loadUi("Register.ui",self)
#         self.edit_2.clicked.connect(self.edit)
#         self.delete_2.clicked.connect(self.delete)
#         # self.chto_delete_2.clicked.connect(self.chto_delete)

# # class Delete(QDialog):
# #     def __init__(self):
# #         super(Register, self).__init__()
# #         loadUi("Register.ui",self)
# #         self.edit.clicked_2.connect(self.edit)
# #         self.chto_delete_2.clicked.connect(self.chto_delete)
        
#         self.tableWidget.setColumnWidth(0, 200)
#         self.tableWidget.setColumnWidth(1, 180)
#         self.tableWidget.setColumnWidth(2, 180)
#         self.tableWidget.setColumnWidth(3, 120)
#         self.tableWidget.setColumnWidth(4, 100)
#         self.tableWidget.setHorizontalHeaderLabels(["КодВрача","Фио Врача","Должность","Логин"])
#         self.loaddata()
#         self.tableWidget2.setColumnWidth(0, 200)
#         self.tableWidget2.setColumnWidth(1, 180)
#         self.tableWidget2.setColumnWidth(2, 180)
#         self.tableWidget2.setHorizontalHeaderLabels(["Фио Клиента","Дата Рождения","Лет"])
#         self.loaddata2()
#         self.tableWidget3.setColumnWidth(0, 200)
#         self.tableWidget3.setColumnWidth(1, 180)
#         self.tableWidget3.setColumnWidth(2, 180)
#         self.tableWidget3.setColumnWidth(3, 120)
#         self.tableWidget3.setColumnWidth(4, 100)
#         self.tableWidget3.setHorizontalHeaderLabels(["Дата Приёма","Фио Клиента","Фио Врача","Услуга","Колличество"])
#         self.loaddata3()
#         self.tableWidget_2.setColumnWidth(0, 200)
#         self.tableWidget_2.setColumnWidth(1, 180)
#         self.tableWidget_2.setHorizontalHeaderLabels(["Название","Стоимость"])
#         self.loaddata4()
        
#     # def chek_(self):
#     #     widget.setCurrentIndex(widget.currentIndex()+1)
#     #     loadUi("edit.ui",self)

        
#     def edit(self):
#         edit = Edit()
#         widget.addWidget(edit)
#         widget.setCurrentIndex(widget.currentIndex()+1) 

#     def delete(self):
#         edit = Delete4()
#         widget.addWidget(edit)
#         widget.setCurrentIndex(widget.currentIndex()+1) 


#     def loaddata(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table2 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget.setRowCount(20)
#         for row in results:
#             self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[3]))
#             self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
#             tablerow+=1
#             #
#     def loaddata2(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = ('SELECT * FROM table3')

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget2.setRowCount(40)
#         for row in results:
#             self.tableWidget2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(sql1.age(tablerow+1)))
#             tablerow+=1

#     def loaddata3(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table4 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget3.setRowCount(20)
#         for row in results:
#             self.tableWidget3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
#             self.tableWidget3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
#             self.tableWidget3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(sql1.koll2(tablerow+1)))
#             tablerow+=1

#     def loaddata4(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table5 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget_2.setRowCount(20)
#         for row in results:
#             self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(sql1.koll(tablerow+1)))
#             tablerow+=1
        
# class Dobavit(QDialog):
#     def __init__(self):
#         super(Dobavit, self).__init__()
#         loadUi("edit.ui",self)
#         self.prodoljit.clicked.connect(self.dobavit)


#     def dobavit(self):
#         kod_vracha = self.kod_vracha.text()
#         kod_vracha = int(kod_vracha)
#         fio_vracha = self.fio_vracha.text()
#         doljnost = self.doljnost.text()
#         login = self.login.text()
#         # print(type(login))
#         sql1.dobavit_vracha(kod_vracha,fio_vracha,doljnost,login)

# # dobavit_vracha(10001,'нИкитаШ','Должность','Аа')

# class Delete(QDialog):
#     def __init__(self):
#         super(Delete, self).__init__()
#         loadUi("edit.ui",self)
#         self.prodoljit.clicked.connect(self.dobavit)
    
#     def dobavit(self):
#         kod_vracha = self.kod_vracha.text()
#         kod_vracha = int(kod_vracha)
#         fio_vracha = self.fio_vracha.text()
#         doljnost = self.doljnost.text()
#         login = self.login.text()
#         sql1.delete_table2(kod_vracha)
        
# class Edit(QDialog):
#     def __init__(self):
#         super(Edit, self).__init__()
#         loadUi("edit2.ui",self)
#         self.prodoljit.clicked.connect(self.dobavit)
    
#     def dobavit(self):
#         data_priema = self.data_priema.text()
#         fio_klienta = self.fio_klienta.text()
#         fio_vracha = self.fio_vracha.text()
#         kod_vracha = self.kod_vracha.text()
#         usluga = self.usluga.text()
#         stoimost_uslugi = self.stoimost_uslugi.text()
#         koll = self.koll.text()
#         koll = int(koll)
#         stoimost_uslugi = int(stoimost_uslugi)
#         sql1.dobavit_table4(data_priema,fio_klienta ,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll)
        
# class Delete4(QDialog):
#     def __init__(self):
#         super(Delete4, self).__init__()
#         loadUi("edit2.ui",self)
#         self.prodoljit.clicked.connect(self.dobavit)
    
#     def dobavit(self):
#         data_priema = self.data_priema.text()
#         fio_klienta = self.fio_klienta.text()
#         fio_vracha = self.fio_vracha.text()
#         kod_vracha = self.kod_vracha.text()
#         usluga = self.usluga.text()
#         stoimost_uslugi = self.stoimost_uslugi.text()
#         koll = self.koll.text()
#         kod_vracha = int(kod_vracha)
#         sql1.delete_table42(kod_vracha)

# class Admin(QDialog):
#     def __init__(self):
#         super(Admin, self).__init__()
#         loadUi("Admin.ui",self)
#         # self.ready.clicked.connect(self.dobavit)
#         # self.ready_2.clicked.connect(self.delete)
#         self.Delete.clicked.connect(self.delete_)
#         self.all.clicked.connect(self.all_)
#         self.tableWidget.setColumnWidth(0, 200)
#         self.tableWidget.setColumnWidth(1, 180)
#         self.tableWidget.setColumnWidth(2, 180)
#         self.tableWidget.setColumnWidth(3, 120)
#         self.tableWidget.setColumnWidth(4, 100)
#         self.tableWidget.setHorizontalHeaderLabels(["КодВрача","Фио Врача","Должность","Логин"])
#         self.loaddata()
#         self.tableWidget2.setColumnWidth(0, 200)
#         self.tableWidget2.setColumnWidth(1, 180)
#         self.tableWidget2.setColumnWidth(2, 180)
#         self.tableWidget2.setHorizontalHeaderLabels(["Фио Клиента","Дата Рождения","Лет"])
#         self.loaddata2()
#         self.tableWidget3.setColumnWidth(0, 200)
#         self.tableWidget3.setColumnWidth(1, 180)
#         self.tableWidget3.setColumnWidth(2, 180)
#         self.tableWidget3.setColumnWidth(3, 120)
#         self.tableWidget3.setColumnWidth(4, 100)
#         self.tableWidget3.setHorizontalHeaderLabels(["Дата Приёма","Фио Клиента","Фио Врача","Услуга","Колличество"])
#         self.loaddata3()
#         self.tableWidget_2.setColumnWidth(0, 200)
#         self.tableWidget_2.setColumnWidth(1, 180)
#         self.tableWidget_2.setHorizontalHeaderLabels(["Название","Стоимость"])
#         self.loaddata4()
#         self.tableWidget_3.setColumnWidth(0, 200)
#         self.tableWidget_3.setColumnWidth(1, 180)
#         self.tableWidget_3.setColumnWidth(2, 180)
#         self.tableWidget_3.setHorizontalHeaderLabels(["login","parol","kto v bd"])
#         self.loaddata5()
        
#     # def dobavit(self):
#     #     sql1.dobavit_vracha()

#     # def delete(self):
#     #     sql1.delete_table4(argument,chto_delete)

#     def loaddata(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table2 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget.setRowCount(20)
#         for row in results:
#             self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[3]))
#             self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
#             tablerow+=1
#             #
#     def loaddata2(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = ('SELECT * FROM table3')

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget2.setRowCount(40)
#         for row in results:
#             self.tableWidget2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(sql1.age(tablerow+1)))
#             tablerow+=1

#     def loaddata3(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table4 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget3.setRowCount(20)
#         for row in results:
#             self.tableWidget3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
#             self.tableWidget3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
#             self.tableWidget3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
#             self.tableWidget3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(sql1.koll2(tablerow+1)))
#             tablerow+=1

#     def loaddata4(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = 'SELECT * FROM table5 LIMIT 10'

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget_2.setRowCount(20)
#         for row in results:
#             self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(sql1.koll(tablerow+1)))
#             tablerow+=1

#     def loaddata5(self):
#         connection = sqlite3.connect('sql_10.db')
#         cur = connection.cursor()
#         sqlstr = ('SELECT * FROM table1')

#         tablerow=0
#         results = cur.execute(sqlstr)
#         self.tableWidget_3.setRowCount(40)
#         for row in results:
#             self.tableWidget_3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
#             self.tableWidget_3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(sql1.parol(tablerow+1)))
#             self.tableWidget_3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[4]))
#             tablerow+=1

#     def all_(self):
#         edit = All()
#         widget.addWidget(edit)
#         widget.setCurrentIndex(widget.currentIndex()+1) 
    
#     def delete_(self):
#         chtodel = self.chtodel.text()
#         argument = self.argument.text()
#         table = self.table.text()
#         sql1.delete(table,argument,chtodel)

# class All(QDialog):
#     def __init__(self):
#         super(All, self).__init__()
#         loadUi("all.ui",self)
#     #     self.prodoljit.clicked.connect(self.dobavit)
    
#     # def dobavit(self):
#     #     data_priema = self.data_priema.text()
#     #     fio_klienta = self.fio_klienta.text()
#     #     fio_vracha = self.fio_vracha.text()
#     #     kod_vracha = self.kod_vracha.text()
#     #     usluga = self.usluga.text()
#     #     stoimost_uslugi = self.stoimost_uslugi.text()
#     #     koll = self.koll.text()
#     #     koll = int(koll)
#     #     stoimost_uslugi = int(stoimost_uslugi)
#     #     sql1.dobavit_table4(data_priema,fio_klienta ,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll)

app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('выход')


# class First:
#     def __init__(self):
#         self.name = 'Name'

# class Second:
#     def __init__(self, name):
#         self.name = name


# first = First()
# second = Second(first.name)
# print(second.name)