
#Function to calculate x raised to the power y
def Power( x , y ) :

	if (y == 0) :
		return 1

	else :

		ans = x**y 
		return ans


#Function to convert Binary to Decimal
def BinaryToDecimal( n ) :

	ans = 0
	x   = 1
	m = int(n)

	while m > 0 :
		b   =  m%10
		ans += b*x
		x   =  x*2
		m   =  m//10

	return ans


#Function to convert Octal to Decimal
def OctalToDecimal( n ) :

	ans = 0
	x   = 1
	m = int(n)

	while m > 0 :
		b   =  m%10
		ans += b*x
		x   =  x*8
		m   =  m//10

	return ans


#Function to convert Hexadecimal to Decimal
def HexadecimalToDecimal( n ):

	ans = 0
	x   = 1
	s = len( n )
	
	for i in range( s-1 , -1 , -1 ) :
		if n[i] >= '0' and n[i] <= '9' :
			ans += x*(int(n[i]))

		elif n[i] >= 'A' and n[i] <= 'F' :
			ans += x*(ord(n[i]) - ord('A') + 10)

		x = x*16

	return ans


#Function to convert Decimal to Binary
def DecimalToBinary( n ) :
	L = []
	while(n>0):
		rem = n%2
		L.append(rem)
		n = n//2
	#L = L[::-1]

	dec = 0
	for i in range(0,len(L)):
		dec = dec + L[i]*(10**i)

	return dec

#Function to convert Decimal to Octal
def DecimalToOctal( n ) :
	
	ans   = 0
	count = 0

	while (n > 0) :
		lastDigit =  n%8
		ans       += lastDigit*(10**(count))
		n         =  n//8

		count     += 1

	return ans


#Function to convert Decimal to Hexadecimal
def DecimaltoHexadecimal( n ) :

	ans = ''

	while (n > 0) :
		lastDigit = n%16
		if (lastDigit >= 0 and lastDigit <=9 ) :
			ans = ans + str(lastDigit)

		elif (lastDigit >= 10 and lastDigit <= 15) :
			a = chr(ord('A') + (lastDigit-10))
			ans = ans + a

		n = n//16

	return ans[::-1]

while True:
	print('1 -> Calculate Exponents')
	print('2 -> convert Binary to Decimal ')
	print('3 -> convert Octal to Decimal ')
	print('4 -> convert Hexadecimal to Decimal ')
	print('5 -> convert Decimal to Binary ')
	print('6 -> convert Decimal to Octal ')
	print('7 -> convert Decimal to Hexadecimal ')
	print('0 -> Exit')
	

	n = int(input('\nEnter: '))

	if n == 1:
		a,b = int(input("Enter Base :\n")),int(input("Enter Superscript : \n"))
		print("The result is : ",Power(a,b), "\n")

	elif n == 2:
		b = int(input("Enter Binary Number:\n"))
		print("Corresponding Decimal Number is : ", BinaryToDecimal(b), "\n")

	elif n == 3:
		b = int(input("Enter Octal Number:\n"))
		print("Corresponding Decimal Number is : ", OctalToDecimal(b), "\n")

	elif n == 4:
		b = (input("Enter Hexadecimal Number:\n"))
		print("Corresponding Decimal Number is : ", HexadecimalToDecimal(b), "\n")	

	elif n == 5:
		b = int(input("Enter Decimal Number:\n"))
		print("Corresponding Binary Number is : ", DecimalToBinary(b), "\n")

	elif n == 6:
		b = int(input("Enter Decimal Number:\n"))
		print("Corresponding Octal Number is : ", DecimalToOctal(b), "\n")

	elif n == 7:
		b = int(input("Enter Decimal Number:\n"))
		print("Corresponding Hexadecimal Number is : ", DecimaltoHexadecimal(b), "\n")

	elif n == 0:
		
		exit()

	else:
		print("\nNo such option exists!! ")


