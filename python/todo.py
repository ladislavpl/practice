import sys

print("To-Do v1.0\n")

todo = []

try:
    while True:
        option = input("Zvolte akci (add, list, delete, end): ").lower()
        match option:
            case "add":
                name = input("Zadejte úkol: ")
                subject = input("Zadejte předmět: ")
                date = input("Zadejte datum odevzdání: ")
                todo.append({"name": name, "subject": subject, "date": date})
                print()
            case "list":
                if len(todo) == 0:
                    print("Seznam je prázdný!\n")
                else:
                    print()
                    for i in range(len(todo)):
                        print(f"{i + 1}.\nÚkol: {todo[i]["name"]}\nPředmět: {todo[i]["subject"]}\nDatum: {todo[i]["date"]}\n")
            case "delete":
                if len(todo) == 0:
                    print("Seznam je prázdný!\n")
                else:
                    print()
                    for i in range(len(todo)):
                        print(f"{i + 1}.\nÚkol: {todo[i]["name"]}\nPředmět: {todo[i]["subject"]}\nDatum: {todo[i]["date"]}\n")
                    try:
                        choose = int(input("Vyberte úkol ke smazání (pro zrušení zvolte 0): "))
                    except ValueError:
                        print("Zadali jste neplatnou hodnotu!\n")
                    if choose > 0:
                        try:
                            todo.pop(choose - 1)
                            print()
                        except IndexError:
                            print("Vámi zvolený úkol neexistuje!\n")
                    else:
                        print("Zadali jste neplatnou hodnotu!\n")
            case "end":
                sys.exit(0)
            case _:
                print("Zadali jste neplatný příkaz!\n")
except KeyboardInterrupt:
    sys.exit(0)