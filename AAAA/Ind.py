
import sql1
import sqlite3
# import parol
import datetime
import time
db = sqlite3.connect('sql_10.db')
cur = db.cursor()

# # Kto = input('Вы гость или админ?')
# # Kto = Kto.upper()

# def admin():
#     Kto = input('Вы гость или админ?')
#     Kto = Kto.upper()
#     if Kto == 'АДМИН' or Kto == 'ADMIN' or Kto == 'FLVBY':
#         vvod = int(input('Введите пароль:'))
#         if vvod == parol.parol:
#             print('     -Верный пароль-')
#         # Даём доступ уровня админ 
#             zapros = input('Что вы хотите?. Добавить/Удалить/Посмотреть/Замена (Запись/записи):')
#             zapros = zapros.upper()
#             if zapros == 'ДОБАВИТЬ' or zapros == 'LJ,FDBNM':
#                 sql1.dobavit()
# # Удаляем
#             if zapros == 'УДАЛИТЬ' or zapros == 'ELFKBNM':
#                 table1 = input('Таблица название:')
#                 argument = input('Аргумент название:')
#                 chto_delete = input('Уникальное значение название:')
#                 sql1.delete(table1,argument,chto_delete)
# # Смотри
#             if zapros == 'ПОСМОТРЕТЬ' or zapros == 'GJCVJNHTNM':
#                 kakoy_table = input('Какую таблицу хочешь посмотреть? table1/table2/Все;')
#                 if kakoy_table == 'table1':
#                     sql1.prosmort1()
#                 elif kakoy_table == 'table2':
#                     sql1.prosmort2()
#                 elif kakoy_table == 'Все':
#                     print('Первая таблица')
#                     sql1.prosmort1()
#                     print('Вторая таблица')
#                     sql1.prosmort2()
#             else:
#                     print('Neverno')
# # Заменяем
#             if zapros == 'ЗАМЕНА' or zapros == 'PFVTYF':
#                 sql1.zamena()
#             else:
#                 print('')
#         else:
#             print('          -Неверный пароль-')
# def vrach():
#     Kto = input('Вы гость или админ?')
#     Kto = Kto.upper()
#     if Kto == 'ВРАЧ' or Kto == 'DHFX' or Kto == 'VRACH':
#         zapros1 = input('Что вы хотите?:')
#         zapros1 == 'ЗАПИСАТЬ НА ПРИЁМ' or 'PFGBCFNM YF GHB`V'
#         data_priema = input('Дата приёма через . ;')
#         fio_klienta = input('Фио клиента;')
#         fio_vracha = input('Фио врача;')
#         usluga = input('Услуга;')
#         stoimost_uslugi = int(input('Стоимость;'))
#         koll = int(input('Колличество услуг;'))
#         summa_itog = (stoimost_uslugi) * (koll)
#         sql1.zapis(data_priema,fio_klienta,fio_vracha,usluga,stoimost_uslugi,koll,summa_itog)



# def klient():
#     Kto = input('Вы гость или админ?')
#     Kto = Kto.upper()
#     if Kto == 'КЛИЕНТ'or Kto == 'RKBTYN' or Kto == 'KLIENT':
#         sql1.prosmort2()



# vrach()
# vrach()
# klient()

# db = sqlite3.connect('sql_10.db')
# cur = db.cursor()


# login = input('Введите login:')
# while True:
#     parol = (input('Пароль(Минимум 6 символов):'))
#     parol2 = len(parol)
#     if parol2 >= 6:
#         print('зарегистрированно')
#         break
#     else:
#         print('Пароль Меньше 6 символов введите другой')

# sql1.register(login,parol)



