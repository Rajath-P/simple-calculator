def add(n1,n2): 
  return n1+n2

def sub(n1,n2):
  return n1-n2

def div(n1,n2):
  return n1/n2

def multi(n1,n2):
  return n1*n2

print("1-Addition")
print("2-Subtraction")
print("3-Division")
print("4-Multiplication")
ch=int(input("Select the airthmetic operation(1,2,3,4):"))

if(ch==1):
  print("Your choice is ADDITION")
  n1=float(input("Enter 1st number for addition:"))
  n2=float(input("Enter 2nd number for addition:"))
  print("RESULT=",add(n1, n2))

elif(ch==2):
  print("Your choice is SUBTRACTION")
  n1=float(input("Enter 1st number for subtraction:"))
  n2=float(input("Enter 2nd number for subtraction:"))
  print("RESULT=",sub(n1, n2))

elif(ch==3):
  print("Your choice is DIVISION")
  n1=float(input("Enter 1st number for division:"))
  n2=float(input("Enter 2nd number for division:"))
  print("RESULT=",div(n1,n2))

elif(ch==4):
  print("Your choice is MULTIPLCATION")
  n1=float(input("Enter 1st number for multiplication:"))
  n2=float(input("Enter 2nd number for multiplication:"))
  print("RESULT=",multi(n1,n2))

else:
  print("Invaild choice")


