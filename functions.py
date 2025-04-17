def read_todo(filename="todo.txt"):
    with open(filename,"r") as file:
            todos = file.readlines()
            return todos
def write_todo(todos,filename="todo.txt"):
    with open(filename, "w") as file:
            file.writelines(todos)
if __name__ == "__main__":
    print(read_todo())
    print("function is working properly")