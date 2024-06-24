import csv
import re
from colorama import Fore, Back, Style

print(Fore.CYAN + "*" * 147)
print(Fore.CYAN + "*" * 147)
print(Fore.CYAN + "---------------------------------------------------------",Fore.YELLOW + "Welcome to Ali Boys Hostel",Fore.CYAN + "--------------------------------------------------------------")
print(Fore.CYAN + "*" * 147)
print(Fore.CYAN + "*" * 147)
print(Fore.RED + "\n                                            Note: 'Admin1234' is the password to access Admin page")
print(Style.RESET_ALL)

Workers_database = 'Workers.csv'
Residents_database = 'Residents.csv'
Complaints_database = 'Complaints.csv'

worker_details = []
resident_details = []

seater_2 = 16000
seater_3 = 13500
seater_4 = 12500

with open(Workers_database,"w",newline="") as f:
    writer=csv.writer(f)
f.close()
with open(Residents_database,"w",newline="") as f:
    writer=csv.writer(f)
f.close()
with open(Complaints_database,"w",newline="") as f:
    writer=csv.writer(f)
f.close()

# Selection for admin/workers/residents
def show_options():
    while True:
        options = str(input(Style.BRIGHT+"Enter\n1. For Admin\n2. For Residents\n3. For Workers\n4. To exit\nEnter your choice: "))
        print(Style.RESET_ALL)

        if options == "1" or options == "2" or options == "3" or options == "4" :
            break
        else:
            print(Fore.RED+ "\n--- Wrong input ---")
            print(Style.RESET_ALL)
    return options

# Function to view prices 
def view_prices():
    global seater_2
    global seater_3
    global seater_4
    print("\nThe rate list for rents is as follows:")
    print("The rent for 2 seater room is Rs. ", seater_2)
    print("The rent for 3 seater room is Rs. ", seater_3)
    print("The rent for 4 seater room is Rs. ", seater_4)

# Function to change prices
def change_prices():
    global seater_2
    global seater_3
    global seater_4
    while True:
        x = str(input("\nEnter the room for which you want to change the rent.\n1 for 2 seater\n2 for 3 seater\n3 for 4 seater\n4 to exit\nEnter your option:"))
        if x=="1":
            while  True:
                seater_2 = input("Enter new rent for 2 seater: ")
                if seater_2.isdigit():
                    break
                else:
                    print(Fore.RED+ "\nWrong Input")
                    print(Style.RESET_ALL)

        elif x=="2":
            while  True:
                seater_3 = input("Enter new rent for 3 seater: ")
                if seater_3.isdigit():
                    break
                else:
                    print(Fore.RED+ "\nWrong Input")
                    print(Style.RESET_ALL)

        elif x=="3":
            while  True:
                seater_4 = input("Enter new rent for 4 seater: ")
                if seater_4.isdigit():
                    break
                else:
                    print(Fore.RED+ "\nWrong Input")
                    print(Style.RESET_ALL)

        elif x == "4":
            break
        else:
            print(Fore.RED+ "\nWrong input")
            print(Style.RESET_ALL)
# Function for printing menu
def show_menu():
    print(Style.BRIGHT+"The menu for the hostel is: \n")
    print("Day      |       Breakfast        |        Lunch        |           Dinner             ")
    print("---------------------------------------------------------------------------------------")
    print("Monday   | Omellete, Paratha, Tea |    Lobia, Chatni    | Chiken Biryani, Raita, Zarda ")
    print("Tuesday  |  Egg fry, Paratha, Tea |        Curry        |     Mix Vegetables, Kheer    ")
    print("Wednesday|  Channa, Paratha, Tea  | Seasonal Vegetables |     Chiken Korma, Custard    ")
    print("Thursday |  Egg fry, Paratha, Tea | Daal Channa, Chatni | Chiken Pulao, Kebab, Raita   ")
    print("Friday   |   Nihari, Naan, Tea    |     Daal Chawal     |      Aloo Gosht, Kheer       ")
    print("Saturday | Omellete, Paratha, Tea |      Aloo Qeema     |      Daal Mash, Chatni       ")
    print("Sunday   |  Channa, Halwa, Kulcha |   Brunch on Sunday  |       Chicken Haleem       \n")

