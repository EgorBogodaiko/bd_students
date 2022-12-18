import ui
import show_bd as show
import search_rows as search
import constants
db_name = constants.DATA_BASE_NAME
import delete_row as d
import edit_row as edit
action = ''
while action != '6':
    action = ui.get_action()
    if action == '1': show.show_all_bd(db_name) # Готово, работает
    if action == '2': 
        f,v=ui.get_field_n_value()
        search.search(db_name,f,v,1)
    if action == '3':
        f,v=ui.get_field_n_value()
        print('Найдены следующие элементы по этим критериям:')
        search.search(db_name,f,v,1)
        decision=ui.agree()
        if decision == True:
            d.delete_row(db_name,search.search(db_name,f,v,2))
    if action == '4':
        ui.add_row()
    if action == '5':
        print('Для начала найдём строку')
        f,v=list(ui.get_field_n_value())
        print('Найдены следующие элементы по этим критериям:')
        search.search(db_name,f,v,1)
        mod_row=ui.row_to_modify(search(db_name,f,v,2))
        field_to_correct=ui.field_to_correct(db_name,mod_row)
        new_value=ui.to_input()
        edit.modify_row(db_name,mod_row,field_to_correct, new_value)
print('Работа завершена.')