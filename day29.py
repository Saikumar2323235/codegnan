#7.?
'''--> this meta character will form a searching pattern as it will taken any even or one character for(?)

syntax --> re.findall(".?",Variable_name)'''
'''
import re
any = "This meta character"
an = re.findall("Th.?",any)
print(an)

#8.{}
-----
this meta character will form a searching pattern as we can mention the size in the {}
syntax --> re.search(".{size}",variable)
'''

'''import re
any = "This meta character will form a searching pattern as it will take any zero or one character for"
an = re.findall(".{25}",any)
print(an)

#9.|(pipe
)
--- this meta character will form a searching pattern as it consider right
or left any string is present or not for (|)
'''
'''import re
any = "This meta character will form"
an = re.findall("that|will",any)
print(an)

#10 special sequence
a special sequence is a\ followed by one of the characters in the list below, and has special meaning

 special meaning:
 ----
\A
returns a match if the specified characters are the beginning
of the string
eg : "\AThe"
'''
'''import re
txt = "The rain in Spain"

# Check if the string starts with "The"
x = re.findall(r"\AThe", txt)

print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")
'''

'''\b-Returns a match where the specified characters are at the
beginning or at the end of a word
Eg:
r"\bain"'''

'''import re

txt = "The rain in Spain"

# Check if is presented at the beginning of a word:
x = re.findall(r"\BThe", txt)
print(x)
if x:
    print("Yes, there is a at least one match!")
else:
    print("No match")
----------------------------------------------------------------   '''
'''
#d
import re

txt = "The rain in 56 Spain"

# Check if the string contains any digits (numbers from 0-9):
x = re.findall(r"\d", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

-------------------------------------------------------------------

import re

# \D → returns non-digit characters
txt = "the rain in 56 spain"

x = re.findall(r"\D", txt)
print(x)

if x:
    print("Yes, there is at least one match")
else:
    print("No match")

----------------------------------------------------------------------    
'''
'''Time and Date


%d-Day (01–31)
%m-Month (01–12)
%Y-Year (e.g., 2026)
%H-Hour (00–23)
%M-Minutes
%S-Seconds
%p-AM / PM
%A-Full Day Name (Monday)
%B-Full Month Name (April)
'''

import datetime

# Current date and time
now = datetime.datetime.now()
print(now)

# Only current date
today = datetime.date.today()

# Different formats
print(today.strftime("%d-%m-%Y"))  # Day-Month-Year
print(today.strftime("%A"))        # Day name
print(today.strftime("%B"))        # Month name
