class Employee:
	company = "vinsys"
	def __init__(self):#superficial constructor
		print("I was initialized....")
		print(self)
	def __del__(self):#superficial destructor
		print("Destructor called")
	def calculatetax(self):
		print ("calculating tax")
	#def checkpasswd(self):
	#	if self.username == "Abhishek":
		#	print("You got this")
	def __str__(self):
		return "In python  training"
	
emp = Employee()
emp.calculatetax()
print(emp.company)
#inheritance in python
class Manager(Employee):
	def __init__(self):
		super().__init__()
		print("Manager")
		
Manager()
#emp.checkpasswd()
