Pwd_Key = 4 #modify to set personalised Key

#Function to Encode the user given data
def Cipher(Text) :
    
    Cipher_Text = ''    
    for i in Text:
        a = chr(ord(i) + Pwd_Key )
        Cipher_Text += a
    
    T = Cipher_Text + '\n'
    return T

#Function to store the encrypted data.
def Entry(Data):
	file = open('Data.txt', 'a')
	file.write(Data)
	print('\nEntered data has been successfully encrypted and recorded..!!!\n')
	file.close()
'''

print(En_Data)
'''
#Function to display the encrypted data.
def Extract():

	En_Records,De_Records = [],[]

	file = open('Data.txt', 'r')
	x = file.readlines()

	for i in x:
		En_Records.append(i)

	for i in range(0,len(En_Records)):
		En_Text = En_Records[i]
		De_Text = ""

		for j in range(0, len(En_Text)):
			De_Text += (chr(ord(En_Text[j]) - Pwd_Key))

		De_Records.append(De_Text)

	file.close()

	return De_Records


while(True):
	print(" 1 -> Enter Data ")
	print(" 2 -> Display Stored Data ")
	print(" 0 -> Exit \n")

	opt = int(input("Enter the option : "))
	print("\n")

	if opt == 1 :
		Data = input("Enter your data :\n")
		En_Data = Cipher(Data)
		Entry(En_Data)

	elif opt == 2 :
		user_key = int(input("Enter the Key to decrypt : "))

		if user_key == Pwd_Key :
			L = Extract()
			for i in range(0,len(L)):
				print(L[i][:-1])
			print("\n")
			
		else :
			print("Wrong key !! ")

	elif opt == 0 :
		exit()

	else :
		print("Enter valid option !!")








