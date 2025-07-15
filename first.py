print("hello\nllll") # string \n to next line 
a='''A 
B
C'''
print(a)    # layout

a='Apple'  # extract
print(a[:3])

#n = input("enter:")
#print(n)

#concat
print("a","b") # WITH SPACE 
print("a"+"b") #no space 
print(8,9) # WITH SPACE 
print(8+9) # add 

# def myName():
#     print("ABB")

# myName()

def myFullName(name):
    return name+"dddd" 
print(myFullName("abbs dcf"))


# n = input("enter")
# print(n)

#lambda

x= lambda x:x+10
print(x(5))


fruit =["apple","mango","cherry"]
list(map(lambda x : print(x),fruit)) # list ,fruit lambda

#variable -->not in memory/ dynamic /redeclare /multiple data 
#
#len()
n= "AAAA"
n="BBBB"
print(n) # latest only
n="ccc"

length = len(n)
print(length)

