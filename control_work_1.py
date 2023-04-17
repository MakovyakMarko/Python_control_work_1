
def comparison():
    x = int(input("Введіть х: "))
    y = int(input("Введіть у: "))
    if x > y:
        print("x > y")
    elif x < y:
        print("x < y")
    elif x == y:
        print("x = y")
    else:
        print("Invalid value. ")
# comparison()

x = 20
y = 10
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x // y)
print(x % y)

print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print(x == y)
print(x != y)

x += 5
print(x)
x -= 5
print(x)
x *= 2
print(x)
x /= 2
print(x)
x %= 6
print(x)

list = ["Yellow","Green", "Blue"]
def myfunc():
    for x in list:
        x = input("Enter data to list: ")
        list.append(x)
        print(list)
        y = input("Would you enter more data?(y/n): ")
        if y == "y":
            myfunc()
        elif y == "n" :
            z = print(list)
        break
#myfunc()

# Робота з рядками
# Чи є в рядку елемент (слово)?
# Чи немає слова в рядку?
def string_menager():
    string = ()
    try:
        while True:
            print("What do you want to do with string?")
            print("1.Create string")
            print("2.Check string")
            print("3.Check legth of string")
            print("4.Capitalize string")
            print("5.Upper string")
            print("6.Lower string")
            print("7.Count in string")
            print("8.Search in string")
            print("9.Find index of letter in string")
            print("10.Break string to parts")
            print("11.Replace in string")
            print("12.Split string to list")
            print("13.Print string")
            print("14.Exit")
            choise = input("Make your chiose (1-14): ")
            if choise == "1":
                print(string)
                value = input("Do you want to add some data into string? (y/n): ")
                if value == "y":
                    data = input("Type data into string: ")
                    string = str(data)
                elif value == "n":
                    continue
                else:
                    print("Invalid value.")
            elif choise == "2":
                check = input("What value you want to check in string?: ")
                if check in string:
                    print(f"{check} is in the string")
                else:
                    print(f"{check} is not in the string")
            elif choise == "3":
                print("Length of the string is", len(string), "charecters.")
            elif choise == "4":
                print(string.capitalize())
            elif choise == "5":
                print(string.upper())
            elif choise == "6":
                print(string.lower())
            elif choise == "7":
                count = input("What we will count?: ")
                if count in string:
                    print("There is ",string.count(count), "characters")
                else:
                    print("There is no such value in string")
            elif choise == "8":
                search = input("What we will search?: ")
                if search in string:
                    print(string.find(search))
                else:
                    print("There is no such value in string")
            elif choise == "9":
                index = input("Type letter wich index you want to know: ")
                if index in string:
                    print(string.index(index))
                else:
                    print("There is no such letters in string")
            elif choise == "10":
                break_word = input("Type the word to break around it: ")
                if break_word in string:
                    print(string.partition(break_word))
                else:
                    print("There is no such word in string")
            elif choise == "11":
                str_word = input("Type word in string wich you want to replace: ")
                if str_word in string:
                    repl_word = input("Type new word to replace: ")
                    print(string.replace(str_word, repl_word))
                else:
                    print("There is no such word in string")
            elif choise == "12":
                string.split()
                print(string)
            elif choise == "13":
                print(string)
            elif choise == "14":
                print("Exiting program.")
                break
            else:
                print("Invalid value.")
        return string
    except KeyError:
        print("Invalid input.")

string_menager()
# виберіть що ви хочете зробити:
# додати до спику - append()
# видалити зі списку - pop()
# змінити список - list[x] = z
# сортувати список - list.sort

thislist = ["Values:"]
def lists():
    while True:
        x = input("What would you do with list? Add item('a'). Remove item('r'). Sort list('s'). Nothing ('n'): ")
        if x == "a":
            x = input("Enter the item: ")
            thislist.append(x)
            print(thislist)
            add = input("Would you add more items? (y/n):")
            while add == "y":
                add = input("Enter the item: ")
                thislist.append(add)
                print(thislist)
                add = input("Would you add more items? (y/n):")
            if add == "n":
                continue
        elif x == "r":
            r = input("Enter item value to remove item: ")
            thislist.remove(r)
            print(thislist)
            r = input("Would you remove more items? (y/n): ")
            while r == "y":
                r = input("Enter the item value to remove: ")
                thislist.remove(r)
                print(thislist)
                r = input("Would you remove more items? (y/n): ")
            if r == "n":
                continue
        elif x == "s":
            thislist.sort()
            print(thislist)
            s = input("Would you like to reverse the list? (y/n): ")
            if s == "y":
                thislist.sort(reverse=True)
                print(thislist)
            elif s == "n":
                continue
        elif x == "n":
            print(thislist)
            break
        else:
            print("Invalid input. Please try again.")
    again = input("Would you like to perform another oparation? (y/n): ")
    if again == "y":
        lists()
    elif again == "n":
        print("Exiting program.")
