
import sqlite3
import time
db = sqlite3.connect('C:/Users/kng/Desktop/AAAA/GAMEbd.db')
cur = db.cursor()
# #  Создание первой таблицы       Имя 
# ## СЛЕДИ ЗА ЗНАЧЕНИЯМИ ТЕКСТ ИЛИ ИНТЕДЖЕР
# cur.execute('''CREATE TABLE main(
# id INTEGER PRIMARY KEY,
# shagi integer NOT NULL,
# lvl TEXT NOT NULL,
# name TEXT                    
# )''')

# def dobavit1():
#     cur.execute(f'INSERT INTO main (nazvanie) VALUES(?) ',[1]) 
#     print("Запись успешно добавлена")
#     db.commit()
# dobavit1()
# def prosmort():
#     cur.execute('SELECT * FROM main')
#     result = cur.fetchall()
#     x = len(result)
#     print(x)
#     return(x)
# # print(prosmort())
# for i in range((prosmort())):
#     print(i)
#     db = sqlite3.connect(f'{i+1}.db')
#     cur = db.cursor()



# # cur.execute('''CREATE TABLE login (
# # id INTEGER PRIMARY KEY,
# # login TEXT NOT NULL
# # )''')
# ## СЛЕДИ ЗА ЗНАЧЕНИЯМИ ТЕКСТ ИЛИ ИНТЕДЖЕР

# # cur.execute('''CREATE TABLE table2 (
# # id INTEGER PRIMARY KEY,
# # kod_vracha INTEGER NOT NULL,
# # fio_vracha TEXT NOT NULL,
# # doljnost TEXT NOT NULL,
# # login TEXT NOT NULL
# # )''')

# # 1	Аня Т	26.10.2003	17
# # 2	Анаит Т	26.10.2003	17
# # 3	Коля К	31.05.1999	65
# # 4	Егор Б	12.04.12	11
# # 5	Базаров Д	3.05.1978	44
# # cur.execute('''CREATE TABLE table3 (
# #     id INTEGER PRIMARY KEY,
# #     fio_klienta TEXT  NOT NULL,
# #     data_r INTEGER NOT NULL,
# #     age INTEGER NOT NULL,
# #     login TEXT NOT NULL
# # )''')

# # cur.execute('''CREATE TABLE table6(
# # id INTEGER PRIMARY KEY,
# # price text NOT NULL,
# # name text NOT NULL
# # )''')

# # cur.execute(''' CREATE TABLE table4 (
# #     id              INTEGER PRIMARY KEY,
# #     data_priema     INTEGER NOT NULL,
# #     fio_klienta     TEXT    NOT NULL,
# #     fio_vracha      TEXT    NOT NULL,
# #     kod_vracha      INTEGER NOT NULL,
# #     usluga          TEXT    NOT NULL,
# #     stoimost_uslugi INTEGER NOT NULL,
# #     koll            INTEGER NOT NULL,
# #     summa_itog      INTEGER NOT NULL
    
# # )''')
# def proverkatovar(name,price):
#     cur.execute(f'SELECT * FROM table6 WHERE name="{name}";') 
#     value = cur.fetchall()
#     if value != []:
#         print('Такой товар уже зарегестрирован!')
#     elif value == []:
#         def zapis(name,price):
#                     cur.execute('INSERT INTO table6 (name, price) VALUES(?,?) ',[name,price]) 
#                     print("Запись успешно добавлена")
#                     db.commit()
#         zapis(name,price)



# def prosmort_table5():
#     cur.execute('SELECT * FROM table5')
#     result = cur.fetchall()
#     print(result,sep='/n')

# def pribl():
#     cur.execute('SELECT price FROM table6')
#     result = cur.fetchall()
#     summa = []
#     for i in range(len(result)):
#         x = result[i]
#         l = (''.join(map(str,x)))
#         x2 = (float(l))
#         summa.append(x2)
#     summa = (sum(summa))
#     print(f'Общая прибль со всех товаров в наличии составила',summa,'₽')
# # pribl()
# def prosmort_table2():
#     cur.execute('SELECT id,fio_vracha,kod_vracha,login FROM table2 WHERE doljnost = "Врач"')
#     result = cur.fetchall()
#     print(result,sep='/n')
# # prosmort_table2()

