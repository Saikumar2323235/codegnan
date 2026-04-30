'''def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern, name)

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return  re.fullmatch(phone)
def validateph(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern,phone)
def validatepass(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern,password)
def main():
    name = input()
    email = input()
    phone = input()
    password = input()

    if not validatename(name):
        print("invalid name")
    elif not validateemail(email):
        print("invalid name")
    elif not validateph(phone):
        print("invalid phone number")
    elif not validatepass(password):
        print("invalid password")
    else:
        print("all inputs are valid form submitted successfully")


                            Data Analysis
why it is need ?
--> this is critical because it converts raw data into actionable
insighs, enabling information to decision to decision making easy and improve
operational efficiency...
1.Decision-making
2. improved operational efficency
3. customer understanding
4. market insights
5. risk Management
6.data-driven startegies
7. 

pip install matplotlib
'''
'''
import matplotlib.pyplot as pit
x = [1,2,3,4]
y = [10,20,30,40]
pit.plot(x,y)
pit.show()
'''

'''
import matplotlib.pyplot as plt

plt.plot([1,2,3], [4,5,6])
plt.show()'''

'''import sys

# add matplotlib path manually
sys.path.append(r"C:\Users\HP\AppData\Roaming\Python\Python313\site-packages")

# remove current folder (fix string.py issue)
sys.path = [p for p in sys.path if "codegnan" not in p]

import matplotlib.pyplot as plt
'''

import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[43,62,86])
plt.title("car sales")
plt.xlabel("years")
plt.ylabel("cars sold")
plt.show()



















































        