# Function for entering a worker
def create_worker():
    global Workers_database
    worker_details = []
    cond = False

    while True:
        while True:
            CNIC = input("CNIC: \n")
            if CNIC.isdigit() and len(CNIC)==13:
                break
            else:
                print(Fore.RED+ "\nWrong Input")
                print(Style.RESET_ALL)
        with open(Workers_database,"r",newline="") as f:
            reader = csv.reader(f)
            for records in reader:
                if CNIC == records[3]:
                    cond = True
        if cond==True:
            print(Fore.RED+"\nWorker already exists")
            print(Style.RESET_ALL)
            break
        while True:
            Name = input("Name: \n")
            x = re.sub(r'\s+', '', Name)
            if x.isalpha() == True:
                break
            else:
                print(Fore.RED+ "\nWrong Input")
                print(Style.RESET_ALL)
        Name = Name.capitalize()

        while  True:
            Age = input("Age: \n")
            if Age.isdigit():
                break
            else:
                print(Fore.RED+ "\nWrong Input")
                print(Style.RESET_ALL)

        while True:
            City = input("City: \n")
            if City.isalpha() == True:
                break
            else:
                print(Fore.RED+ "\nWrong Input")
                print(Style.RESET_ALL)
        City = City.capitalize()

        while True:
            Mobile_number = input("Mobile no.: \n")
            if Mobile_number.isdigit() and len(Mobile_number)==11:
                break
            else:
                print(Fore.RED+ "\nWrong Input")
                print(Style.RESET_ALL)

        while True:
            Area_of_Work = input("Area of Work: \n")
            if Area_of_Work.isalpha() == True:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)
        Area_of_Work = Area_of_Work.capitalize()

        while True:
            salary_paid = input("Is the worker's salary paid? ")
            if salary_paid=="yes" or salary_paid=="Yes" or salary_paid=="No" or salary_paid=="no":
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        information = [Name, Age, City, CNIC, Mobile_number, Area_of_Work, salary_paid]
        worker_details.append(information)
        with open(Workers_database,"a",newline="") as f:
            writer=csv.writer(f)
            writer.writerows(worker_details)

        print(Fore.YELLOW+"\nInformation saved successfully\n", worker_details)
        print(Style.RESET_ALL)
        f.close()
        break

# Function for entering a resident
def create_resident():
    global Residents_database
    resident_details = []
    cond = False

    while True:
        while True:
            CNIC = input("CNIC: \n")
            if CNIC.isdigit() and len(CNIC)==13:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        with open(Residents_database,"r",newline="") as f:
            reader = csv.reader(f)
            for records in reader:
                if CNIC == records[3]:
                    cond = True
        if cond==True:
            print(Fore.RED+"\nWorker already exist")
            print(Style.RESET_ALL)
            break

        while True:
            Name = input("Name: \n")
            x = re.sub(r'\s+', '', Name)
            if x.isalpha() == True:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)
        Name = Name.capitalize()

        while  True:
            Age = input("Age: \n")
            if Age.isdigit():
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        while True:
            City = input("City: \n")
            if City.isalpha() == True:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)
        City = City.capitalize()

        while True:
            Mobile_number = input("Mobile no.: \n")
            if Mobile_number.isdigit() and len(Mobile_number)==11:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        while True:
            Month_duration= input("Duration of stay in months: \n")
            if Month_duration.isdigit():
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        while True:
            rent_collected = input("Is the resident's rent paid? ")
            if rent_collected=="yes" or rent_collected=="Yes" or rent_collected=="No" or rent_collected=="no":
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        while True:
            room = input("Type of room;2, 3 or 4 seater? ")
            if room=="2" or room =="3" or room =="4":
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        information = [Name, Age, City, CNIC, Mobile_number, Month_duration +" months", rent_collected, room +" seater"]

        resident_details.append(information)
        with open(Residents_database,"a",newline="") as f:
            writer=csv.writer(f)
            writer.writerows(resident_details)

        print(Fore.YELLOW+"\nInformation saved successfully\n", resident_details)
        print(Style.RESET_ALL)
        f.close()
        break

# Function for viewing workers:
def view_worker():
    global Workers_database
    print("************** Viewing Workers **************")
    print("[Name, Age, City, CNIC, Mobile no., Area of Work, Salary paid]")
    with open(Workers_database,"r",newline="") as f:
        reader=csv.reader(f)
        
        for records in reader:
            print(records)
    f.close()
# Function for viewing residents:
def view_resident():
    global Residents_database
    print("************** Viewing Residents **************")
    print("[Name, Age, City, CNIC, MObile no., Duration of stay, Rent collected]")
    with open(Residents_database,"r",newline="") as f:
        reader=csv.reader(f)
        
        for records in reader:
            print(records)
    f.close()

