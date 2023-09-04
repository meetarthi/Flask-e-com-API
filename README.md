# Backend api for e-com site 

Web application made using Flask serves as a e-com **API**.  This allows user to register, login, rate the products, sort the products based on rating with **pagination**. This also leverages admin to update the product data in MySQL databases later integrating to the application.  

**Developed using:**
------------
1. **Language** - Python, HTML

2. **Libraries** - flask, pandas, pymysql

3. **Database** - MySQL

**Workflow**
------------
1. Flask installation
2. Create folder- app.py
3. SQL installation
4. Create Database
5. Create Table
6. Create user for Admin access
7. Grant Admin user all permission to the table.
8. Develop API for user registration ,user login, uploading product data by admin, inserting the uploaded product data, enabling user to give rating, sorting review and pagination in app.py.
9. Flask run 

**Application**
------------
1. **User registration**
Api 'register' to get the details for registration from user, GET method with parameters for firstname, lastname, username, and password.
Inserts user information into the app_users table in a MySQL database
![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/466f6451-aaaa-4e56-98ef-91da4d91b511)
![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/ab740e36-ea6f-49cd-818c-ab4dff173ca2)

2. 