# def prosmort_table3():
#     cur.execute('SELECT id,fio_klienta,data_r,age,login FROM table3')
#     result = cur.fetchall()
#     print(result,sep='/n')

# # prosmort_table3()

	
# def dobavit_table4(data_priema,fio_klienta ,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll):
#     summa_itog = stoimost_uslugi * koll
#     cur.execute('INSERT INTO table4 (data_priema,fio_klienta ,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll,summa_itog) VALUES(?,?,?,?,?,?,?,?) ',[data_priema,fio_klienta ,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll,summa_itog]) 
#     print("Запись успешно добавлена")
#     db.commit()
#     db.close()
# # 1	23.12.2003	Аня Т	Никита Ш 10001	Замена	1000	1	1000
# # 2	15.04.2003	Анаит Т	Мария Л	Регистрация	2000	1	2000
# # 3	14.05.2003	Коля К	Игорь_С	Палировка	3000	1	3000
# # 4	13.12.2003	Егор Б	Арина С	Чистка	4000	1	4000
# # 5	12.01.2003	Базаров Д	Саша С	Удаление записей	5000	1	5000
# # 6	2	1	3	4	5	6	30

# def dobavit():
#     fio = input('fio:')
#     kto = (input('kto:'))
#     parol = int(input('parol:'))
#     kto = kto.upper()
#     if kto == 'ADMIN' or 'АДМИН':
#         print('')
#     cur.execute('INSERT INTO table1 (fio,kto,parol) VALUES(?,?,?) ',[fio,kto,parol]) 
#     print("Запись успешно добавлена")
#     db.commit()
#     db.close()
# # # Добавляем 
# # id_d = input('Введите ФИО')
# # ss = input('dsd;')
# # cursor.execute('DELETE FROM pat WHERE fio = ?',(srh,))
# def delete(table,argument,chtodel):
#     # prosmort_table4()
#     sql_delete = (f'DELETE from {table} where {argument} = {chtodel}')
#     cur.execute(sql_delete)
#     db.commit()
#     print("Запись успешно удалена")
#     db.close()
# # delete()

# def delete_table4(argument,chto_delete):
#     sql_delete = (f'DELETE from table3 where {argument} = {chto_delete}')
#     cur.execute(sql_delete)
#     db.commit()
#     print("Запись успешно удалена")
#     db.close()

# def delete_table42(kod_vracha):
#     sql_delete = (f'DELETE from table4 where kod_vracha = {kod_vracha}')
#     cur.execute(sql_delete)
#     db.commit()
#     print("Запись успешно удалена")
#     db.close()
# # delete_table4('login',123)
# # 1	10001	F	a	g
# # 2	10002	a	s	s
# # 3	10003	s	g	f
# # 4	10004	f	h	s
# # 5	10005	g	h	a
# def delete_table2(kod_vracha):
#     sql_delete = (f'DELETE from table2 where kod_vracha = {kod_vracha}')
#     cur.execute(sql_delete)
#     db.commit()
#     print("Запись успешно удалена")
#     db.close()
# # delete_table2('kod_vracha','g')
# #         Выбрать *(всё) Где  и название
# def prosmort_table4():
#     cur.execute('SELECT * FROM table4')
#     result = cur.fetchall()
#     print(result)
# # prosmort_table4()

# def prosmort5(x2):
#     cur.execute(f'SELECT data_priema,fio_klienta,usluga,stoimost_uslugi,koll,summa_itog FROM table4 WHERE fio_klienta = {x2}' )
#     result = cur.fetchall()
#     print(result)


# def prosmort_tovara():
#     cur.execute(f'SELECT name FROM table6')
#     result = cur.fetchall()
#     cur.execute(f'SELECT price FROM table6')
#     result1 = cur.fetchall()
#     for i in range(len(result)):
#         print("Название товара:",result[i]," Цена товара:",result1[i])
#     return(result)

