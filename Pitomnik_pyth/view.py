import text
from typing import List
from model import DataBase_Pitomnik
from datetime import datetime

animal_id=''
class_animal=''

def main_menu()->int:
    for n, item in enumerate(text.main_menu):
        if n==0:
            print(item)
        else:
            print(f'\t{n}.{item}')

    while True:
        choice=input(text.main_menu_choice) 
        print(choice)  
        if choice.isdigit() and 0<int(choice)<len(text.main_menu):
            return int(choice)
        print(f'введите пункт меню от 1 до {len(text.main_menu)-1}')


def print_massege(massege:str):
    
    print('\n'+'='*len(massege))  
    print(massege)       
    print('='*len(massege)+'\n')           

    

def table_print(tabl_MySQL:DataBase_Pitomnik,n,array):
    stolbsi=[]*n
    table =[[stolbsi[i] for i in array] for (stolbsi) in tabl_MySQL]
    for i in table:
        for j in i:
            print(j,end="  ")
        print()        


def show_class_animals(pitomnik: DataBase_Pitomnik,query:str,error:int):
    global class_animal
    if error:
        return error
    class_animal=input(text.class_animal+'\n')
    if class_animal not in ['1','2']:
        return 2
    pitomnik.query_MySQL(query,[class_animal])
    table_print(pitomnik.cursor,3,[0,1])
    return None
  

def validation_id(pitomnik: DataBase_Pitomnik,query:str,id:str):
    array=[]
    pitomnik.query_MySQL(query,[id]) 
    for a in pitomnik.cursor:
        array.append(a[0])
    print(array)
    if int(animal_id) in array:
        return None
    else:
        return  2  


def show_id_animals(pitomnik: DataBase_Pitomnik,query:str,error:int):
    
    global animal_id
    if error:
        return error
   
    animal_id=input(text.id_animal)
    return validation_id(pitomnik,query,animal_id)
        

    
def show_animal_comands(pitomnik: DataBase_Pitomnik,query:str,error:int):  
    global animal_id
    if error:
        return error
    pitomnik.query_MySQL(query,[animal_id])
    
    table_print(pitomnik.cursor,3,[0,1,2]) 
    return None


def add_animal_command(pitomnik: DataBase_Pitomnik,query:str,error:int):
    global animal_id
    if error:
        return error
    command=input(text.animal_use_command).capitalize()
    pitomnik.query_MySQL_into(query,[command,animal_id])
    pitomnik.save_change()
    return 0
    

def dell_animal_command(pitomnik: DataBase_Pitomnik,query:str,error:int):
    if error:
        return error
    id_command=input(text.id_command)
    pitomnik.query_MySQL(query,[id_command])
    pitomnik.save_change()
    return 1


    

def add_animal(pitomnik: DataBase_Pitomnik,message:List[str],query:str,error:int):
    animal_card=['','','']
    if error:
        return error
    for i,mes in enumerate(message):
        text=''
        while not text: 
            text=input(mes)    
        if i==1:
            try:
                datetime.strptime(text, '%Y-%m-%d')
            except ValueError:
                return 3
        animal_card[i]=text if text else animal_card[i]
    
    animal_card[2]=class_animal
    pitomnik.query_MySQL(query,animal_card)
    #print(animal_card)
    #pitomnik.query_MySQL_into(query,animal_card)
    
    pitomnik.save_change()
    return 1


    
def dell_animal(pitomnik: DataBase_Pitomnik,query:str,query_comands:str,error:int):
    if error:
        return error
    
    pitomnik.query_MySQL(query,[animal_id])
    pitomnik.save_change()

    pitomnik.query_MySQL(query_comands,[animal_id])
    pitomnik.save_change()
    return 1
    



def show_full_animal(pitomnik: DataBase_Pitomnik, error_massege: str ):
    pitomnik.query_MySQL(text.full_animal)
    table_print(pitomnik.cursor,4,[0,1,2,3])
    if pitomnik.cursor.rowcount>0:
        return None
    else:
        return 5
   


