import pickle
import datetime

def Menu() :
    print('*'*148)
    print("MAIN MENU".center(148))
    print(" "*48+"1. Insert Employee Record / Records")
    print(" "*48+"2. Display Sorted Employee Records as per Emp No.")
    print(" "*48+"3. Display Sorted Employee Records as per Names ")
    print(" "*48+"4. Display Sorted Employee Records as per Designation ")
    print(" "*48+"5. Display Employee Records as the Designation")
    print(" "*48+"6. Delete Record")
    print(" "*48+"7. Update Record")
    print(" "*48+"8. Search Employee Record Details as per the Employee Number")
    print(" "*48+"9. Search Record Details as per the Customer Name")
    print(" "*48+"10. Display Gross Salary Breakup")
    print(" "*48+"11. Exit")
    print("*"*148)

def SortAcc(F) :            #Function to arrange records as per ascending order of Employee Number
    try :
        with open(F,'rb+') as fil :
            rec= pickle.load(fil)
            rec.sort(key=lambda rec : rec['ID'])
            fil.seek(0)
            pickle.dump(rec,fil)
            
    except FileNotFoundError :
        print(F, "File has no records ")


def SortName(F) :            #Function to arrange records as per ascending order of Employee Name
    try :
        with open(F,'rb+') as fil :
            rec= pickle.load(fil)
            rec.sort(key=lambda rec : rec['NAME'])
            fil.seek(0)
            pickle.dump(rec,fil)
            
    except FileNotFoundError :
        print(F, "File has no records ")

def SortDesig(F) :            #Function to arrange records as per ascending order of Designation
    try :
        with open(F,'rb+') as fil :
            rec= pickle.load(fil)
            rec.sort(key=lambda rec : rec['Desig'])
            fil.seek(0)
            pickle.dump(rec,fil)
            
    except FileNotFoundError :
        print(F, "File has no records ")


def Insert(F) :
    try :
        fil = open(F,'ab+')     #will create file if not existing else read the records from the existing file .
        print(fil.tell())
        Des = ["MGR","CLK","VP","PRES"]
        Dep = ["HR","IT","SALES","FIN"]
        if fil.tell() > 0 :
            fil.seek(0)
            Rec1 = pickle.load(fil)
        else :
            Rec1 = []
        while True :        #Loop for accepting records

           #Allowing only unique Employee Ids to be inserted
            while True :
                Eid = input("Enter Emp Id ")
                Eid = Eid.upper()
                if any(dict.get('ID') == Eid for dict in Rec1) :    #checks whether the Eid is already existing in list of dictionary
                    print("Employee already exists ")
                else :
                    break
            Name = input("Enter Employee Name ")
            #Allowing only valid 10 digit Mobile No. to be inserted
            while True:
                Mob = input("Enter Mobile Number ")
                if len(Mob)!=10 or Mob.isdigit() == False :
                    print("Please enter valid Mobile No.")
                else :
                    break
                    
            #Allowing only valid email address to be inserted
            while True:
                    Email = input("Enter Email ")
                    if '@' not in Email or '.' not in Email :
                        print("Please enter valid Email address")
                    else :
                        break

             #Allowing only specific Deptid to be inserted
            while True :
                Deptid = input("Enter Dept Name of the Employee (HR / IT / SALES / FIN)")
                if Deptid.upper() in Dep :
                    break
                
            #Allowing only specific Designation to be inserted
            while True :
                Desig = input("Enter the Designation (MGR / CLK / PRES / VP )")
                if Desig.upper() in Des :
                    break

            Sal = float(input("Enter Salary "))

            #The current date is stored as the Date of joining of the Employee
            Dat = datetime.datetime.now()
            Dat = Dat.date()
            Rec = {"ID" : Eid.upper() , "NAME" :Name.upper() , "Mob" :Mob , "Email" : Email.upper() ,\
                   "DeptID" : Deptid.upper() , "Desig":Desig.upper(), "Sal" : Sal}
            Rec1.append(Rec)
            pickle.dump(Rec, fil)
            ch = input("Do you want to enter more records")
            if ch == 'N' or ch == 'n' :
                break
        fil.close()
        with open(F,'wb') as fil :      #will open the file for overwriting
            pickle.dump(Rec1, fil)
            
    except ValueError:
        print("Invalid values entered ")

        
