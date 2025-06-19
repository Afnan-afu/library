#about

This software is a simple Library Management System designed to manage:

📘 Book details

👥 Library members

🔄 Book rental records

It does not require authentication, as it is intended for offline or internal use only, not for live deployment on the internet.


#All set up

#Book Management
        #Add books = http://127.0.0.1:8000/api/v1/books/add-book/
        #Update book = http://127.0.0.1:8000/api/v1/books/update-book/<id>/  (id of the book)
        #delete book = http://127.0.0.1:8000/api/v1/books/delete-book/<id>/  (id of the book)
    

#Memberhip Management
        #Add Member = http://127.0.0.1:8000/api/v1/members/add-member/
        #All Members = http://127.0.0.1:8000/api/v1/members/
        #Renew Memberhip(month) = http://127.0.0.1:8000/api/v1/members/renew-membership-month/<id>/ (id of the Member)
        #Renew Membership(Year) = http://127.0.0.1:8000/api/v1/members/renew-membership-year/<id>/ (id of the Member)


#Book Rental System
        #Rent Books = http://127.0.0.1:8000/api/v1/books/rent-book/
        #Rental History = http://127.0.0.1:8000/api/v1/books/rented-history/
        #Rent out books = http://127.0.0.1:8000/api/v1/books/rent-out/

#Overdue Handling
        #Over dued books = http://127.0.0.1:8000/api/v1/books/overdue_books/

