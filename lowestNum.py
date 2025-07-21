arrayNum = []
for i in range(5):
    a=int(input("enter"))
   
    arrayNum.append(a)
min_num=arrayNum[0]
for j in arrayNum:
    if j < min_num:
       min_num = j

print(min_num)    

