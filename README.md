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
   
Api 'register' to get the details for registration from user, GET method with parameters firstname, lastname, username, and password.

Inserts user information into the app_users table in a MySQL database
![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/466f6451-aaaa-4e56-98ef-91da4d91b511)
![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/ab740e36-ea6f-49cd-818c-ab4dff173ca2)
------------
2. **User Login**
   
GET method with parameters username and password
checks if the username is in the app_users table.
- if not in table, displays 'Not registered'
  
  ![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/4007a946-1de7-450f-bdb6-5998bbed1203)
- if the username is correct, and corresponds to password , displays 'logged in'
  ![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/18409fce-093a-41ed-9ff8-cfd0514eec7f)
- if the username is correct, but DOESN'T corresponds to password , displays 'Password incorrect'
  ![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/a09ed37d-fb6c-4a9f-8bea-666de5a404e5)

------------
3. **Helper Front-end**

Front-end to upload product data by admin.

![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/30a85e7a-96a1-4899-a637-a5f8b29ae305) 

------------

4. **Upload the product data**
Using POST method, uploads the csv file, reads and converts to dataframe.
Calls the **insert_pd_to_sql function** to insert the DataFrame data into the products table in the database and returns'done'.

![image](https://github.com/meetarthi/marlo-assignment/assets/112666126/793cdd75-5ff3-45b8-876d-ceb4f60fc71e)

------------
5.**Insert product data into table 'products'**

**insert_pd_to_sql**  function inserts data from pandas dataframe into products table, iterates through each row of the dataframe and inserts into the table.

------------ 

