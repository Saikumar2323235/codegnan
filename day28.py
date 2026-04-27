'''with open ("demo.txt","r") as any:
    print(any.read())
'''
# regular expressions
'''
---> This regular expression or RegEx is a sequence of characters that forms
     a searching pattern.
---> To use this we have to import re, which will unlock the package

functions
---------
1. findall
---------
--> by using this function , it will find all sequence in the string

syntax->  re.findall(metachar, variable_name)

2. search --> by using this functions , it will only find first sequence in
the string
syntax ->  re.search("metachar", variable_name)

3.metacharacters:
---> meta characters are used to form searching pattern'''
'''
1. square brackets[]
import re
any = "my name is 8 Saikumar 5"
so = re.findall ("[a-z]",any)
an = re.search("[a-z]",any)
print(so)
print(an)

 2. dot(.)

import re
we = "hello"
the = re.findall("h...o",we)
thing = re.search("he..o",we)
print(the)
print(thing)

3. ^
-> this is used to fill the string is starting with sequence or not

syntax-> re.finall ("metachar", variable_name)
'''
'''import re
how = "this is used to find the string"
who = re.findall("this is",how)
then = re.search("^This",how)
print(who)
print(then)'''

#4.dollar $ :
'''
---> this is used to find the string is ending with the sequence or not
syntax -> re.findall("$",variable_name)
'''
'''import re
out = "this is used to find the string is ending"
one = re.findall("sequence $",out)
two = re.search("this $",out)
print(one)
print(two)

#5. astric *:
---> this meta character will form a searching pattern as it will take zero
or more characters.
'''

import re
sai = "This is used to find the string is starting with the zero"
gk = re.findall("c,*i",sai)
nk = re.search("t.*",sai)
print(gk)
print(nk)

#6.plus +
'''
this meta character will form a searching pattern it will take any one or more character for (+)

syntax->re.search(",+", variable_name)'''

sai = "This is used to find the string is starting with the sequence"
gk = re.findall("an.+y",sai)
nk = re.search("i.+",sai)
print(gk)
print(nk)
















































































