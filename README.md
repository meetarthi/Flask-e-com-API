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
   3.1 Open sql using sudo mysql
   3.2 Create Database
   3.3 Create Table
   3.4 Create user for Admin access
4. Grant Admin user all permission to the table.
5. Import libraries in app.py
6. API development
   6.1 Create Api for user registration and login.
   6.2 Create a helper front-end to upload product data.
   6.3 Create a Api for admin to upload the product data.
   6.4 Create a Api for inserting the product data into SQL table. 
   6.5 Create a Api enabling user to give rating to products , and updating the rating in the database.
   6.6 Create a Api for Sorting products based on rating and pagination
