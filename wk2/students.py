# Classes
class Student:
    def __init__(self, name, school_id, gpa):           # 2 underscores on each side of init
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

# New student objects
alex = Student('Alex', 'abcdef', '3.2')
print(alex.name)
print(alex.school_id)
print(alex.gpa)
print(alex)

sam = Student('Sam', '12345', '4.0')
print(sam.name)
print(sam.school_id)
print(sam.gpa)
print(sam)

# Author class example
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
       # if self.books:                              # Empty list are False, list with objects are True
        book_list = ', '.join(self.books) or 'No books'
        # else:
        #     book_list = 'No book list.'
        return f'Name: {self.name} Books Published: {book_list}'
    
    # if statement way
        # if self.books:                              # Empty list are False, list with objects are True
        #     book_list = ', '.join(self.books)
        # else:
        #     book_list = 'No book list.'
        # return f'Name: {self.name} Books Published: {book_list}'

shakespeare = Author('William Shakespeare')
shakespeare.publish('Hamlet')
shakespeare.publish('Richard III')
shakespeare.publish('McBeth')

print(shakespeare)

matt = Author('Matt')
print(matt)


# PowerPoint example:
# print('PowerPoint example')

# class Author:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def publish(self, title):
#         self.books.append(title)

#     def __str__(self):
#         titles = ', '.join(self.books) or 'No published books'
#         return f'{self.name}. Books: {titles}'

# def main():
    
#     rowling = Author('J. K. Rowling')
#     rowling.publish('Harry Potter and the Philosopher\'s Stone')
#     rowling.publish('Fantastic Beasts and Where to Find Them')
#     print(rowling)

#     matt = Author('Matt')
#     print(matt)

# main()