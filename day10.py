'''any_ = "python is a programming language"

vowel_cou = 0
space_cou = 0
for j in any_:
    if j in "AEIOUaeiou":
        vowel_cou += 1
    elif j == " ":
        space_cou += 1
    

print(f"this is count of all vowel in the string {vowel_cou}")
print(f"this is the count of all space in the string {space_cou}")
print(f"count of all cons_ in the string{len(any_)- (vowel_cou + space_cou)}")


a=9
print(b)
for j in range (1,10):
    print(j)


range ()---> this is used to generate the number
syntax ----> range (start, end,step)

for j in range(2,20,6):
 print(j)

any = "123"
print(int(any))
print(list(any))
print(tuple(any))

an=[2,3,4]
vs= str(an)
print(type(vs))
print(vs)
print(tuple(an))

ab =[(2,3),(4,5)]
print(dict(ab))


rev_str="saikumar"
empty_=""
for j in rev_str:
    empty_ = j + empty_
    print (empty_)
    
rev_str ="sis"
empty_= ""
for j in rev_str:
    empty_=j+ empty_
if empty_== rev_str:
    print(f"{rev_str}is palin")
else:
        print(f"{rev_str} is not a palin")

'''

for number in range(1,100):
    if number % 2 == 0:
        print (f"{number} is a even number")
    else :
        print (f"{number} is a odd number")