# def dobavit_tovara(name,price):
#         cur.execute('INSERT INTO table6 (name, price) VALUES(?,?) ',[name,price]) 
#         print("Запись успешно добавлена")
#         db.commit()

# def delete_tovara(name):
#     sql_delete = (f'DELETE from table6 where name = "{name}"')
#     cur.execute(sql_delete)
#     db.commit()
#     print("Запись успешно удалена")

# def delete_sotrudnik(login):
#     sql_delete = (f'DELETE from table1 where login = "{login}"')
#     cur.execute(sql_delete)
#     db.commit()
#     print("Сотрудник удален")


# def dobavit_sotrudnika(login,parol):
#         cur.execute('INSERT INTO table1 (login,parol,kto_v_bd) VALUES(?,?,?) ',[login,parol,'KONSUL']) 
#         print("Запись успешно добавлена")
#         db.commit()

# def prosmort_sotrudnikov():
#     cur.execute(f'SELECT login FROM table1 WHERE kto_v_bd = "PRODAVEC"' )
#     result = cur.fetchall()

#     for i in range(len(result)):
#             x = result[i]
#             x2 = (str(x)[1:-2])
#             print("Ваши продавцы",x2)
#     cur.execute(f'SELECT login FROM table1 WHERE kto_v_bd = "KONSUL"' )
#     time.sleep(5)
#     for i in range(len(result)):
#             x = result[i]
#             x2 = (str(x)[1:-2])
#             print("Ваши Консультанты",x2)




# def prosmort3_1(login):
#     cur.execute(f'SELECT * FROM table2 WHERE login = "{login}"' )
#     result = cur.fetchall()
#     return(result)

# def prosmort4_1(login):
#     cur.execute(f'SELECT kod_vracha FROM table2 WHERE login = "{login}"' )
#     result = cur.fetchall()
#     print(result)
#     return(result)

# # prosmort4_1('kng123123')

# def prosmort5_1(x2):
#     cur.execute(f'SELECT data_priema,fio_klienta,usluga,stoimost_uslugi,koll,summa_itog FROM table4 WHERE kod_vracha = {x2}' )
#     result = cur.fetchall()
#     print(result)

# # prosmort5_1('10003')

# def prosmort3(login): 
#     cur.execute(f'SELECT * FROM table3 WHERE login = "{login}"' )
#     result = cur.fetchall()
#     print(result)
#     return(result)
#     # cur.close() 

# # prosmort3('kng33')

# def prosmort1(login):
#     cur.execute(f'SELECT kto_v_bd FROM table1 WHERE login = "{login}"' )
#     result = cur.fetchall()
#     # print('Вы вошли как',result)
#     return(result)
#     # cur.close() 

# def prosmort4(login):
#     cur.execute(f'SELECT fio_klienta FROM table3 WHERE login = "{login}"' )
#     result = cur.fetchall()
#     # print(result)
#     return(result)

# # prosmort4("kng33")

# def zamena():
#         cho = input('Что заменить;')
#         koll= input('На что заменить:')
#         kak = input('Как найти:')
#         x = input('Уникальный способ нахождения:')
#         sql_update_query = (f'Update table1 set {cho} = {koll} where {kak} = {x}')
#         cur.execute(sql_update_query)
#         db.commit()
#         print("Запись успешно обновлена")
#         db.close()

def login(login,parol):
    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM logins WHERE login="{login}";')
    value = cur.fetchall()
    if value != [] and value[0][2] == parol:
        print('Успешная авторизация!')
        return(1)
    else:
        print('Проверьте правильность ввода данных!')
        return(2)

lvl = '1'	
x2 = 13
def pozdarvPol(x2,lvl):
            cur.execute(f'SELECT name FROM main WHERE shagi = {x2} AND lvl = "{lvl}" ')
            result = cur.fetchall()
            print(result)