# 3 Попытки входа 
for i in range(0,3):
    vhod = input('Вход или Регистрация?:')
    # Запрос на вход или РЕГ
    vhod = vhod.upper()
    # Защита от дурака(тебя) (ОТ ОШИБОК)
    if vhod == 'ВХОД' or vhod == 'D[JL' or vhod == 'VHOD': 
        # Так же 3 ввода (Надо для sql защиты(sql защиту просит препод))
        for i in range(3):
            login = str(input('Введите login:'))
            parol = (int(input('Пароль(Минимум 6 символов):')))
            # Логин пароль 
            output = sql1.login(login,parol)
            # Запуск функции (И возращаем ответ через ретёрн)
            # Даём функции имя что бы её ответ можно было использовать
            if output == 1:
                # 1 = Правильный ввод логина пароля
                m = sql1.prosmort1(login)
                #  Функция ответ на вопрос кто ты в Бд
                # [('KLIENT',)]  = Пример ответа Функции на вопрос кто ты? (Автоматизираванно)
                if m == [('KLIENT',)]:
                    print('Ваши права Ограничиваются на Просмотре')
                    time.sleep(1)
                    # Сон на 1 секунду для Внешнего вида
                    print('Добавить или же Удалить запись может лишь Регистратура')

                    time.sleep(1)
                    # Сон на 1 секунду для Внешнего вида
                    print(' Id / Fio / Data_R / Age / Login')
                    time.sleep(1)
                    # Сон на 1 секунду для Внешнего вида
                    sql1.prosmort3(login)
                    # (' Id / Fio / Data_R / Age / Login') Из Базы данных (Функция даёт ответ относительно логина, именно поэтому и предаётся логин)
                    x = sql1.prosmort4(login)
                    # Тоже саммое но ответ из другой таблицы
                    l = (''.join(map(str,x)))
                    x2 = (str(l)[1:-2])
                    # Для корекции вида ответа (Превращаем ответ из списка в строку )
                    # print(x2)
                    print(' Data / fio / usluga / summa / koll / itog_summa')
                    # Функция отвечает за вывод ' Data / fio / usluga / summa / koll / itog_summa'
                    sql1.prosmort5(x2)
                    break
                    # Брейк так как у нас 3 Попытки входа если его не включить то после всей операции челове будет входить ещё 3 раза(Не безопасно)

                elif m == [('REGISTER',)]:
                    chto_1 = input('Удалить запись/Записаться/Посмотреть записи:')
                    if chto_1 == 'Удалить запись':#Поставить обход ошибок
                        argument = input('argument:')
                        chto_delete = input('chto_delete:')
                        sql1.delete_table4(argument,chto_delete)

                    elif chto_1 == 'Записаться':#Поставить обход ошибок
                            now = datetime.datetime.now()
                            print(now.strftime("%d-%m-%Y %H:%M"))
                            data_priema = input('Дата приёма через - ;')
                            sql1.prosmort_table3()
                            fio_klienta = input('Фио клиента;')
                            sql1.prosmort_table2()
                            fio_vracha = input('Фио врача;')
                            kod_vracha = input('Код Врача:')
                            sql1.prosmort_table5()
                            usluga = input('Услуга;')
                            stoimost_uslugi = int(input('Стоимость;'))
                            koll = int(input('Колличество услуг;'))
                            summa_itog = (stoimost_uslugi) * (koll)
                            sql1.zapis(data_priema,fio_klienta,fio_vracha,kod_vracha,usluga,stoimost_uslugi,koll,summa_itog)

                    elif chto_1 == 'Посмотреть записи':#Поставить обход ошибок
                        sql1.prosmort()
                    else:
                        print('Зациклить')
                    
                elif m == [('G-VRACH',)]:
                    print('1')
                    chto_1 = input('Удалить врача/Записать врача/Посмотреть Врачей/ Посмотреть Клиетов/ Посмотреть Записи/Услуги:')
                    if chto_1 == 'Удалить врача':#Поставить обход ошибок
                        argument = input('argument:')
                        chto_delete = input('chto_delete:')
                        sql1.delete_table4(argument,chto_delete)
                    elif chto_1 == 'Добавить врача':
                        sql1.dobavit_vracha()
                    elif chto_1 == 'Посмотреть врачей':
                        sql1.prosmort_G_vrach1()
                    elif chto_1 == 'Посмотреть клиентов':
                        sql1.prosmort_G_vrach2()
                    elif chto_1 == 'Посмотреть записи':
                        sql1.prosmort_G_vrach3()
                    elif chto_1 == 'Услуги': 
                            chto_2 = input('Что делать? Посмотреть/Добавить/Удалить?')
                            if chto_2 == 'Посмотреть':
                                sql1.prosmort_G_vrach_Uslugi()
                            elif chto_2 == 'Добавить':
                                    nazvanie_uslugi = input('Название услуги которую вы хотите добавить:')
                                    stoimost_uslugi = int(input('Стоимость услуги:'))
                                    sql1.dobavit_uslugu(nazvanie_uslugi,stoimost_uslugi)
                            elif chto_2 == 'Удалить':
                                nazvanie_uslugi = input('Название услуги которую вы хотите удалить:')
                                sql1.delete_uslugi(nazvanie_uslugi)
                    
                    
            
                elif m == [('VRACH',)]:
                        print('Ваши права Ограничиваются на Просмотре')
                        sql1.prosmort3_1(login)
                        x = sql1.prosmort4_1(login)
                        l = (''.join(map(str,x )))
                        x2 = ((l)[1:-2])
                        # print(x2)
                        # print(' Data / fio / usluga / summa / koll / itog_summa')
                        sql1.prosmort5_1(x2)

                    
                
                elif m == [('ADMIN',)]:
                    print('5')
        else:
            print('')
    
    if vhod == 'HTUBCNHFWBZ' or vhod == 'REGISTACIA' or vhod == 'РЕГИСТРАЦИЯ':
        login = input('Введите login:')
        sql1.register(login)
        break
        




        #  while True:
        #     parol = (input('Пароль(Минимум 6 символов):'))
        #     parol2 = len(parol)
        #     if parol2 >= 6:
        #         sql1.register(login)
                # print('зарегистрированно')
                # print('Вы успешно зарегистрированы!')
                # fio_klienta = input('Ваша Фамилия:')
                # data_r = input('Дата (гггг-мм-дд): ')
                # a = data_r
                # a = a.split('-')
                # aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
                # bb = datetime.date.today()
                # cc = bb-aa

                # x = (cc) / 365
                # x1 = str(x)
                # age = x1
                # sql1.register2(login,fio_klienta,data_r,age)

                # age = (x1.split()[0])
                # age = 17
                # # sql1.register(login,parol,fio_klienta,data_r,age)

                # break
            # else:
            #     print('Пароль Меньше 6 символов введите другой')



# sql1.register('asd','parol','asd','data_r','age')