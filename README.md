# Library_project
mini, mini project using CRUD and DRF. To be updated
ReadMe to be updated soon, will do that ASAP
For now, the sites that can be visited are: 
http://localhost:8000/ -- The front end using HTML templates. It is linked to the other HTML pages, so I neednt mention them here for now.
http://localhost:8000/api/ -- The API view using DRF. This shows all the books present, and has the Create function
http://localhost:8000/api/bd/<book title> -- The API view of each book. Remember: <book title> needs to be replaced 
by a book's title to access. This part has the Update and Delete funtions
http://localhost:8000/api/rest-auth/ -- has options to see: Login, Logout, Register, etc
http://localhost:8000/api/users/ -- Displays all the users
http://localhost:8000/api/users/<int> -- Displays details of each user. Like in Books, CRUD happens for users as well <int to be replaced>
Also, a login/logout at the very top. One needs to Log in, to see any of the stuff. You may log in as the superuser, so create one by CMD:
>>python manage.py createsuperuser


and then, enter the details it asks.
Hope you like this project! It still needs a little bit work on a section, but that is independent of the working of the project.