def Display(F) :        #Function to Display the records in the Binary File
    try :
        with open(F, "rb") as fil :
            F = "%15s %15s %15s %15s %15s %15s %15s %15s"
            print(F % ("ID", "NAME", "MOBILE", "EMAIL ADDRESS ", "Dept ID", "Designation", "Salary", "Date of joining "))
            print("=" * 148)
            Rec = pickle.load(fil)
            c = len(Rec)
            for i in Rec :
                for j in i.values() :
                    print("%15s" %j , end = ' ')
                print()
            print("*"*148)
            print("Records Read :", c)
            
    except EOFError:
        print('*'*148)
        print('Records Read :', c)

    except FileNotFoundError :
        print(F,"File Doesn't exist ")


def DisplayonDesig(F) :
    try :
        with open(F,"rb") as fil :
            Des = ["MGR" , "CLK", "VP","PRES"]
            print("="*148)
            Rec = pickle.load(fil)
            while True :
                D = input("Enter the Designation (MGR/ CLK/PRES/VP)")
                if D.upper() in Des :
                    break
            c = 0
            F = "%15s %15s %15s %15s %15s %15s %15s %15s"
            print(F % ("ID", "NAME", "MOBILE", "EMAIL ADDRESS ", "Dept ID", "Designation", "Salary", "Date of joining "))
            print("=" * 148)
            for i in Rec :
                if i['Desig'] == D.upper() :
                    c += 1
                    for j in i.values() :
                        print("%15s" % j,end = ' ')
                    print()
            print('*' * 148)
            print("Records Read :", c)
            
            
    except EOFError:
        print('='*148)
        print('Records Read :', c)

    except FileNotFoundError :
        print(F,"File Doesn't exist ")


def Update(F) :     #Function to change the details of a customer
    try :
        with open(F,"rb+") as fil :
            found = -1
            Rec = pickle.load(fil)
            A = input("Enter the Emp ID whose details to be changed ")
            for p in Rec :
                if A == p['ID'] :
                    found = 0
                    for i , j in p.items() :
                        if i != 'DOJ' :
                            ch = input("Change " +i+ " (Y/N)")
                            if ch == 'y' or ch == 'Y' :
                                p[i] = input("Enter " +i)
                                p[i] = p[i].upper()
                        elif i =='Sal'  :
                            ch = input("Change " +i+ " (Y/N)")
                            if ch == 'y' or ch == 'Y' :
                                p[i] = float(input("Enter " +i))
                    break
            if found == -1 :
                print("Employee details not found")
            else :
                fil.seek(0)
                pickle.dump(Rec,fil)
                                             
    except EOFError :
        print('Records not Found')

    except FileNotFoundError :
        print(F,"File Doesn't exist ")
        
        
def Delete(F) :
    try :
        with open(F,'rb+') as fil :
            Rec = pickle.load(fil)
            ch = input("Enter the Employee ID to be deleted ")
            for i in range(0, len(Rec)):
                if Rec[i]["ID"] == ch :
                    print("*"*148)
                    F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                    print(F % ("ID", "NAME", "MOBILE", "EMAIL ADDRESS ", "Dept ID", "Designation", "Salary", "Date of joining "))
                    N = Rec.pop(i)
                    for j in N.values() :
                        print("%15s" % j , end = ' ')
                    print()
                    print("Record Deleted")
                    break
            else :
                print("Record Not Found")
            fil.seek(0)
            pickle.dump(Rec, fil)
            
    except FileNotFoundError :
        print(F,"File Doesn't exist ")
    except KeyError :
        print("Record Not Found")
    except IndexError :
        print("Record Not Found")


