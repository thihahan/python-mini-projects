from random import randint
metals = [' Lithium','Beryllium', ' sodium','   Magnesium', 'Aluminum' , 'Potassium', 'Calcium', '	Scandium', '	Chromium', 'Manganese', 'Iron', 'Copper', 'Zinc', 'Tin', 'Cesium', 'Barium', ]
non_metals = ['Hydrogen', 'Helium', 'Carbon', 'nitrogen', 'Oxygen','Fluorine', '	Neon', '	Phosphorus', '	Sulfur', '	Chlorine', '	Argon', 'Bromine', '	Iodine']

quit = False
def game():
    ran = randint(1,2)
    if ran == 1:
        number = randint(0,len(metals)-1)
        user_ans = input((f"{metals[number].strip()} is (1).metal or (2).non-metal. please answer 1 or 2:   "))
        if user_ans == '1':
            print("True")
        else: print("False")
    elif ran == 2:
        number = randint(0,len(non_metals)-1)
        user_ans = input((f"{non_metals[number].strip()} is (1).metal or (2).non-metal. please answer 1 or 2:   "))
        if user_ans == '2':
            print("True")
        else: print("False")
while not quit:
    game()
    
 