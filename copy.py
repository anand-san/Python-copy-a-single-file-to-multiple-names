import shutil
#Output file names
id = ("1541012007","1541012014","1541012024","1541012026","1541012034","1541012041","1541012044","1541012046","1541012080","1541012088","1541012096","1541012101","1541012103","1541012104",) 
print("In case you are facing problems , Please raise an issue at https://github.com/seanjin17")
src=input("Enter file name with extension (File must be in same path): ")
dst=input("Enter Output Extension followed by (.) : ")
for i in id:
	try:
		print("copying "+i)
		shutil.copy2(src, i+dst)
	except:
		print("Please check Your source file location \n Something went wrong")