# Create initial to-do list
tasks = [
    "Start Python Course",
    "Chap 1",
    "Chap 2",
    "Chap 3",
    "Chap 4",
    "Chap 5",
    "Chap 6",
    "Chap 7",
    "Chap 8",
    "Chap 9"
]

# Write tasks to file
with open("ToDo_list.txt", "w") as f:
    for i, task in enumerate(tasks, 1):
        f.write(f"{i}) {task}: Pending\n")

# Ask user which task to complete
task_no = int(input("Enter task number to mark as completed: "))

# Read file
with open("ToDo_list.txt", "r") as f:
    lines = f.readlines()

# Update selected task
lines[task_no - 1] = lines[task_no - 1].replace("Pending", "Completed")

# Write back updated file
with open("ToDo_list.txt", "w") as f:
    f.writelines(lines)

print("Task Updated Successfully")