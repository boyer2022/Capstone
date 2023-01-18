from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

    def __str__(self):
        return f'Name {self.name}, ID: {self.college_id}, GPA: {self.gpa}'

def main():
    alice = Student('Alice', 12345, 4.0)
    bob = Student('Bob', 98765, 3.2)

    print(alice)
    print(bob)


main()                      # Will not display/run without this line

    