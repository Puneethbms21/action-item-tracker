
'''
x=int(input("Enter the number :"))
y=int(input("Enter the number :"))

if x!=y:
	if x>y:
		print("x is greater")
	elif x<y:
		print("y is greater")
else:
	print("both a equal")
'''
'''
amount=int(input('Enter amount :'))
day=input("enter day :")

if day=="sunday":
	if amount>=5000:
		discount=(amount*10)/100
		amount=amount-discount
		print("after 10% the amount will be :",amount)
	else:
		print("amount must be more than 5000")
else:
	print("please visit on sunday")
'''
'''
x=([1,2,3],[4,5,6],[7,8,9])

for i in x:
	for j in x:
		print(j[0])
'''
'''
list=([1,2,3],[4,5,6],[7,2,9])
for l in list:
	print(l)
list.append(4)
print("list after appending element: ",list)
'''
'''
x=[[1,3],[2,4]]
y=[[8,7],[9,7]]
result= [[0,0],[0,0]]
for i in range(len(x)):
	for j in range(len(x[0])):
		result[i][j]= x[i][j] - y[i][j]
	for r in result:
		print(r)
'''
'''
even = []

for num in range(1, 11):
    if num % 2 == 0:
        even.append(num)

print(even)
'''

'''row = int(input("enter the row num: "))
col = int(input("enter the number of column: "))
print("enter the element for matrix 1: ")
matrix1 = [[int(input()) for i in range(col)] for j in range (row)]
print("matrix: ")
for i in range(row):
	for  j in range(col):
		print("|", matrix1[i][j], "|")
for k in matrix1:
	print("|",k,"|")
print("enter the  column for matrix2: ")
matrix2 = [[int(input()) for i in range(col)] for j in range (row)]
print("matrix: ")
for i in range(row):
        for  j in range(col):
                print("|", matrix2[i][j], "|")
for k in matrix2:
        print("|",k,"|")'''
'''
row = int(input("enter the row num: "))
col = int(input("enter the number of column: "))
print("enter the element for matrix 1: ")
matrix1 = [[int(input()) for i in range(col)] for j in range (row)]
print("matrix: ")
for i in range(row):
        for  j in range(col):
                print("|", matrix1[i][j], "|")
for k in matrix1:
        print("|",k,"|")
print("enter the  column for matrix2: ")
matrix2 = [[int(input()) for i in range(col)] for j in range (row)]
print("matrix: ")
for i in range(row):
        for  j in range(col):
                print("|", matrix2[i][j], "|")
for k in matrix2:
        print("|",k,"|")

matrix = [[1,2],[5,6]]
print("matrix before transpose")
for row in matrix:
	print(row)
result=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
print("matrix after transpose")
for row in result:
        print(row)

'''
'''
amount=int(input('Enter amount :'))
day=input("enter day :")

if day=="sunday":
        if amount>=5000:
                discount=(amount*10)/100
                amount=amount-discount
                print("after 10% the amount will be :",amount)
        else:
                print("amount must be more than 5000")
else:
        print("please visit on sunday")
'''
'''
row = int(input("enter the row num: "))
col = int(input("enter the number of column: "))
print("enter the element for matrix 1: ")
matrix1 = [[int(input()) for i in range(col)] for j in range (row)]
print("matrix: ")
for i in range(row):
        for  j in range(col):
                print("|", matrix1[i][j], "|")
for k in matrix1:
        print("|",k,"|")
print("enter the  column for matrix2: ")
matrix2 = [[int(input()) for i in range(col)] for j in range (row)]
print("matrix: ")
for i in range(row):
        for  j in range(col):
                print("|", matrix2[i][j], "|")
for k in matrix2:
        print("|",k,"|")

matrix = [[1,2],[5,6]]
print("matrix before transpose")
for row in matrix:
        print(row)
result=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
print("matrix after transpose")
for row in result:
        print(row)
'''
name = input("your good name?")
print("hi", name ,"can you please provide the first action item")
deadline = input("what is the deadline of this activity")
datetime_object = datetime.daterime.now()
print(datetime_object)
print("what is the status of the current action item; ")
status = input("enter the status: ")
if status == "inqueue" :
	print("take this project asap")
elif status == "inprogress" :
	print("complete in estimated time")