# видаліть шарп, якщо хочете побачити як прцює функція
#lists()
# ефктивніша функція для роботи з списками від chatGPT
def list_menager():
    my_list = []
    while True:
        print("What would you like to do with the list?")
        print("1. Add item")
        print("2. Remove item")
        print("3. Sort list")
        print("4. Reverse list")
        print("5. Print list")
        print("6. Exit")

        choise = input("Enter your choise (1-6): ")

        if choise == "1":
            item = input("Enter your item: ")
            my_list.append(item)
            print(f"{item} hes been added to the list.")
        elif choise == "2":
            item = input("Enter the item to remove: ")
            if item in my_list:
                my_list.remove(item)
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} is not in the list.")
        elif choise == "3":
            my_list.sort()
            print("List has been sorted.")
        elif choise == "4":
            my_list.reverse()
            print("List has been reversed.")
        elif choise == "5":
            print("Curent list: ", my_list)
        elif choise == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please try again.")
    return my_list

#list_menager()
# Робота з словниками
# Що ви хочете зробити з словником?
# дадати ключ та значення
# змінити ключ, змінити значення
# копіювати словник
# видалити словник, ключ і значення
# очистити словник
def dictionary_manager():
    dictionary = {}
    while True:
        print("What would you like to do with dictionary?")
        print("1.Create dictionary")
        print("2.Add key and value")
        print("3.Change value")
        print("4.Remove key and value")
        print("5.Print dictionary")
        print("6.Print items")
        print("7.Print keys")
        print("8.Print values")
        print("9.Clear dictionary")
        print("10.Exit")
        choise = input("Make your choise (1-10): ")
        if choise == "1":
            #new_dictionary = dict({})
            #print(new_dictionary)
            print(dictionary)
            first_adding = input("Do you want to enter first key and value? (y/n): ")
            if first_adding == "y":
                key = input("Enter first key value: ")
                value = input("Enter first value for key: ")
                #new_dictionary.update({key:value})
                dictionary.update({key:value})
            elif first_adding == "n":
                continue
            else:
                print("Invalid value")
        elif choise == "2":
            key = input("Enter key: ")
            value = input("Enter value: ")
            dictionary.update({key:value})
            add = input("Do you want add more keys and values? (y/n): ")
            while add == "y":
                key = input("Enter key: ")
                value = input("Enter value: ")
                dictionary.update({key: value})
                add = input("Do you want add more keys and values? (y/n): ")
                if add == "n":
                    continue
        elif choise == "3":
            key = input("Enter key to change its value: ")
            if key in dictionary.keys():
                new_value = input("Enter new value: ")
                dictionary[key] = new_value
            else:
                print("Theare is no such keys in dictionary")
            change = input("Do you want to change onther value? (y/n): ")
            while change == "y":
                key = input("Enter key to change its value: ")
                if key in dictionary.keys():
                    new_value = input("Enter new value: ")
                    dictionary[key] = new_value
                    change = input("Do you want to change onther value? (y/n): ")
                else:
                    print("Theare is no such keys in dictionary")
            if change == "n":
                continue
        elif choise == "4":
            key = input("Enter the key to remove key and value: ")
            if key in dictionary.keys():
                dictionary.pop(key)
            else:
                    print("There is no such keys in dictionary")
        elif choise == "5":
            print(dictionary)
        elif choise == "6":
            for keys, values in dictionary.items():
                print(keys,values)
        elif choise == "7":
            for key in dictionary.keys():
                print(key)
        elif choise == "8":
            for value in dictionary.values():
                print(value)
        elif choise == "9":
            dictionary.clear()
        elif choise == "10":
            print("Exiting program")
            break
        else:
            print("Invalid value!")
    return dictionary