# Function for searching a worker
def search_worker():
    global Workers_database
    print("******** Search Worker *********")

    while True:
        search_CNIC = input("Enter Worker's CNIC: \n")
        if search_CNIC.isdigit() and len(search_CNIC)==13:
            break
        else:
            print(Fore.RED+"\nWrong Input")
            print(Style.RESET_ALL)

    with open(Workers_database,"r",newline="") as f:
        reader = csv.reader(f)
        for records in reader:
            if search_CNIC == records[3]:
                print("The details of the desired worker are:")
                print(f'Name: {records[0]}')
                print(f'Age: {records[1]}')
                print(f'City: {records[2]}')
                print(f'CNIC: {records[3]}')
                print(f'Mobile no.: {records[4]}')
                print(f'Area of work: {records[5]}')
                print(f'Salary paid or not: {records[6]}')
                break
            else:
                print(Fore.RED+"\nWorker doesn't exist.")
                print(Style.RESET_ALL)
    f.close()

# Function for searching a resident
def search_resident():
    global Residents_database
    print("******** Search Resident *********")

    while True:
        search_CNIC = input("Enter Resident's CNIC: \n")
        if search_CNIC.isdigit() and len(search_CNIC)==13:
            break
        else:
            print(Fore.RED+"\nWrong Input")
            print(Style.RESET_ALL)

    with open(Residents_database,"r",newline="") as f:
        reader=csv.reader(f)
        for records in reader:
            if search_CNIC == records[3]:
                print("The details of the desired resident are:")
                print(f'Name: {records[0]}')
                print(f'Age: {records[1]}')
                print(f'City: {records[2]}')
                print(f'CNIC: {records[3]}')
                print(f'Mobile no.: {records[4]}')
                print(f'Duration of stay: {records[5]}')
                print(f'Rent paid or not: {records[6]}')
                print(f'Type of room: {records[7]}')
                break
            else:
                print(Fore.RED+"\nResident doesn't exist")
                print(Style.RESET_ALL)

    f.close()

# Function for deleting a worker
def delete_worker():
    global Workers_database
    updated_list=[]
    with open(Workers_database,"r",newline="") as f:
        reader=csv.reader(f)
        Found=False

        while True:
            CNIC = input("CNIC: \n")
            if CNIC.isdigit() and len(CNIC)==13:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        for records in reader:
            if CNIC == records[3]:
                Found=True
            else:
                updated_list.append(records)

    if Found == False:
        print(Fore.RED+"\n-------Worker not found------")
        print(Style.RESET_ALL)
    else:
        with open(Workers_database,"w", newline = "") as f:
                    writer=csv.writer(f)
                    writer.writerows(updated_list)
                
        print(Fore.BLUE+"\n-------Worker deleted succesfully--------")
        print(Style.RESET_ALL)
    f.close()

# Function for deleting a resident
def delete_resident():
    global Residents_database
    updated_list=[]

    with open(Residents_database,"r",newline="") as f:
        reader=csv.reader(f)
        Found=False

        while True:
            CNIC = input("CNIC: \n")
            if CNIC.isdigit() and len(CNIC)==13:
                break
            else:
                print("\nWrong Input")

        for records in reader:
            if CNIC == records[3]:
                Found=True
            else:
                updated_list.append(records)
    
    if Found == False:
        print(Fore.RED+"\n-------Resident not found------")
        print(Style.RESET_ALL)
    else:
        with open(Residents_database,"w",newline="") as f:
                    writer=csv.writer(f)
                    writer.writerows(updated_list)
                    
        print(Fore.BLUE+"-------Resident deleted succesfully--------")
        print(Style.RESET_ALL)
    f.close()

