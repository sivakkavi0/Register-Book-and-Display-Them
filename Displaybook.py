class Library:
    def __init__(self):
        self.bookname=""
        self.author=""
    def getdata(self):
        self.bookname=input("Enter Name of the Book : ")
        self.author=input("Enter Author of the Book : ")
    def display(self):
        print("Name of the Book : ",self.bookname)
        print("Author of the Book : ",self.author)
        print("\n")

book=[]
ch='y'
while (ch=='y'):
    print("1.Add New Book \n 2.Display Books")
    resp=int(input("Enter Your Choice : "))
if (resp==1):
    L=Library()
    L.getdata()
    book.append(L)
elif(resp==2):
    for x in book:
        x.display()
else:
    print("Invaid Input .......................")

ch=input("Do you want Continue..... y")
        
    
