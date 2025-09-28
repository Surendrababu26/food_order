print("order of the food")
while True:
    print("1.burger")
    print("2.pizza")
    choice = int(input("choose the choice(1/2): "))

    if choice == 1:
        print("your order is burger and you want any fries(yes/no)")
        extra = input("enter your answer: ")
        if extra == "yes":
            print("your order is burger and fries")
        else:
            print("your order is only burger")
        break  

    elif choice == 2:
        print("your order is pizza and you want any extra cheese(yes/no)")
        extra = input("enter your answer: ")
        if extra == "yes":
            print("your order is pizza and extra cheese")
        else:
            print("your order is only pizza")
        break   

    else:
        print("invalid choice")
