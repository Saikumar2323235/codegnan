'''vowel_con = input("Enter a letter:")
if vowel_con in "AEIOUaeiou":
    print("vow")
else:
        print("con")
Time_aday = input("enter 24hrs time:")
Parts_= Time_aday.split(":")
hours_= int (Parts_[0])
min_= int(Parts_[1])
if hours_>=13 and min_ < 60:
    print(f"{Time_aday} convert into {hours_-12}: {min_}pm")
else:
    print(f"you can entered normal or min are incorrect")



#List ----> different types of data inside [], which are seperated by,
#eg ---> [1,"sandy",4,3]

list_1=[1,2,3,"python",[1,2,["python","java"], "language"]]
print(list_1[4][2][0][4])
  -----------
mutuable ---> can modify or change directly the variable.
immutable ---> cant modify a variable data directly (we can by using another variable)
  append()--- this method is used to add new file in end of the list
  syntax-- variable_name.append(item)
  extend()--
  remove()--
  pop()--this method is used will delete the item or value basedon index position

  
  
list_2=[1,2,3,4,5]
print(list_2)
list_2.append("sai")    
print (list_2)
list_2.extend("sai")

print (list_2)

#remove

list_3=[10,20,30,40]
list_3.remove(10)
print(list_3)

list4=[100,200,300,("sai")]
list4.remove(100)
print(list4)
'''

#pop
list5=[1,2,3,4,5]
list5.pop(1)
print(list5)
