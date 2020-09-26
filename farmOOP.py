import crop

def display_menu():
    print("1.grow manually over a day")
    print("2.auto grow over 30 days")
    print("3.status report")
    print("0. exit test")
    print()
    print('please select an option')

def get_menu_choice():
    option_valid=False
    while not option_valid:
        try:
            choice = int(input("option selected"))            
            if 0 <= choice <= 4:
                option_valid=True
            else:
                print("please enter a valid option")
        except ValueError:
            print("please enter a valid option")
    return choice


def manage_crop(crop):
    print("this is the crop management program")
    print()
    noexit=True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print('option chosen',option)
        if option == 1:
            crop.manual_grow()
            print(crop.report())
        elif option == 2:
            crop.auto_grow(30)
        else:
            noexit = False


def main():
    new_crop = crop.Crop(2,7,3)
    manage_crop(new_crop)
    print(new_crop.report())


main()
