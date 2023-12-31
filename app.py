from flask import Flask, jsonify, request
from fileinput import filename
from flask import * 
import pymysql.cursors
import pandas as pd

app = Flask(__name__)



#1. Registration API
@app.route('/register',methods=['GET'])
def register():
    firstname = request.args.get('firstname', type = str)
    lastname = request.args.get('lastname', type = str)
    username = request.args.get('username',type= str)
    password = request.args.get('password', type= str)

    connection = pymysql.connect(host='localhost', user='USERNAME', password='PASSWORD', database='MarloDB', cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO app_users VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (firstname, lastname, username, password))
        connection.commit()
    return jsonify({'INSERTED': True})



#2. Login API
@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username', type= str)
    password = request.args.get('password', type= str)

    connection = pymysql.connect(host='localhost', user='USERNAME', password='PASSWORD', database='MarloDB', cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM app_users WHERE `userName`=%s "
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            if not result:
                return 'Not registered'
            else:
                if result['passWord'] == password:
                    return 'logged in'
                else:
                    return 'Password incorrect'



#3. Product Upload API
#helper front-end
@app.route('/')  
def html_view():  
    return render_template("index.html")  



#Upload the product data
@app.route('/upload', methods = ['POST'])  
def upload():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename) 
        df = pd.read_csv(f.filename)
        insert_pd_to_sql(df)
    return "done"

#Insert product data into table 'products'
def insert_pd_to_sql(df):
    connection = pymysql.connect(host='localhost', user='USERNAME', password='PASSWORD', database='MarloDB', cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor: 
            for row in df.iloc:
                name = row.name
                barcode = row.barcode
                brand = row.brand
                description = row.description
                price = row.price
                rating = row.rating
                available = True if row.available == "TRUE" else False

                sql = "INSERT INTO products VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (name, barcode, brand, description,price,available,rating))
        connection.commit()



#4. Product Review API
@app.route('/rating', methods=['GET'])
def rating():
    name = request.args.get('name', type= str)
    rating = request.args.get('rating', type= int)

    connection = pymysql.connect(host='localhost', user='USERNAME', password='PASSWORD', database='MarloDB', cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "UPDATE products SET `rating`=%s WHERE `name` = %s "
            cursor.execute(sql, (rating, name))
        connection.commit()
    return jsonify({'rating': 'Updated'})
            


#5. Product view Pagination API
@app.route('/products', methods=['GET'])
def products():
    page_no = request.args.get('page_no', type= int)
    start = 5*(page_no-1)
    end = 5*page_no

    connection = pymysql.connect(host='localhost', user='USERNAME', password='PASSWORD', database='MarloDB', cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
            sql = "select * from (SELECT *, row_number() OVER (ORDER BY rating DESC) AS ranks FROM products) a WHERE ranks > %s AND ranks <= %s;"
            cursor.execute(sql, (start, end))
            result = cursor.fetchall()
        connection.commit()
    return jsonify(result)