pozdarvPol(x2,lvl)
# # login('kng',123)


# def prosmort_G_vrach1():
#     cur.execute(f'SELECT fio_vracha,doljnost,kod_vracha,id FROM table2')
#     result = cur.fetchall()
#     print(result)

# # prosmort_G_vrach1()
# def prosmort_G_vrach2():
#     cur.execute(f'SELECT fio_klienta,data_r,age,id FROM table3')
#     result = cur.fetchall()
#     print(result)

# def prosmort_G_vrach3():
#     cur.execute('SELECT * FROM table4')
#     result = cur.fetchall()
#     print(result)

# def prosmort_G_vrach_Uslugi():
#     cur.execute('SELECT nazvanie_uslugi,stoimost_uslugi FROM table5')
#     result = cur.fetchall()
#     print('Название/Цена',result)

# # prosmort_G_vrach_Uslugi()


def register(login,parol):
    cur.execute(f'SELECT * FROM logins WHERE login="{login}";')
    parol = str(parol)
    parol2 = len(parol)
    value = cur.fetchall()
    if value != []:
        print('Такой логин уже разегестрирован')
        return(1)
        
    elif value == []:

                
                # fio_klienta = input('Ваша Фамилия:')
                # data_r = input('Дата (гггг-мм-дд): ')
                # age = data_r
                # age = age.split('-')
                # aa = datetime.date(int(age[0]),int(age[1]),int(age[2]))
                # bb = datetime.date.today()
                # cc = bb-aa

                cur.execute(f"INSERT INTO logins (login, parol) VALUES ('{login}', '{parol}')")
                print('Вы успешно зарегистрированы!')
                db.commit()

                # cur.execute(f"INSERT INTO table3 (login,fio_klienta,data_r,age) VALUES ('{login}','{fio_klienta}','{data_r}','{age}')")
                # db.commit()
                # break
# def register2(login,fio_klienta,data_r):
#     age = data_r
#     age = age.split('.')
#     aa = datetime.date(int(age[2]),int(age[1]),int(age[0]))
#     bb = datetime.date.today()
#     cc = bb-aa
#     x = (cc) / 365
#     x1 = str(x)
#     age = (x1.split()[0])
#     cur.execute(f"INSERT INTO table3 (login,fio_klienta,data_r,age) VALUES ('{login}','{fio_klienta}','{data_r}','{age}')")
#     db.commit()

       




# # def register2(login,fio_klienta,data_r,age):
# #         cur.execute(f"INSERT INTO table3 (login,fio_klienta,data_r,age) VALUES ('{login}','{fio_klienta}','{data_r}','{age}')")
# #         print('Вы успешно зарегистрированы!')
# #         db.commit()

# #         cur.close()

# def zapis(data_priema,fio_klienta,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll,summa_itog):
#     cur.execute('INSERT INTO table4 (data_priema,fio_klienta,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll,summa_itog) VALUES(?,?,?,?,?,?,?,?) ',[data_priema,fio_klienta,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll,summa_itog]) 
#     print("Запись успешно добавлена")
#     db.commit()
#     db.close()



# # from datetime import date
# # today = date.today()

# # def get_age():
# #     d= int(e1.get())
# #     m=int(e2.get())
# #     y=int(e3.get())
# #     age = today.year-y-((today.month, today.day)<(m,d))
# #     print(age)

# # get_age()

# # def dobavit_klienta():
    
# # zamena()
# # db.close()
# import datetime
# import time
 
# # def db(d1, d2):
# #     date_format = "%m/%Y"
# #     delta = datetime.datetime.strptime(d2, date_format) - datetime.datetime.strptime(d1, date_format)
# #     return delta.days / 365.245

#     # print(x.split()[0])

