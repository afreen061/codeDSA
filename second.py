# int
# string
# bool
#float
#substring
#[-1]
#type
#typecaste
#str+int==>error
#a//b==>floor without decimal ==>
#2**3==>8
#(),**,* or /,+ or -
#round() 3.3/3.9 round(n,2) 2 decimal
#+=
#f not + 
# typestring = str(35435)
# print(type(typestring))

# print(3*3+3/3-3)
#$

# print("Welcome to tip calculator")
# totalbill=float(input("What is total bill?"))

# tip=float(input("How much tip would you like to give?"))

# tipsplit=int(input("How many people to split the bill?"))
# payable = (totalbill + (totalbill*tip/100))/tipsplit
# print(f"each person should pay:${round(payable,2)}")
# payable=2

# if payable >=7 :
#     print("i will pay")
# elif payable <7 :
#     print("you will pay")    
# else :
#     print("bye")


print("Welcom to the Pizza order.")
size=input("Which Size S,M,L?")
pepperoni=input("Do add Pepperoni Y ,N?")
Extra=input("Do add Extra cheese Y ,N?")
price=0
if size =="S":
    price+=15
    if pepperoni=="Y":
        price+=2
    if  Extra =="Y":
        price+=1
elif size =="M":  
    price +=20
    if pepperoni=="Y":
        price+=3
    if  Extra =="Y":
        price+=1   

else: 
    price +=25
    if pepperoni=="Y":
        price+=3
    if  Extra =="Y":
        price+=1         
print(f"price is {price}:")        

#and or not 
   











































































































































































































































