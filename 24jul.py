#reserve 
arr=[1,5,7,9,3]
rearr=arr[::-1]
print(rearr)

#second largest
# arrr= [4,5,7,7,6]   
# ln=[5,7,7,8,3,8,5,9]  
ln=[5,-5]  
f=s=ln[0]
for a in ln:
    if f<a or f==a:
        s=f
        f=a
                
    elif f>a:
        if s<a:
            s=a
print(s)            


#merge 2 sorted list 
arf=[1,2,3,4,5]
ars=[6,7,8,9,10]
ars=sorted(arf+ars)
# for a in ars:
#     arf.append(a)
# print(arf)
print(ars)

# & intersection 
# | Or 



