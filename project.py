students = []

def store():
    name = input("Enter the name: ")
    roll = input("Enter the roll: ")
    std = input("Enter the class: ")
    students.append({
        'name': name,
        'roll': roll,
        'std': std
    })
    print("Student stored successfully!")

def search():
    roll = input("Enter roll to search: ")
    for student in students:
        if student['roll'] == roll:
            print(f"Student Roll: {student['roll']}, Student Name: {student['name']}, Class: {student['std']}")
            return
    print("Student not found")

def display():
    if not students:
        print("No students found")
        return
    for student in students:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Class: {student['std']}")

def remove():
    roll = input("Enter roll to delete: ")
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("Student removed successfully!")
            return
    print("Student not found")

while True:
    print("------------------Student Mangement System---------------------------")
    print("\nChoose any one: 1.Store  2.Search  3.Display  4.Delete  5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        store()
    elif choice == "2":
        search()
    elif choice == "3":
        display()
    elif choice == "4":
        remove()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid Choice")