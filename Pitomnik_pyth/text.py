main_menu=['главное меню',
           'Вывести всех животных приюта',
           'Добавить животное в приют',
           'Удалить животное из приюта',
           'Вывести все команды животного',
           'Обучить животное новой команде',
           'Удалить у животного команду',
           'Выход',
           ]

main_menu_choice='Выберите пункт меню: '

error_pitomnik_animal=[
    'В питомнике нет животных!',
    'Не верный id животного!'
]

class_animal='Введите класс животного:\n1)Вьючное животное\n2)Домашнее животное'
new_animal=[
    'введите кличку животного: ',
    'введите дату рождения в формате YYYY-MM-DD: '
]


list_error={0:'Успешно',
               1: 'Данные успешно изменены!',
                2:'Введен не корректный ключь!\n Попробуйте снова)',
               3: 'Дата введена некорректно. \nПопробуйте еще раз!',
                4:'Команда уже разучена!',
                5:'Пусто!',
               6: '',
               None:''
}


good_bay='До новых встреч!'
emty_pitomnik_animal='В питомнике нет животных!'

delete_comand_animal='DELETE FROM Comands WHERE id=%s'
delete_animal='DELETE FROM Animals_of_the_nursery WHERE id=%s'
delete_animal_and_comands='DELETE FROM Comands WHERE id_animal=%s'
AnimalView_group_id_select = "SELECT * FROM AnimalView WHERE group_id=%s"

add_animal_into='INSERT INTO Animals_of_the_nursery(name,birthDate,view_id) VALUES(%s, %s, %s)'
add_comand_animal_into='INSERT INTO Comands(command,id_animal) VALUES(%s, %s)'
AnimalView_id_select = "SELECT * FROM AnimalView WHERE id=%s"
animal_id_select = "SELECT * FROM Animals_of_the_nursery WHERE id=%s"
full_animal="SELECT * FROM Animals_of_the_nursery"
animal_command="SELECT * FROM Comands WHERE id_animal=%s"

id_animal='введите id животного: '
animal_use_command='Выше перечисленные команды животное уже знает\n введите новую команду:\n'
id_command='Введите id команды: \n'

def new_animal_add_successful(name:str)->str:
    return f'Животное {name} успешно добавлено!'