import FreeSimpleGUI as sg
import functions
import time
import os
if not os.path.exists("todo.txt"):
    with open("todo.txt","w"):
        pass
label = sg.Text("Enter a Todo")
todo_input = sg.InputText(tooltip="Enter a Todo", key="todo")
button = sg.Button("Add")
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")
clock = sg.Text("",key="time")
list_box = sg. Listbox(values=functions.read_todo(),size=(45,15),key="todos")
window = sg.Window("MY TODO LIST",layout=[[clock],[label],[todo_input , button],[list_box,edit_button,delete_button],[exit_button]])
while True:
    event,value = window.read(timeout=200)
    window["time"].update(value=time.strftime("%d %b %Y %H:%M:%S %p"))
    print(event)
    print(value["todo"])
    match event:
        case "Add":
            todos=functions.read_todo()
            new_todo = value["todo"]+"\n"
            todos.append(new_todo)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            todos = functions.read_todo()
            todo_to_edit = value["todos"][0]
            index = todos.index(todo_to_edit)
            todos[index] = value["todo"] + "\n"
            functions.write_todo(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Delete":
            todos = functions.read_todo()
            todo_to_delete = value["todos"][0]
            todos.remove(todo_to_delete)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case sg.WINDOW_CLOSED:
            break