# Function for updating a worker
def update_worker():
    global Workers_database
    updated_list=[]

    while True:
        CNIC = input("CNIC: \n")
        if CNIC.isdigit() and len(CNIC)==13:
            break
        else:
            print(Fore.RED+"\nWrong Input")
            print(Style.RESET_ALL)

    Found = False
    with open(Workers_database,"r",newline="") as f:
        reader=csv.reader(f)
        for records in reader:
            if CNIC == records[3]:
                print("----------------Worker found succesfully----------------")
                Found=True

                while True:
                    updated_age = input("Enter worker's updated age: ")
                    if updated_age.isdigit()==True:
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)
                
                while True:
                    updated_mobno = input("Enter worker's updated mobile number: ")
                    if updated_mobno.isdigit() and len(updated_mobno)==11:
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)

                while True:
                    updated_aow = input("Enter worker's updated area of work: ")
                    if updated_aow.isalpha() == True:
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)
                updated_aow = updated_aow.capitalize()

                while True:
                    updated_salary = input("Is the worker's salary paid? ")
                    if updated_salary=="yes" or updated_salary=="Yes" or updated_salary=="No" or updated_salary=="no":
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)

                records[1] = updated_age
                records[4] = updated_mobno
                records[5] = updated_aow
                records[6] = updated_salary
            updated_list.append(records)

        if Found==False:
            print(Fore.RED+"\nWorker not found")
            print(Style.RESET_ALL)
            
        else:
            with open(Workers_database,"w",newline="") as f:
                writer=csv.writer(f)
                writer.writerows(updated_list)
            print("---------Updated Worker's information Succesfully--------")
                
    f.close()

# Function for updating a resident
def update_resident():
    global Residents_database
    updated_list=[]

    while True:
        CNIC = input("CNIC: \n")
        if CNIC.isdigit() and len(CNIC)==13:
            break
        else:
            print(Fore.RED+"\nWrong Input")
            print(Style.RESET_ALL)

    Found = False
    with open(Residents_database,"r",newline="") as f:
        reader=csv.reader(f)
        for records in reader:
            if CNIC == records[3]:
                print("----------------Resident found succesfully----------------")
                Found = True

                while True:
                    updated_mobno = input("Enter Resident's updated mobile number: ")
                    if updated_mobno.isdigit() and len(updated_mobno)==11:
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)

                while True:
                    updated_dos = input("Enter worker's duration of stay: ")
                    if updated_dos.isdigit() == True :
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)

                while True:
                    updated_rent = input("Is the resident's rent paid? ")
                    if updated_rent=="yes" or updated_rent=="Yes" or updated_rent=="No" or updated_rent=="no":
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)

                records[4] = updated_mobno
                records[5] = updated_dos
                records[6] = updated_rent
            updated_list.append(records)

        if Found==False:
            print(Fore.RED+"\nResident not found")
            print(Style.RESET_ALL)
            
        else:
            with open(Residents_database,"w",newline="") as f:
                writer=csv.writer(f)
                writer.writerows(updated_list)
            print("---------Updated Resident's information Succesfully--------")
                
    f.close()

# Function for creating complaints
def complaints():
    global Complaints_database
    Complaints = []
    cond = False

    while True:
        while True:
            CNIC = input("CNIC: \n")
            if CNIC.isdigit() and len(CNIC)==13:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        with open(Complaints_database,"r",newline="") as f:
            reader = csv.reader(f)
            for records in reader:
                if CNIC == records[1]:
                    cond = True
        if cond==True:
            print("Complaint already exist")
            break

        while True:
            Name = input("Name: \n")
            x = re.sub(r'\s+', '', Name)
            if x.isalpha() == True:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        Name = Name.capitalize()

        Complaint = input("Enter your complaint: \n")

        information = [Name, CNIC, Complaint]

        Complaints.append(information)

        with open(Complaints_database,"a",newline="") as f:
            writer=csv.writer(f)
            writer.writerows(Complaints)

        print("\nYour submitted complaint is: \n", Complaint)
        f.close()
        break

# Function for updating complaints
def update_complaints():
    global Complaints_database
    updated_list=[]

    while True:
        CNIC = input("CNIC: \n")
        if CNIC.isdigit() and len(CNIC)==13:
            break
        else:
            print(Fore.RED+"\nWrong Input")
            print(Style.RESET_ALL)

    Found = False
    with open(Complaints_database,"r",newline="") as f:
        reader=csv.reader(f)
        for records in reader:
            if CNIC == records[1]:
                print("----------------Complaint found succesfully----------------")
                Found = True
                updated_complaint = input("Update your complaint: ")

                records[2] = updated_complaint
            updated_list.append(records)

        if Found==False:
            print(Fore.RED+"There is no complaint for this CNIC.")
            print(Style.RESET_ALL)

        else:
            with open(Complaints_database,"w",newline="") as f:
                writer=csv.writer(f)
                writer.writerows(updated_list)
            print("---------Your Complaint is updated Succesfully--------")
    
    f.close()


