grade=input("Enter the grade of the employee :")
sal=int(input("Enter the Employee Salary :"))
if(grade=='A'):
    bon=(5/100)*sal
elif(grade=='B'):
    bon=(10/100)*sal
else:
    print("Invalid Employee Grade...")
if(sal<10000):
    bon=bon+(2/100)*sal
print("Salary :",sal)
print("Bonus :",bon)
