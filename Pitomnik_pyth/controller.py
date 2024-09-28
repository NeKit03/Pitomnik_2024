import text
import view
import model


def strart_app():
    pitomnik=model.DataBase_Pitomnik()
    while True:
        
        choice=view.main_menu()
        match choice:
            case 1:
                view.print_massege(text.list_error[view.show_full_animal(pitomnik,text.emty_pitomnik_animal)])
            case 2:
                view.print_massege(text.list_error[view.add_animal(pitomnik,text.new_animal,text.add_animal_into,
                    view.show_id_animals(
                        pitomnik,text.AnimalView_id_select,
                        view.show_class_animals(
                            pitomnik,text.AnimalView_group_id_select,None)))])
                #view.show_class_animals(pitomnik,text.AnimalView_group_id_select,None)
            case 3:
                view.print_massege(text.list_error[view.show_full_animal(pitomnik,text.emty_pitomnik_animal)])
                
                view.print_massege(text.list_error[
                        view.dell_animal(pitomnik, text.delete_animal,text.delete_animal_and_comands,
                            view.show_id_animals(pitomnik,text.animal_id_select,None))])
            case 4:
                view.print_massege(text.list_error[view.show_full_animal(pitomnik,text.emty_pitomnik_animal)])
                view.print_massege(text.list_error[
                    view.show_animal_comands(pitomnik,text.animal_command,
                        view.show_id_animals(pitomnik,text.animal_id_select,None))])
            case 5:
                view.print_massege(text.list_error[view.show_full_animal(pitomnik,text.emty_pitomnik_animal)])
                
                view.print_massege(text.list_error[
                    view.add_animal_command(pitomnik,text.add_comand_animal_into,
                        view.show_id_animals(pitomnik,text.animal_id_select,None))])

            case 6:
                view.print_massege(text.list_error[view.show_full_animal(pitomnik,text.emty_pitomnik_animal)])
                
                view.print_massege(text.list_error[
                    view.dell_animal_command(pitomnik,text.delete_comand_animal,
                        view.show_animal_comands(pitomnik,text.animal_command,
                            view.show_id_animals(pitomnik,text.animal_id_select,None)))])

            case 7:
                view.print_massege(text.good_bay)   
                break 
                


