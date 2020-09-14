from potato_class import *
from wheat_class import *
from sheep_class import *
from cow_class import *
import random
class Field:

    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_cropst

    def plant_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False
    def add_animal(self, animal):
        if len(self._animals)< self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False
    def harvest_crop(self, position):
        return self._crops.pop(position)
    def remove_animal(self,position):
        return self._animal.pop(position)
    def report_contents(self):
        crop_report = []
        animal_report=[]
        for crops in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return{"crops": crop_report, "animals": animal_report}
    def report_needs(self):
        food=0
        light=0
        water=0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"]> light:
                light= needs["light need"]
            if needs ["water need"]>water:
                water= needs["water need"]
        for animal in self._animals:
            needs = animal.need()
            food += needs ["food need"]
            if needs["water need"]>water:
                water = needs["water need"]
        return {"food":food,"light":light, "water":water}
    def grow(self,light,food,water):
        if len(self._crops)>0:
            for crop in self._crops:
                crop.grow(light,water)
        if len(self._animals)>0:
            food_required = 0
            for animal in self._animals:
                needs = animal.needs()
                food_required += needs["food need"]
            if food > food_required:
                additional_food = food - food_required
                food = food_requested
            else:
                additional_food=0
            for animal in self._animals:
                needs = animal.needs()
                if food >= needs["food needs"]:
                    food -= needs["food need"]
                    feed = needs["food need"]
                if additional_food > 0:
                    additional_food -= 1
                    feed += 1
                animal.grow(feed,water)
def auto_grow(self,days):
    for day in range(days):
        light = random.randint(1,10)
        water= random.randint(1,10)
        food= random.randint(1,100)
        field.grow(light,food,water)
def manual_grow(field):
    valid=False
    while not valid:
        try:
            light = int(input("please enter a light value"))
            if 1 <= light <= 10:
                valid = True
            else:
                print("value entered not valid")
        except ValueError:
            print("please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int (input("please enter a water value 1-10"))
            if 1<=water<=10:
                valid=True
            else:
                print("value enetered not valid")
        except ValueError:
            print("value entered not valid")
    valid = False
    while not valid:
        try:
            water = int (input("please enter a food value 1-100"))
            if 1<=food<=100:
                valid=True
            else:
                print("value enetered not valid")
        except ValueError:
            print("value entered not valid")
    field.grow(light,food,water)
    
    
                
                
            

def display_crops(crop_list):
    print("the following crops are in this field")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos +=1

def display_animals(animal_list):
    print("the following animals are in this field")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos +=1
def select_crops(length_list):
    valid = False
    while not valid:
        selected = int(input("please select a crop"))
        if selected in range(1,length_list+1):
            valid=True
        else:
            print("please select a valid option")
        return selected -1
def select_animal(length_list):
    valid=False
    while not valid:
        selected = int(input("pelese select an animal:"))
        if selected in range(1,length_list+1):
            valid=True
        else:print("please select a valid option")
    return selected - 1
        
def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop= select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)
        
def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove_animal(selected_animal)
def display_crop_menut():
    print("which crop would you like to add")
    print("1.potato")
    print("2.wheat")
    print("")
    print("0.return to main menu")
def display_animal_menue():
    print("which animal would you like to add")
    print("1.cow")
    print("2.sheep")
    print("")
    print("return to main menu")
def display_main_menu():
    print("1, plant a new crop")
    print("2, harvest a crop")
    print("3.add an animal")
    print("4. remove an animal")
    print("5.grow field manually over 1 day")
    print("grow field over 30 days")
    print("7. report field status")
    print("8.exit the test")
    print("please select an option")
def get_menu_choice(lower,upper):
    valid = False
    while not valid:
        try:
            choice = int (input("option selected"))
            if lower <= choice <= upper:
                  valid = True
            else:
                print("please enter a valid option")
        except ValueError:
            print ("hplease enter a valid input")
    return choice
def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.plant_crop(Potato()):
            print("crop planted")
        else:
            print("field is full")
    elif choice == 2:
        if field.plant_crop(Wheat()):
            print("crop planted")
        else:
            print("field is full")
def manage_field ():
    print("this is the field management program")
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,7)
        if option == 1:
            plant_crop_in_field(field)
        elif option == 2:
            remove_crop = harvest_crop_from_field(field)
            print("you removed the crop".format(remove_crop))
        elif option==3:
            add_animal_to_field(field)
        elif option == 4:
            removed_animal = remove_animal_from_field(field)
            print("you removed the animal".format(removed_animal))
        elif option == 5:
            manual_grow(field)
        elif option==6:
            auto_grow(field,30)
        elif option == 7:
            print(field.report_contents())
        elif opiton == 0:
            exit=True
    print("thankyou for using the field management system")


def get_menu_choice(lower,upper):
    valid = False
    while not valid:
        try:
            choice= int(input("option selected" ))
            if lower <= choice <=upper:
                valid = True
            else:
                print("please enter a valid number")
        except ValueError:
            print("please enter a valid opiton")
    return choice
def plant_crop_in_field(field):
    display_crop_menui()
    choice = get_menu_choice(0,2)
    if choice == 1 :
        if field.plant_crop(Potato()):
            print("crop planted")
        else:
            print("field is full")
    elif choice == 2:
        if field.plant_crop(Wheat()):
            print("crop planted")
        else:
            ("field is full")
            

    
    
                

def main():
    new_field = Field(5,2)
    manage_field(new_field)
    

                  

if __name__ == "__main__":
    main()
