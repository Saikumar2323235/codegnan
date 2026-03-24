'''
String ---> A string is a collection of characters.
It is represented using single quotes (' ') or double quotes (" ").

We can access characters using indexing and slicing.

Strings are immutable, meaning we cannot modify the original string directly.
Instead, operations like replace() return a new string.


# Assign a string value to a variable
text = 'Python Programming'

# Replace 'Python' with 'Java' (creates a new string)
new_text = text.replace("Python", "Java")

# Print the original string
print(text)

# Print the modified string
print(new_text)
any = 'python programming'
print(any[5])
a_day = "I'm Saikumar from visakhapatnam,have 1 year experience of python"
print(f" my name is {a_day[6:12]}")

any = "I am going to tour"
print(f" we have dropped the {any[14:19]}")

any= "i am going to home"
print(len(any))

note :- we can convert a string into integer , if contains only integer value...


methods of string

split()--> removes space and the list [] it will give seperate


some = "python is a programming language"
print(some.split("a programming"))

lower()--> this is used to convert all letter into lower cases


some = "python IS a Programming lANGUAGE"
print(some.lower())

sum = "my name is MVV"
print (sum.upper())


upper syntax

REPLACE syntax


sum= "python is a programming language"
print (sum.replace("programming","regular"))
'''

