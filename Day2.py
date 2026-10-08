"""
name="Codegnan"
age=8
place="Vizag"
print(name)
print(age)
email_id="saketh@codegnan.com" #snakecase Convention (multiple words)
print(email_id)
branch_1="Vijayawada"
print(branch_1)

#True = 45 #as True is a keyword we cannot use as a variable
name,email_id,mobile,gender = "Saketh","saketh@codegnan.com",8106429771,"Male"
print(name,mobile)


name="Codegnan" ,age=8, place="Vizag"
print(name,age)

#Deletion ---->
del age #permanent deletion
del name,place

"""
""""

#Swapping of variables
a,b=15,25
print(a)
print(b)
a,b=b,a #value of a will become b
print(a)
print(b)

c=a  #reassigning the existing value to a new variable
print(c)

#Literals ---> These are constants such as numbers (int,float,complex)
#"Hello" "Good"
age=32
print(age)
taste="Bad"
print(taste)
price=115.45
print(price)
print(type(price)) #it returns the type of object
#type() is very very imp
print(type(age))
"""
#Identifiers ---> names given to variables,functions,classes,objects,modules

#Punctuators ---> [] ---> Lists,()-->Tuples,{} -->Dictionaries,Sets
#Operators ---> There are Different type of operators----> Operations
#+,-,*,**,/  (Arthematic Operators),//,%
a=5
b=3
print(a/b) #Float Division (answer is always in float value)
print(a//b) #Flooring Division (Integer Division) returns quotient
print(a%b) #Modulus --->returns remainder

#Raju purchased Shoes with price  1000,discount 15%,
#now how much Raju has to pay?

price=1000
discount=0.15
final_price=price - (price*discount)
print(final_price)





#Vijay went to hotel for dinner his bill is 2500,GST


bill=2500
gst=0.5
discount=0.5
Total_Bill=bill+(bill*gst)
Total_Bill=Total_Bill+(Total_Bill*discount)
print(Total_Bill)

















