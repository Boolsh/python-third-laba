# Класс «Бог» с полями «имя», «стихия». Декоратор, который помимо действия
# метода, выводит «Вы осмелились потревожить имя_бога». Декорировать им все методы
# (кроме геттера имени). Добавить метод «выслушать молитву», который принимает
# строку и ничего с ней не делает.
#Пекшин Степан 9 группа


from God import God

def main():
    pantheon = []
    choice = 0
    while (choice != 6):
        choice = menu()
        if (choice == 1):
            add_God(pantheon)
        elif (choice == 2):
            print_list(pantheon)
        elif (choice == 3):
            pray(pantheon)
        elif (choice == 4):
            load_from_file(pantheon)
        elif (choice == 5):
            save_to_file(pantheon)






def validation(inp, condition):
    while True:
        try:
            inp = int(input(">>> "))
            if condition(inp):
                return inp
            else:
                print("Ошибка ввода")
        except ValueError:
            print("Ошибка ввода")

def menu():
    print("1.Добавить Бога\n"
                   "2.Посмотреть всех добавленных Богов\n"
                   "3.Выслушать молитву\n"
                   "4.Загрузить из файла\n"
                   "5.Сохранить в файл\n"
                   "6.Завершить работу программы")

    choice = 0
    choice = validation(choice, lambda inp: (inp >= 1) and (inp <= 6))
    return choice

def add_God(list):
    name = str(input("Введите имя Бога:"))
    elem = str(input("Введите стихию Бога:"))
    new_God = God(name, elem)
    print()
    list.append(new_God)

def pray(list):
    if (len(list) == 0):
        print("Некому молиться\n")
    else:
        choice = 1
        print(f"К какому Богу Вы хотите обратиться с молитвой (1-{len(list)})?")
        choice = validation(choice, lambda inp: (inp >=1) and inp <=len(list))
        praying = str(input("Напишите молитву"))
        list[choice-1].listen_praying(praying)

def load_from_file(list):
    filename = input("Введите имя файла для загрузки: ")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                name, elem= line.strip().split(',')
                new_God = God(name, elem)
                list.append(new_God)
        print("Данные загружены.")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")

def save_to_file(list):
    filename = input("Введите имя файла для сохранения: ")
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for  i in list:
                file.write(f"{i.get_name()}, {i.get_elem()}\n")
        print("Данные сохранены.")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def print_list(list):
    for i in list:
        print(i)




if __name__ == "__main__":
    main()


