import ui
import show_bd as show
import search_rows as search
import constants
db_name = constants.DATA_BASE_NAME
import delete_row as d
import edit_row as edit
import add_row as add
def start_bd_controler():
    action = ''
    while action != '6':
        action = ui.get_action()
        if action == '1': show.show_all_bd(db_name) # Готово, работает
        if action == '2':                           # Готово, работает
            f,v=ui.get_field_n_value()
            search.search(db_name,f,v,1)
        if action == '3':                           # Готово, работает
            f,v=ui.get_field_n_value()
            print('Найдены следующие элементы по этим критериям:')
            del_list= search.search(db_name,f,v,2)
            decision=ui.agree(list)
            if decision == True:
                d.delete_row(db_name,del_list)
            else:
                print('Хорошо, удалять не будем')
        if action == '4':                           # Не написана, пишет Константин, Марина, Мариана
            add.add_row(db_name)
        if action == '5':                           # Готово, работает
            id_row=ui.get_id(db_name)                          
            f,v=ui.get_field_n_value()                     
            edit.modify_row(db_name,id_row,f, v)
    print('Работа завершена.')