# # def klient(login):
# #     m = prosmort1(login)
# #     if m == [('KLIENT',)]:
# #         print('Ваши права Ограничиваются на Просмотре')
# #         time.sleep(1)
# #         print('Добавить или же Удалить запись может лишь Регистратура')
# #         time.sleep(1)
# #         print(' Id / Fio / Data_R/ Age / Login')
# #         time.sleep(1)
# #         prosmort3(login)
# #         x = prosmort4(login)
# #         l = (''.join(map(str,x )))
# #         x2 = (str(l)[1:-2])
# #                 # print(x2)
# #         print(' Data / fio / usluga / summa / koll / itog_summa')
# #         prosmort5(x2)
# # nazvanie_uslugi 
# # stoimost_uslugi
# def dobavit_uslugu(nazvanie_uslugi,stoimost_uslugi):
#     # nazvanie_uslugi = input('Название услуги которую вы хотите добавить:')
#     # stoimost_uslugi = int(input('Стоимость услуги'))
#     cur.execute('INSERT INTO table5 (nazvanie_uslugi,stoimost_uslugi) VALUES(?,?) ',[nazvanie_uslugi,stoimost_uslugi]) 
#     print("Запись успешно добавлена")
#     db.commit()
#     db.close

# def delete_uslugi(nazvanie_uslugi):
#     sql_delete = (f'DELETE from table5 where nazvanie_uslugi = "{nazvanie_uslugi}"')
#     cur.execute(sql_delete)
#     db.commit()
#     print("Запись успешно удалена")
#     db.close()
# # dobavit_uslugu('Чистака',500)
# # dobavit_uslugu()
# # kod_vracha
# # fio_vracha
# # doljnost
# # login


# # kod_vracha fio_vracha doljnost login
# def dobavit_vracha(kod_vracha,fio_vracha,doljnost,login):
#     cur.execute('INSERT INTO table2 (kod_vracha,fio_vracha,doljnost,login) VALUES(?,?,?,?) ',[kod_vracha,fio_vracha,doljnost,login]) 
#     print("Запись успешно добавлена")
#     db.commit()
#     db.close
# # dobavit_vracha(10001,'нИкитаШ','Должность','Аа')

def proverkalogin(login):
    cur.execute(f'SELECT * FROM logins WHERE login="{login}";') 
    value = cur.fetchall()
    if value != []:
        print('Такой ник уже используется!')
        return(1)
    elif value == []:
        return(2)


# # proverkalogin('kng33')
# # register('kng33',123)
# # dobavit_vracha()


# # x = prosmort4('kng33')
# # l = (''.join(map(str,x )))
# # x2 = (str(l)[1:-2])
# # print(x2)
# # print(' Data / fio / usluga / summa / koll / itog_summa')
# # prosmort5(x2)

# def age(tablerow):
#     cur.execute(f'SELECT age FROM table3 WHERE id = {tablerow}')
#     result = cur.fetchall()
#     x = result
#     l = (''.join(map(str,x)))
#     x2 = (str(l)[1:-2])

#     return(x2)
#     # cur.execute('SELECT * FROM table4')
#     # result = cur.fetchall()
#     # print(result)

# def koll(tablerow):
#     cur.execute(f'SELECT stoimost_uslugi FROM table5 WHERE id = {tablerow}')
#     result = cur.fetchall()
#     x = result
#     l = (''.join(map(str,x)))
#     x2 = (str(l)[1:-2])

#     return(x2)


# def koll2(tablerow):
#     cur.execute(f'SELECT koll FROM table4 WHERE id = {tablerow}')
#     result = cur.fetchall()
#     x = result
#     l = (''.join(map(str,x)))
#     x2 = (str(l)[1:-2])

#     return(x2)

# def parol(tablerow):
#     cur.execute(f'SELECT parol FROM table1 WHERE id = {tablerow}')
#     result = cur.fetchall()
#     x = result
#     l = (''.join(map(str,x)))
#     x2 = (str(l)[1:-2])

#     return(x2)

# def kod(tablerow):
#     cur.execute(f'SELECT kod_vracha FROM table2 WHERE id = {tablerow}')
#     result = cur.fetchall()
#     x = result
#     l = (''.join(map(str,x)))
#     x2 = (str(l)[1:-2])

#     return(x2)


# # age(3)
