# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if size == 's':
 bill = 15
   
elif size == 'm':
 bill = 20
  
elif size == 'l':
  bill = 25
if add_pepperoni == 'y' and bill == 15:
  bill +=2
  
elif add_pepperoni == 'y' and bill >=20:
  bill +=3
  
if extra_cheese == 'y':
  bill +=1
  
print(f"your bill is ${bill}") 
# else:
# print('wrong option')






