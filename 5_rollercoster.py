print("""
                                                           
  ___   ___            .__    __    .__   __     /\         
 /   | |   \  _______  |__| _/  |_  |__| |  | __ )/   ______
/    |_|    \ \_  __ \ |  | \   __\ |  | |  |/ /     /  ___/
\    | |    /  |  | \/ |  |  |  |   |  | |    <      \___ \ 
 \___| |___/   |__|    |__|  |__|   |__| |__|_ \    /____  >
                                                                               
             
 _ __ ___ | | | ___ _ __ ___ ___   __ _ ___| |_ ___ _ __ 
| '__/ _ \| | |/ _ \ '__/ __/ _ \ / _` / __| __/ _ \ '__|
| | | (_) | | |  __/ | | (_| (_) | (_| \__ \ ||  __/ |   
|_|  \___/|_|_|\___|_|  \___\___/ \__,_|___/\__\___|_|   
                                                         """)


print("Welcome to the world deadliest rollercoster ride. Here you will gonna see god!\n")
print("We need some info about yourself")
ticket = 0
height = int(input("Please enter your height in cm\n"))
if height > 120:
    
    
    age = int(input("Please enter your age\n"))
    if age < 12:
        ticket+=5
        print(f"Then child ticket price is ${ticket}.")
    elif age >= 12 and age < 18 :
        ticket += 7
        print(f"Then youth ticket price is ${ticket}.")
    elif age >= 45 and age <= 55 :
        print(f"You are in mid life crises so today enjoy the free ride we will not charger you for ticket")    
    else:
        ticket += 12
        print(f"Then adult ticket price is ${ticket}.")

    photo = input("Do you want photo of enjoying this ride as a memory press y for yes or n for no\n")
    photo = photo.lower()
    if photo == "y":
        ticket +=3
    else:
        pass

    print(f"The total bill is ${ticket}\n\tEnjoy the ride dear!!!")    


   
else:
    print("Hey! hey! hey! Sorry you are too short please come after some years :)")    