#dictionary_manager()
# покращення коду від ChatGPT
def dictionary_manager_chatGPT():
    dictionary = {}
    while True:
        print("What would you like to do with dictionary?")
        print("1.Create dictionary")
        print("2.Add key and value")
        print("3.Change value")
        print("4.Remove key and value")
        print("5.Print dictionary")
        print("6.Print items")
        print("7.Print keys")
        print("8.Print values")
        print("9.Clear dictionary")
        print("10.Exit")
        choise = input("Make your choise (1-10): ")
        try:
            if choise == "1":
                #new_dictionary = dict({})
                #print(new_dictionary)
                print(dictionary)
                first_adding = input("Do you want to enter first key and value? (y/n): ")
                if first_adding == "y":
                    key = input("Enter first key value: ")
                    value = input("Enter first value for key: ")
                    #new_dictionary.update({key:value})
                    dictionary.update({key:value})
                elif first_adding == "n":
                    continue
                else:
                    print("Invalid value")
            elif choise == "2":
                add = "y"
                while add == "y":
                    key = input("Enter key: ")
                    value = input("Enter value: ")
                    dictionary.update({key: value})
                    add = input("Do you want add more keys and values? (y/n): ")
                    if add == "n":
                        continue
            elif choise == "3":
                change = "y"
                while change == "y":
                    key = input("Enter key to change its value: ")
                    if key in dictionary.keys():
                        new_value = input("Enter new value: ")
                        dictionary[key] = new_value
                    else:
                        raise KeyError("Theare is no such keys in dictionary")
                    change = input("Do you want to change onther value? (y/n): ")
            elif choise == "4":
                key = input("Enter the key to remove key and value: ")
                if key in dictionary.keys():
                    dictionary.pop(key)
                else:
                    raise KeyError("There is no such keys in dictionary")
            elif choise == "5":
                print(dictionary)
            elif choise == "6":
                print(dictionary.items())
            elif choise == "7":
                print(dictionary.keys())
            elif choise == "8":
                print(dictionary.values())
            elif choise == "9":
                dictionary.clear()
            elif choise == "10":
                print("Exiting program")
                break
            else:
                print("Invalid value!")
        except KeyError as e:
            print("Error:",str(e))
    return dictionary

#dictionary_manager_chatGPT()

# робота з кортежами
# створити кортеж і заповнити
def tuple_menager():
    tuple_list = []
    try:
        while True:
            print("What do you want to do with tuple?")
            print("1.Create tuple")
            print("2.Print tuples")
            print("3.Delete tuple")
            print("4.Exit")
            choise = input("Make your choise (1-4): ")
            if choise == "1":
                tuples = int(input("How many tuples you want to create?: "))
                for i in range(tuples):
                    data = input(f"Enter the values for {i+1} tuple: ")
                    tuple_data = tuple(data.split(","))
                    tuple_list.append(tuple_data)
            elif choise == "2":
                print(tuple_list)
            elif choise == "3":
                print(tuple_list)
                delete = int(input("Count from 1 and choose wich tuple you want to delete?:"))
                i = delete - 1
                if i not in range(tuple_list):
                    print("Invalid value.")
                else:
                    tuple_list.pop(i)
            elif choise == "4":
                print("Exiting program.")
                break
            else:
                print("Invalid value.")
        return tuple_list()
    except KeyError:
        print("Invalid value.")

#tuple_menager()

def set_menager():
    thisset = set()
    try:
        while True:
            print("Whay do you want to do with set?")
            print("1.Create set")
            print("2.Add items to set")
            print("3.Remove items from set")
            print("4.Print set")
            print("5.Exit")
            choise = input("Make your choise (1-5): ")
            if choise == "1":
                print(thisset)
                question = input("Do you want to add item into set? (y/n): ")
                while question == "y":
                    item = input("Enter the item: ")
                    thisset.add(item)
                    question = input("Do you want to add item into set? (y/n): ")
                    if question == "n":
                        continue
            elif choise == "2":
                question = "y"
                while question == "y":
                    item = input("Enter the item: ")
                    thisset.add(item)
                    question = input("Do you want to add more items? (y/n): ")
                    if question == "n":
                        continue
            elif choise == "3":
                item = input("Enter the item wich you want remove from set: ")
                if item in thisset:
                    thisset.remove(item)
                else:
                    print("Theare is no such item in set")
            elif choise == "4":
                print(thisset)
            elif choise == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid value.")
        return thisset()
    except KeyError:
        print("Invalid value.")

#set_menager()
