#defining the Student class
class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def change_grade(self, new_grade, grade_to_adjust):
        self.grades[grade_to_adjust] = new_grade

    def change_name(self, new_name, name_part):
        if name_part == "first_name":
            self.name[0] = new_name
        elif name_part == "last_name":
            self.name[1] = new_name


    def average_grade(self):
        average_grade = 0
        for grade in self.grades:
            average_grade += grade
        return average_grade / len(self.grades)

    def name_value(self):
        #step 1: make full name
        full_name = ""
        for name_part in self.name:
            full_name += name_part
        #step 2: make full name lower case
        full_name = full_name.lower()
        #step 3: loop over each character in full name and add to name value
        name_value = 0
        for char in full_name:
            name_value += ord(char) - 96
        return name_value

    #andere manier van x += y -> x = x + y

def change_grade(student, new_grade, grade_to_adjust):
    student.change_grade(new_grade, grade_to_adjust)

def change_name(student, new_name, name_part):
    student.change_name(new_name, name_part)

def average_grade(student):
    return student.average_grade()

def name_value(student):
    return student.name_value()

if __name__ == "__main__":
    student1 = Student(["Lucas", "Senden"], [7, 8, 8, 4])
    name_value = name_value(student1)
    average = average_grade(student1)
    change_name(student1, "Fernandez", "last_name")
    change_grade(student1, 4.5, 1)
    student1.change_grade(3.5, 2)
    change_name(student1, "Laura", "first_name")

    print("for debug purposes :)")
