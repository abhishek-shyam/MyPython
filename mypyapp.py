list_of_users = ["abhishek","a","b"]

for user in list_of_users:
	print(user)

print("End Application***********");
print("***Globals***");
print(globals())

def do_something():
	print("doing something")
	return 10394

def calculate_tax(a):
	print(a)

def manage_user(b,p,a=10):
	print(a)

do_something()
calculate_tax(100)
manage_user(100,30)

def my_callback():
	print("I am a callback")
def my_sample(a):
	a()

my_sample(my_callback)

def my_otherfunc():
	def some_other():
		print("The other function")
	return some_other

my_otherfunc()()

#-----------------------------------------
def some_function_with_params(a,b=10):
	print(print(a))

some_function_with_params(b=100,a=20)

#--------------------------------------------
file = open(file="C:/Newairports.txt",mode="rt",encoding="utf-8")
line = file.readline()
while(line):
	split_line = line.split(",")
	for data in split_line:
		print(data)
	line=file.readline()
#-----------------------------------------------
file = open(file="C:/Newairports.txt",mode="wt",encoding="utf-8")
data = "my_info"
file.write(data)
file.close()

#---------------------------------------------------
def count_airports(filename):
	small_airport = 0
	heliport = 0
	closed = 0
	file = open(file=filename, mode="rt", encoding="utf-8")
	line = file.readline()
	while(line):
		split_line = line.split(",")
		for data in split_line:
			if data.count("small_airport") >0:
				small_airport+=1
			elif data.count("heliport") >0:
				heliport+=1
			elif data.count("closed") >0:
				closed+=1
		line = file.readline()

	print("Small Airports",small_airport)
	print("Heliports",heliport)
	print("Closed Airports",closed)

count_airports("C:/airports.csv")

#--------------------------------------------------
	

