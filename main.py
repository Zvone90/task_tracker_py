from add_task import Add_task
import json
import os.path
from get_task_info import Get_task_info



my_json_file_name = 'task_list.json'

check_file = os.path.isfile(my_json_file_name)
#print(check_file)

if check_file == True :
    with open('task_list.json') as json_data:
        my_json = json.load(json_data)
        #print(json.dumps(my_json, indent=4))
else:
    my_json = {"content": []}

user_input = ""
select_menu = input("\nFor adding new tasks type:  new task\nFor updating a task type:   update\nFor list of task enter:     task list\n============================\n\n")

#add a new task
if select_menu == "new task":
    while user_input != "exit":
        print("Enter any new task with id, description, status")
        task = input(user_input)
        new_task = task.split(", ")

        add_new_task = Add_task(new_task[0], new_task[1], new_task[2])
        dumping_info = add_new_task.get_task_info()

        new_task_dictionary = { "id": add_new_task.id, "Description":  add_new_task.description, "Status": add_new_task.status }
    
        
        my_json["content"].append(new_task_dictionary)
        print(json.dumps(my_json, indent=4))
        #json.dump(my_json, 'w', ensure_ascii=False, indent=4)
        
        with open('task_list.json', 'w', encoding='utf-8') as f:
             json.dump(my_json, f, ensure_ascii=False, indent=4)


#update a task
if select_menu== "update":
    while user_input != "exit":
        update_task_id = input("Enter the id of task that you want to update: ")

        with open(f"{my_json_file_name}", "r") as json_data_file:

            print_task_data = Get_task_info(json_data_file)
            print("task before update")
            print(json.dumps(print_task_data.get_task_by_id(f"{update_task_id}"), indent=4))

            new_status = input("Select from the following:\n1. complete\n2. in-progress\n3. to-do\n")

            updated_task = print_task_data.update_task_status(update_task_id, new_status)

            print(json.dumps(updated_task, indent=4))


#list tasks
if select_menu == "task list":
    list_type = input("\nFor full list enter: all\nFor specific task enter: id\nFor specific status enter: status\n============================\n\n")

    if list_type == "all":
        with open(f'{my_json_file_name}') as json_file:
            task = json.load(json_file)
            print(json.dumps(task, indent=4))

    if list_type == "id":
        task_id = input("\nEnter the id number of the task: ")
        with open(f"{my_json_file_name}", "r") as json_data_file:

            print_task_data = Get_task_info(json_data_file)
            #print_task_data.print_data_info()

            print(json.dumps(print_task_data.get_task_by_id(f"{task_id}"), indent=4))
    
    if list_type == "status":
        status_type = input("\nWhat status of tasks do you want to see: ")
        
        with open(f"{my_json_file_name}", "r") as json_data_file:
            print_task_data = Get_task_info(json_data_file)

            print(json.dumps(print_task_data.get_task_by_status(f"{status_type}"), indent=4))

            