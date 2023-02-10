#first function, named hello and prints a greeting to the user

def hello():
    print("Hello user!")

hello()

#second function, named pack.  Accepts 3 arguments and returns a single list

def pack(a, b ,c):
    list_items = [a, b, c]
    print(list_items)

pack("Football", "Basketball", "Baseball")


#third function, named eat_lunch.  accept a list of any length and return the items to three different messages


def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty")
    else:
        for l in range(len(lunch_list)):
            if l == 0:
                print(f"First I eat {lunch_list[0]}")
            else:
                print(f"Next I eat {lunch_list[l]}")


eat_lunch([])
eat_lunch(["Boiled Eggs"])
eat_lunch(["Boiled Eggs", "Chips", "Banana", "Water"])
