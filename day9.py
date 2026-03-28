'''
we can store data as key: value
keys are union and we can only give immutable data types 
keys
values---- we all data types (immutable and mutuable)
methods
------ keys ()this method is used to get all keys from the dict
values()---this method is used to get all value from the dict
clear()--- this method is used to delete the dict

sai = {"name":"sai",
           45:89,(4,7):0}
print(sai)

sai={"name": "kalastar",
     "role":"mentor",
     "salary" : 5678}
print(sai.keys())
print(sai.values())
print( sai.clear())
print(sai)

set{}----> set data type is a unordered collection and is never allow duplication
methods
----
union---- this is used add or get 2 different sets without duplication
intersection---this is used to findout common items from the 2 sets
difference --- this method is used to find

sai.clear()
print(sai)

any = {1,2,3,4}
so = {4,5,6}
print(any.union(so))
print(any.intersection(so))
print(any.difference(any))
print(any.pop())
print("the removed inbox value:",any.pop())

#check whether user entered pin is write or wrong

correct_pin = ("1234")
user_pin = input ("enter pin")'''





some = "python is a programming language"
count_ = 0

for j in some:
    if j == " ":
        count_ += 1

print(count_)