def SearchAcc(F) :
    try :
        with open(F,'rb') as fil :
            Rec = pickle.load(fil)
            ch = input("Enter the Employee ID to be searched ")
            for i in Rec :
                if i['ID'] == ch.upper() :
                    print("*"*148)
                    F = "%15s %15s %15s %15s %15s %15s %15s %15s"
                    print(F % ("ID", "NAME", "MOBILE", "EMAIL ADDRESS ", "Dept ID", "Designation", "Salary", "Date of joining "))
                    print('='*148)
                    for j in i.values() :
                        print("%15s " % j, end = ' ')
                    print()
                    break
            else :
                print("Record Not Found")
                               
    except FileNotFoundError :
        print(F,"File Doesn't exist ")
   
def SearchName(F) :
    try :
        with open(F,'rb') as fil :
            Rec = pickle.load(fil)
            found = 0
            ch = input("Enter the Customer Name to be searched ")
            print('='*148)
            F = "%15s %15s %15s %15s %15s %15s %15s %15s"
            print(F % ("ID", "NAME", "MOBILE", "EMAIL ADDRESS ", "Dept ID", "Designation", "Salary", "Date of joining "))
            print("*" * 148)
            for i in Rec :
                if i['NAME'] == ch.upper() :
                    found += 1
                    for j in i.values() :
                        print('%15s' % j,end = ' ')
                    print()
            if found == 0 :
                print("Record Not Found")
            else :
                print("Total records displayed :", found)
            
    except FileNotFoundError :
        print(F,"File Doesn't exist ")
    except EOFError :
        print("Record Not Found")


def TOTSal(F) :
    try :
        with open(F,"rb") as fil :
            Rec = pickle.load(fil)
            print("Please note the Gross Salary is calculated on the basis of the following criteris :")
            print("1. HRA  is 38% of Basic Salary ")
            print("2. DA  is 15% of Basic Salary ")
            print("3. TAX deducted is 15% of (Basic + HRA + DA) ")
            print("4. Total Gross Salary is : Basic + HRA + DA - TAX ")
            ch = input("Continue(Y/N) ? ")
            if ch == 'y' or ch == 'Y' :
                F = "%15s %15s %15s %15s %15s %15s %15s"
                print(F % ("ID", "NAME", "Basic Salary ", "HRA", "DA", "TAX", "GROSS SALARY "))
                for i in Rec :
                    HRA = round(38 * float(i['Sal']) / 100, 0) 
                    DA = round(15 * float(i['Sal']) / 100, 0) 
                    TAX = round(((float(i['Sal']) + HRA + DA) * 15/ 100), 0) 
                    GROSS = HRA + DA + float(i['Sal']) - TAX
                    print(F % (i['ID'] , i['NAME'] , i['Sal'] , HRA, DA , TAX, GROSS))
                    
            else :
                print("Going to the main menu")   
           
    except FileNotFoundError :
        print(F,"File Doesn't exist ")


Fi = "Employee"
while True :
    Menu()
    ch = input("Enter your Choice ")
    if ch == '1' :
        Insert(Fi) 
    elif ch == '2':
        SortAcc(Fi)
        Display(Fi)
    elif ch == '3' :
        SortName(Fi)
        Display(Fi)
    elif ch == '4' :
        SortDesig(Fi)
        Display(Fi)
    elif ch == '5' :
        DisplayonDesig(Fi)
    elif ch == '6' :
        Delete(Fi)
    elif ch == '7' :
        Update(Fi)
    elif ch == '8' :
        SearchAcc(Fi)
    elif ch == '9' :
        SearchName(Fi)
    elif ch == '10' :
        TOTSal(Fi)
    elif ch == '11' :
        print("Existing .....")
        break
    else :
        print("Wrong Choice Entered")
        

