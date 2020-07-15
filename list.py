# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

list=[1,2,3,4,5,6,"Anmol","Anshu","Tridib","muskan","ankit","komal"]
# A list is an ordered sequence that can be indexed, sliced

#declare
list1=[1,"B","C",22]
print(list1)
#update
list1[1]=7
# while updating, data type doesnt matter
print(list1)
#del
del list1[2]
print(list1)
#concat
list2=["tom",10,"fluffy"]
list3=["bella",3,"angry"]
listcomb=list2+list3
print(listcomb)

#multiply 
#with string, multiply is actually repetition
#basic with integer
print(list2[1]*3)
print(list2*2)

#slicing in list
print(len(list))
print(list)
val="komal_Anshu"
print(val[-1:])
print(list[-1:])
print(list[2:5])
print(list[-10:-1])

# traversing around the list 
for x in list2:
    print(x)

list=[1,2,7,3,4,5,6,3,4,5,6,5]
print(list)
del list[2]
print(list)

    




