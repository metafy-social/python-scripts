import csv 

def check_unique_Product_ID(Product_ID) :

	file = open('ProductRecords.csv','r',newline = '')
	Reader_obj = csv.DictReader(file)
	count = 0

	for line in Reader_obj :
		if line['Product_ID'] == Product_ID :
			count += 1												

	if count == 0:
		return Product_ID   										

	else:
		print('The Product_ID already exists..!!')
		print()
		Product_ID = input('Enter unique Product ID: ')				
		return check_unique_Product_ID(Product_ID)					

	file.close()


def Entry():
	Data = []
	Product_ID = (input('Enter the ID of the Product: '))
	Data.append(check_unique_Product_ID(Product_ID))				
	
	Product_Name 	 = input('Enter the Name of the Product: ')
	Product_Price 	 = int(input('Enter the Price of the Product: '))
	Product_Quantity = int(input('Enter the Quantity of the Product: '))
	
	Data.extend([Product_Name, Product_Price, Product_Quantity])	
	
	file = open('ProductRecords.csv', 'a',newline = '')
	writer_obj = csv.writer(file)					
	writer_obj.writerow(Data)										
	file.close()
	print('Entered data has been successfully recorded..!!!')
	print()

def Extract_Data(Product_ID) :										
	print()
	file = open('ProductRecords.csv','r',newline = '')
	Reader_obj = csv.DictReader(file)

	for line in Reader_obj:
		
		if line['Product_ID'] == str(Product_ID):					
			for i in line.keys() :
				
				print(i , ':' , line[i])							

	file.close()
	print()


def Extract_Quantity(Product_ID) :
	print()
	file = open('ProductRecords.csv','r',newline = '')
	Reader_obj = csv.DictReader(file)
	for line in Reader_obj:
		
		if line['Product_ID'] == str(Product_ID):					
			print('Quantity of',										
				line['Product_Name'] ,
				':',
				line['Product_Quantity'])							
	file.close()
	print()

def Delete_Record(Product_ID) :
	file = open ('ProductRecords.csv','r+',newline = '')
	Reader_obj  = csv.reader(file)
	records = [row for row in Reader_obj][1:]
	temp_records = []												

	for record in records:
		if record != []:
			if record[0] != Product_ID and record != [] :
				temp_records.append(record)							
	file.close()

	file = open ('ProductRecords.csv','w+',newline = '')
	writer_obj = csv.writer(file)
	writer_obj.writerow(['Product_ID','Product_Name','Product_Price','Product_Quantity'])
	writer_obj.writerows(temp_records)								
	print('Record deleted successfully.')
	file.close()


def Update_Price(Product_ID,New_Price) :
	file = open('ProductRecords.csv','r')
	Reader_obj = csv.DictReader(file, fieldnames = ['Product_ID','Product_Name','Product_Price','Product_Quantity'])

	Temp_records = []												
	for line in Reader_obj :
		Temp_records.append(line)

	file.close()

	for record in Temp_records :
		if record['Product_ID'] == Product_ID :
			record['Product_Price'] = New_Price						

	Temp_records = Temp_records[1:]
	file = open('ProductRecords.csv','w+',newline = '')
	Writer_obj = csv.DictWriter(file, fieldnames = ['Product_ID','Product_Name','Product_Price','Product_Quantity'])
	Writer_obj.writeheader()
	Writer_obj.writerows(Temp_records)								
	file.close()
	print('Price has been Updated successfully !!!')


def Update_Quantity(Product_ID,New_Quantity) :
	file = open('ProductRecords.csv','r')
	Reader_obj = csv.DictReader(file, fieldnames = ['Product_ID','Product_Name','Product_Price','Product_Quantity'])

	Temp_records = []												
	for line in Reader_obj :
		Temp_records.append(line)

	file.close()

	for record in Temp_records :
		if record['Product_ID'] == Product_ID :
			record['Product_Quantity'] = New_Quantity				

	Temp_records = Temp_records[1:]
	file = open('ProductRecords.csv','w+',newline = '')
	Writer_obj = csv.DictWriter(file, fieldnames = ['Product_ID','Product_Name','Product_Price','Product_Quantity'])
	Writer_obj.writeheader()
	Writer_obj.writerows(Temp_records)								
	file.close()
	print('Quantity has been Updated successfully !!!')


while True: 														

	print()
	print('Press 1 to Insert Product Details: ')
	print('Press 2 to Fetch Product Details using Product_ID: ')
	print('Press 3 to Fetch Quantity of the Product using Product_ID: ')
	print('Press 4 to Delete Product Details using Product_ID: ')
	print('Press 5 to Update Product Price using Product_ID: ')
	print('Press 6 to Update Product Quantity using Product_ID: ')
	print('Press 0 to Exit: ')
	print()

	Answer = int(input('Press desired number: '))

	if Answer == 1 :
		n = int(input('Enter the number of entries to be entered: '))
		for i in range(n):
			Entry()

	elif Answer == 2 :
		Product_ID = input('Enter the Product ID: ')
		Extract_Data(Product_ID)

	elif Answer == 3 :
		Product_ID = input('Enter the Product ID: ')
		Extract_Quantity(Product_ID)

	elif Answer == 4 :
		Product_ID = input ('Enter the ID of the product to be deleted : ')
		Delete_Record(Product_ID)
	
	elif Answer == 5 :
		Product_ID = input('Enter the Product ID: ')
		New_Price  = int(input('Enter the New Price of the Product: '))
		Update_Price(Product_ID,New_Price)

	elif Answer == 6 :
		Product_ID = input('Enter the Product ID: ')
		New_Quantity  = int(input('Enter the New Quantity of the Product: '))
		Update_Quantity(Product_ID,New_Quantity)

	elif Answer == 0 :
		print('Thank You !!')
		exit()

	else:
		print('No such option exists..!!')
		exit()

  