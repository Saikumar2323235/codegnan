class Person:
    def __init__(self, Name, Age, Education, ID , Course, Mentor, Institute, Location, Country):
        self.Name = Name
        self.Age = Age
        self.Education = Education
        self.ID = ID
        self.Course = Course
        self.Mentor = Mentor
        self.Institute = Institute
        self.Location = Location
        self.Country = Country
        
    def display(self):
        print("*----------------Student Details----------------*")
        print("Name :", self.Name)
        print("Age :", self.Age)
        print("Education :", self.Education)
        print("ID :", self.ID)
        print("Course :", self.Course)
        print("Mentor :", self.Mentor)
        print("Institute :", self.Institute)
        print("Location :", self.Location)
        print("Country :", self.Country)
p1 = Person("SaiKumar", 22, "B.Tech", 101, "CSE", "G.Bhanu Teja", "[Codegnan]", "Visakhapatnam, Andhrapradesh",
            "India")
p1.display()
