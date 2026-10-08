"""
Datatypes -->Numeric Datatypes ---> int,float,complex
---> Boolean datatype --->True/False
None type
--->Sequences --->str,lists[],tuples(),sets set(),mappings (dictionaries)
{}Frozenset

#Lists ----> A list is an Ordered,Mutable,indexed and heterogeneous collection
#we use [] to represent lists
#Students details,Order details,Stock entries.....
details = [1,'saketh','PFS7,'Vizag',56.7]
print(len(details))
print(type(details))

stu_ids=['CGVI0134','CGVI0136']
#print(stu_ids[1])
stu_ids[0]='codegnan'   #here we are using indexing
print(stu_ids)

#Tuples are also immutable ,Ordered,Indexed and Herterogenous
#collections,we use () Paranthesis
#dimensions,coordinates

places=('hyderabad','vizag','vijayawada')
print(places)
print(len(places))
places[0]='chennai'
print(places)

dimensions=10,20,30    #by default it becomes a tuple
print(dimensions)
print(type(dimensions))

#Sets---> A set is a unique collection(removes duplicates)
#A set is n unordered,Unindexed,Mutable collection
ids=set()  #empty set
print(ids)
ids=set([123,134,135,123])
print(ids)
courses={'PFS','JFS','DA'}
print(courses)
print(type(courses)) #A set is unordered there is no index

#Dictionaries --->A dictionary (mapping object) is a collection of
#key value pairs --->dict={k:v},we access only by keys (indexed by keys)
#Dictionary is also mutable collection
details = {'Branch':'Vizag',


                'Course':'PFS',
                'count':19}

print(details)
print(type(details))
print(len(details))
print(details['batch']) #we can access by giving only keys

#Every built-in datatype is a built-in function
#int,float,complex,bool,str,list,tuple,set,dict
#Lists--->tuples,sets,dict,str
marks = [35,24,54]
a=tuple(marks)
print(a)
b=set(marks)
print(b)
c=str(marks)
print(c)
print(len(c))

a=(1,2,3,4)
b=tuple(a)
print(b)
print(type(b))

marks=[35,24,54]
#d=dict(marks) #its not possible like this
e=dict.fromkeys (marks)    #we  not to use fromkeys()
print(e) 

#Tuple ---->list,set,str,dict
#Sets-----> list,tuple,str,dict


#Dictionaries --->  lists,tuples,sets
ids={1:123,2:124}
a=list(ids) #it will only fetch keys
print(a)
b=tuple(ids)
print(b)
c=set(ids)
print(c)
d=str(ids) #every symbol/object will be a character
print(d)
print(len(d))

"""
#Frozensets----> It is an immutable set,unindexed,unordered
#we can typecase it to list,tuple,set
a=frozenset((12,32,12,32))
print(a)
print(type(a))
print(len(a))
b=list (a)
print(b)
c=tuple(a)
d=set(a)
e=dict.fromkeys(a)
f=str(a)
print(c,d,e,f)
print(len(f))

d='Tony Stark'
e=list(d)
f=tuple(d)
g=set(d)
h=dict.fromkeys(d)
print(e,f,g,h)


















