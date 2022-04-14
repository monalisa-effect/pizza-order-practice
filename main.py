# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == 's':
 size = 15
   
elif size == 'm':
 size = 20
  
elif size == 'l':
  size = 25
if add_pepperoni == 'y' and size == 15:
  size +=2
  
elif add_pepperoni == 'y' and size >=20:
  size +=3
  
if extra_cheese == 'y':
  size +=1
  
print(f"your bill is ${size}") 
# else:
# print('wrong option')