# Function to delete a complaint
def delete_complaint():
    global Complaints_database
    updated_list=[]

    with open(Complaints_database,"r",newline="") as f:
        reader=csv.reader(f)
        Found=False
    
        while True:
            CNIC = input("CNIC: \n")
            if CNIC.isdigit() and len(CNIC)==13:
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)

        for records in reader:
            if CNIC == records[1]:
                Found=True
            else:
                updated_list.append(records)
    
        if Found == False:
            print(Fore.RED+"There is no complaint for this CNIC.")
            print(Style.RESET_ALL)
        else:
            with open(Complaints_database,"w",newline="") as f:
                    writer=csv.writer(f)
                    writer.writerows(updated_list)
                    
        print("\n-------Complaint deleted succesfully--------")
    f.close()

# Function to view complaints
def view_complaints():
    global Complaints_database
    print("************** Viewing Complaints **************")
    print("[Name, CNIC, Complaint]")
        
    with open(Complaints_database, "r",newline="") as f:
        reader = csv.reader(f)
        for records in reader:
            print(records)
    f.close()

# Calling the functions by admin
while True:
    n = show_options()
    if (n == "1"):
        print(Fore.MAGENTA+"|*|*|*|*|*|*|*|*| Welcome to Admin login |*|*|*|*|*|*|*|*|")
        print(Style.RESET_ALL)

        while True:
            password = str(input("Enter the password to login. To exit enter 0.\n"))
            if (password == "Admin1234"):
                print("******** Hello Admin ********")
                while True:
                    admin_options = str(input("\nEnter\n1. To create Worker\n2. To create Resident\n3. To view Worker\n4. To view Resident\n5. To search Worker\n6. To search Resident\n7. To update Worker\n8. To update Resident\n9. To delete Worker\n10.To delete Resident\n11.To show complaints\n12.To show Menu\n13.To view prices\n14.To change prices\n15.To go to main menu \nEnter your option: "))
                    if (admin_options == "1"):
                        create_worker()
                    elif (admin_options == "2"):
                        create_resident()
                    elif (admin_options == "3"):
                        view_worker()
                    elif (admin_options == "4"):
                        view_resident()
                    elif (admin_options == "5"):
                        search_worker()
                    elif (admin_options == "6"):
                        search_resident()
                    elif (admin_options == "7"):
                        update_worker()
                    elif (admin_options == "8"):
                        update_resident()
                    elif (admin_options == "9"):
                        delete_worker()
                    elif (admin_options == "10"):
                        delete_resident()
                    elif (admin_options == "11"):
                        view_complaints()
                    elif (admin_options == "12"):
                        show_menu()
                    elif (admin_options == "13"):
                        view_prices()
                    elif (admin_options == "14"):
                        change_prices()
                    elif (admin_options == "15"):
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)
                break
            elif (password == "0"):
                break
            else:
                print(Fore.RED+"\n***** Wrong password, Try again *****\n")
                print(Style.RESET_ALL)

# Callling function made by Resident
    elif (n == "2"):
        print(Fore.MAGENTA+"|*|*|*|*|*|*|*|*| Hello Resident |*|*|*|*|*|*|*|*|")
        print(Style.RESET_ALL)
        while True:
            resident_options = str(input("\nEnter\n1. For viewing menu\n2. For complaints\n3. To update your complaint\n4. To delete complaint\n5. To go to main menu\nEnter your choice: "))

            if (resident_options == "1"):
                show_menu()
            elif (resident_options == "2"):
                complaints()
            elif (resident_options == "3"):
                update_complaints()
            elif (resident_options == "4"):
                delete_complaint()
            elif (resident_options == "5"):
                break
            else:
                print(Fore.RED+"\n***Wrong option***") 
                print(Style.RESET_ALL)      

