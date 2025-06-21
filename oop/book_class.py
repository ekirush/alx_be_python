'''
Master Python magic methods by implementing a Book class 
that incorporates constructors (__init__), destructors (__del__), 
and the representation methods (__str__ and __repr__).

Create a Python script named book_class.py. 
In this script, define a Book class that uses specific magic methods to enhance its functionality. 
This class will model a book with attributes for the title, author, and publication year
'''
class Book:
    def __init__(self, title:str, author:str, pub_year:int):
        self.title = title
        self.author = author
        self.pub_year = pub_year
    
    def __del__(self):
        print(f"Deleting {self.title}")
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.pub_year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pub_year})"