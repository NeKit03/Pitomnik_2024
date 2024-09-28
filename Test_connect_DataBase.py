import mysql.connector
import sqlite3
from datetime import datetime
cursor = None
cursor1 = None
AnimalViewId=[]
cnx = None  
animal_select = "SELECT id FROM Animals_of_the_nursery WHERE id=%s"

def validate_input_animal_id(n):
    if not cursor.execute(animal_select,[n]):
        return 
    else: 
        return 1


def id_animal():
    animal=input('введите id животного: ')
    if validate_input_animal_id(animal):
        return animal
    else:
        return  

def check_connection():
    global cursor, cnx
    try:
        cnx = mysql.connector.connect(user='nikita', password='217455', host='localhost', port=3307, database='humanfriends')
        cursor = cnx.cursor()
        print("Connection successful!")
        return True
    except mysql.connector.Error as err:
        print("Failed to connect to MySQL: {}".format(err))
        return False

def FULL_animal():
    global cursor
    query = "SELECT * FROM Animals_of_the_nursery"
    cursor.execute(query)
    table_print(4,[0,1,2,3],cursor)
    return 0
    #for (id,name, birthDate, view_id ) in cursor:
    #    print(id,name, birthDate, view_id)

def add_animal():
    global cursor
    AnimalView_id_select = "SELECT * FROM AnimalView WHERE id=%s"
    AnimalView_group_id_select = "SELECT * FROM AnimalView WHERE group_id=%s"
    add_animal_into='INSERT INTO Animals_of_the_nursery(name,birthDate,view_id) VALUES(%s, %s, %s)'
    
    print('Введите класс животного:','1)Вьючное животное','2)Домашнее животное',sep='\n')
    class_animal=input()
    
    if class_animal not in ['1','2']:
        return 1
       
    
    cursor.execute(AnimalView_group_id_select,[class_animal])
    table_print(3,[0,1],cursor)
    
    
    
    
    #for (id,name, group_id) in cursor:
    #    print(id,name, group_id)
    
    
    animal=input('Введите id животного:' )
    if cursor.execute(AnimalView_id_select,[animal]):
        return 1
    animal_name=input('введите кличку животного: ')
    animal_birthDate=input('введите дату рождения в формате YYYY-MM-DD: ')
    try:
        datetime.strptime(animal_birthDate, "%Y-%m-%d")
    except ValueError:
        return 2
    cursor.execute(add_animal_into,[animal_name,animal_birthDate,class_animal])
    cnx.commit()
    return 0

def dell_animal():
    FULL_animal()
    global cursor
    delete_animal='DELETE FROM Animals_of_the_nursery WHERE id=%s'
    #animal_select = "SELECT id FROM Animals_of_the_nursery WHERE id=%s"
    animal=input('введите id животного: ')
    if validate_input_animal_id(animal):
        cursor.execute(delete_animal,[animal])
        cnx.commit()
        return 0
    else:
        return 1    

def  animal_comands():
    global cursor
    FULL_animal()
    animal_select = "SELECT id FROM Animals_of_the_nursery WHERE id=%s"
    animal_id=input('Введите id животноко чьи команды вам интересны: ')
    query = "SELECT * FROM Comands WHERE id_animal=%s"
    if not cursor.execute(animal_select,[animal_id]):
        return 1
    cursor.execute(query,[animal_id])

    table_print(3,[0,1],cursor)
    return 0
    #for (id,comand, id_animal ) in cursor:
    #    print(id,comand)    

def add_comand_animal():
    global cursor
    FULL_animal()
    animal_select = "SELECT id FROM Animals_of_the_nursery WHERE id=%s"
    add_comand_animal_into='INSERT INTO Comands(command,id_animal) VALUES(%s, %s)'
    animal_id=input('Введите id животноко которого хотите обучить команде: ')
    if not cursor.execute(animal_select,[animal_id]):
        return 1
    comand_animal = "SELECT * FROM Comands WHERE id_animal=%s"

    cursor.execute(comand_animal,[animal_id])
    list_comands=[command for (id,command, id_animal) in cursor]
    print('Сейчас животное знает',len(list_comands),'команд: ')

    table_print(3,[1],cursor)

    #for i in list_comands:
    #    print(i)

    new_comand=input('Введите новую команду для животного: ')
    

    if new_comand.capitalize() in list_comands:
        return 3
    else:
        cursor.execute(add_comand_animal_into,[new_comand.capitalize(),animal_id])
        cnx.commit()
        cursor.execute(comand_animal,[animal_id])
        table_print(3,[0,1],cursor)
        
    return 0    

    

def table_print(n,array,cursor):
    stolbsi=[]*n
    table =[[stolbsi[i] for i in array] for (stolbsi) in cursor]
    for i in table:
        for j in i:
            print(j,end=" ")
        print()    



def del_comand_animal():
    FULL_animal()
    global cursor
    delete_comand='DELETE FROM Comands WHERE id=%s'
    comand_animal = "SELECT * FROM Comands WHERE id_animal=%s"
    animal_id=input('введите id животного который забыл команду: ')
    cursor.execute(comand_animal,[animal_id])
    table_print(3,[0,1],cursor)
    #for (id,command, id_animal) in cursor:
    #    print(id,command)
    comand=input('введите id команды: ')
    cursor.execute(delete_comand,[comand])
    cnx.commit()



def print_error(error):
    mx=max([int(len(i)) for i in error])+8
    print('='*mx,end="")
    print()
    for i in error:
        print('||',i+' '*(mx-6-len(i)),'||')
    print('='*mx,end="")    
    print()


def print_menu():
    print('===============MENU===============')
    print('1)Вывести всех животных приюта')
    print('2)Добавить животное в приют')
    print('3)Удалить животное из приюта')
    print('4)Вывести все команды животного')
    print('5)Обучить животное новой команде')
    print('6)Удалить у животного команду')
    print('9)table_print')
    print('0)EXIT')


def text_error(n):
    list_error=[['Данные успешно изменены!'],
                ['Введен не корректный ключь!','Попробуйте снова)'],
                ["Дата введена некорректно.",'Попробуйте еще раз'],
                ['Команда уже разучена!']
                ]
    return list_error[n]


def menu():
    print_menu()
    punkt=input()
    if punkt=='1':
        FULL_animal()
    elif punkt=='2':
        print_error(text_error(add_animal()))
    elif punkt=='3':
        print_error(text_error(dell_animal()))
    elif punkt=='4':
        print_error(text_error(animal_comands()))
    elif punkt=='5':
        print_error(text_error(add_comand_animal()))
    elif punkt=='6':
        del_comand_animal() 
    elif punkt=='9':
        table_print()           
    elif punkt=='0':
        exit() 
    else:
        print_error(text_error(1))      
def start():
    result = check_connection()
    if result:
        print("Connection test passed successfully.")
    else:
        print("Connection test failed.")
    while True :
        menu()

if __name__ == "__main__":  
    start()

    if cursor:
        cursor.close()
    if cnx:
        cnx.close()