# Callling function made by Worker
    elif (n == "3"):
        while True:
            print(Fore.MAGENTA+"|*|*|*|*|*|*|*|*| Hello Worker |*|*|*|*|*|*|*|*|")
            print(Style.RESET_ALL)
            worker_options = str(input("\nEnter\n1 if you are a Cook\n2 if you are a Cleaner\n3 if you are a Warden\n4 to go to main menu\nEnter your option: "))
            if (worker_options == "1"):
                while True:
                    day = str(input("\nEnter the day for which you want the menu for:\n1 for Monday\n2 for Tuesday\n3 for Wednesday\n4 for Thursday\n5 for Friday\n6 for Saturday\n7 for Sunday\n8 to Exit\nEnter your option:"))
                    if (day == "1"):
                        print("The menu for today is:\n")
                        print("Breakfast: Omellete, Paratha, Tea\nLunch: Lobia, Chatni\nDinner: Chiken Biryani, Raita, Zarda\n")
                    elif (day == "2"):
                        print("The menu for today is:\n")
                        print("Breakfast: Egg fry, Paratha, Tea\nLunch: Curry\nDinner: Mix Vegetables, Kheer\n")
                    elif (day == "3"):
                        print("The menu for today is:\n")
                        print("Breakfast: Channa, Paratha, Tea\nLunch: Seasonal Vegetables\nDinner: Chiken Korma, Custard\n")
                    elif (day == "4"):
                        print("The menu for today is:\n")
                        print("Breakfast: Egg fry, Paratha, Tea\nLunch: Daal Channa, Chatni\nDinner: Chiken Pulao, Kebab, Raita\n")
                    elif (day == "5"):
                        print("The menu for today is:\n")
                        print("Breakfast: Nihari, Naan, Tea\nLunch: Daal Chawal\nDinner: Aloo Gosht, Kheer\n")
                    elif (day == "6"):
                        print("The menu for today is:\n")
                        print("Breakfast: Omellete, Paratha, Tea\nLunch: Aloo Qeema\nDinner: Daal Mash, Chatni\n")
                    elif (day == "7"):
                        print("The menu for today is:\n")
                        print("Brunch: Channa, Halwa, Kulcha\nDinner: Chicken Haleem\n")
                    elif (day == "8"):
                        print()
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)

            elif (worker_options == "2"):
                while True:
                    day = str(input("\nEnter the day for which you want the schedule for:\n1 for Monday\n2 for Tuesday\n3 for Wednesday\n4 for Thursday\n5 for Friday\n6 for Saturday\n7 for Sunday\n8 to Exit\nEnter your option:"))
                    if (day == "1"):
                        print("The schedule for today is:\n")
                        print("You have to clean the rooms 1-15 of 1st floor today.\n")
                    elif (day == "2"):
                        print("The schedule for today is:\n")
                        print("You have to clean the rooms 16-30 of 1st floor today.\n")
                    elif (day == "3"):
                        print("The schedule for today is:\n")
                        print("You have to clean the rooms 1-15 of 2nd floor today.\n")
                    elif (day == "4"):
                        print("The schedule for today is:\n")
                        print("You have to clean the rooms 16-30 of 2nd floor today.\n")
                    elif (day == "5"):
                        print("The schedule for today is:\n")
                        print("You have to clean the rooms 1-15 of 3rd floor today.\n")
                    elif (day == "6"):
                        print("The schedule for today is:\n")
                        print("You have to clean the rooms 16-30 of 3rd floor today.\n")
                    elif (day == "7"):
                        print("Today is Sunday. Go and chill!\n")
                    elif (day == "8"):
                        print()
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)
            elif (worker_options == "3"):
                while True:
                    day = str(input("\nEnter the day for which you want the schedule for:\n1 for Monday\n2 for Tuesday\n3 for Wednesday\n4 for Thursday\n5 for Friday\n6 for Saturday\n7 for Sunday\n8 to Exit\nEnter your option:"))
                    if (day == "1"):
                        print("The schedule for today is:\n")
                        print("You have to check the rooms 1-15 of 1st floor today.\n")
                    elif (day == "2"):
                        print("The schedule for today is:\n")
                        print("You have to check the rooms 16-30 of 1st floor today.\n")
                    elif (day == "3"):
                        print("The schedule for today is:\n")
                        print("You have to check the rooms 1-15 of 2nd floor today.\n")
                    elif (day == "4"):
                        print("The schedule for today is:\n")
                        print("You have to check the rooms 16-30 of 2nd floor today.\n")
                    elif (day == "5"):
                        print("The schedule for today is:\n")
                        print("You have to check the rooms 1-15 of 3rd floor today.\n")
                    elif (day == "6"):
                        print("The schedule for today is:\n")
                        print("You have to check the rooms 16-30 of 3rd floor today.\n")
                    elif (day == "7"):
                        print("You have to check the kitchen today.\n")
                    elif (day == "8"):
                        print()
                        break
                    else:
                        print(Fore.RED+"\nWrong Input")
                        print(Style.RESET_ALL)
            elif (worker_options == "4"):
                print()
                break
            else:
                print(Fore.RED+"\nWrong Input")
                print(Style.RESET_ALL)


    elif (n == "4"):
        print(Fore.MAGENTA+"|*|*|*|*|*|*|*|*| Thanks for Visiting |*|*|*|*|*|*|*|*|")
        print(Style.RESET_ALL)
        break