from flask import *
import pymysql

app = Flask(__name__)

# We start by creating a secret key
app.secret_key = 'abggfrgjtj5o9s5g'

@app.route('/')
def home():
    # establish db connection
    conn = pymysql.connect(host='localhost', user='root', password='', database='swala_soko_garden')

    

    # smartphones
    cursor = conn.cursor()
    sql1 = "SELECT * FROM products WHERE product_category = 'Smartphone'"
    cursor.execute(sql1)
    rows = cursor.fetchall()

    # electronics
    cursor1 = conn.cursor()
    sql2 = "SELECT * FROM products WHERE product_category = 'Electronics'"
    cursor1.execute(sql2)
    rows2 = cursor1.fetchall()

    # Utensils
    cursor2 = conn.cursor()
    sql3 = "SELECT * FROM products WHERE product_category = 'Utensils'"
    cursor2.execute(sql3)
    rows3 = cursor2.fetchall()

    # Others
    cursor3 = conn.cursor()
    sql4 = "SELECT * FROM products WHERE product_category = 'Others'"
    cursor3.execute(sql4)
    rows4 = cursor3.fetchall()

    # Clothes
    cursor4 = conn.cursor()
    sql5 = "SELECT * FROM products WHERE product_category = 'Clothes'"
    cursor4.execute(sql5)
    rows5 = cursor4.fetchall()


    return render_template('home.html', Smartphone=rows, Electronics=rows2, Utensils=rows3, Others=rows4, Clothes=rows5)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method=='POST':
        product_name=request.form['product_name']
        product_desc=request.form['product_desc']\
    
        product_cost=request.form['product_cost']
        product_category=request.form['product_category']
        product_image_name=request.files['product_image_name']

        # save image on -> static/images/
        product_image_name.save('static/images/' + product_image_name.filename)

        # connect to the database:
        import pymysql
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password="",
                                     database='swala_soko_garden')
        
        data =(product_name,product_desc,product_cost,product_category,product_image_name.filename)

        #cursor: Function that allow sql query to be executed in python

        cursor = connection.cursor()
        sq1 = "insert into products (product_name,product_desc,product_cost,product_category,product_image_name) values(%s, %s, %s, %s, %s)"

        cursor.execute(sq1, data)
        #save changes on database
        connection.commit()
        return render_template('upload.html', success = 'Successful')


    else:
        return render_template('upload.html', message= 'Please fill in form')    
    
@app.route('/single/<id>')
def single(id):
    dbconn = pymysql.connect(host='localhost', user='root', password='',database='swala_soko_garden')

    itemCursor = dbconn.cursor()
    query = "SELECT * FROM products WHERE product_id =%s"
    itemCursor.execute(query,id)
    itemRow = itemCursor.fetchone()
    print(itemRow)
    return render_template('single_item.html',product=itemRow)

@app.route('/register', methods=['POST', 'GET'])
def register():
        
        import sms

        if request.method == 'GET':
             return render_template('register.html')
        else:
             username= request.form['username']
             email = request.form['email']
             phone = request.form['phone']
             password1 = request.form['password']
             password2 = request.form['confirm_password']

             if len(password1) < 8:
                return render_template('register.html', error = 'Password too short - minimum 8 characters')
             elif password1 != password2:
                  return render_template('register.html', error = 'Passwords do not match')
             else:
                  dbconn = pymysql.connect(host='localhost',
                                     user='root',
                                     password="",
                                     database='swala_soko_garden')
                  
                  cursor = dbconn.cursor()

                  sql = "INSERT INTO users (username, password, email, phone) VALUES (%s, %s, %s, %s)"

                  cursor.execute(sql, (username,password1,email,phone))

                  dbconn.commit()

                  sms.send_sms(phone, "Welcome Aboard")

                  return render_template('register.html', message = "Account Created")
             

#  Below is the login route
@app.route('/signin', methods=['POST', 'GET']) 
def signing():
    # We first check if the method is post
    if request.method == 'POST':
        #collect data from the form and assign each to a variable
        username= request.form['username']
        password = request.form['password']
        # Create a connection
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password="",
                                     database='swala_soko_garden')
        # Create a cursor object
        cursor = connection.cursor()

        # We prepare our sql statements
        sql = 'SELECT * FROM users WHERE username = %s AND password = %s'

        #we are now ready to execute. The execute function has 2 parameters:-
        # 1. the sql statement
        # 2. a tuple containing the values
        cursor.execute(sql,(username,password))

        if cursor.rowcount == 0:
            msg = 'The username password combination is wrong'
            return render_template('signin.html', error = msg)
        else:
            #here we make a session variable. This variable will be available in all pages
            session['username'] = username
            return redirect('/') #the login was successful so we redirect to the home page

    else:
        return render_template('signin.html')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/mpesa',methods=['POST','GET'])
def mpesa():
    if request.method=='POST':
        phone = request.form['mpesa_number']
        price= request.form['price']

        import mpesa
        mpesa.stk_push(phone,price)

        return "<h1>please enter your phone and enter mpesa pin</h1><a>ContinueShopping</a>"
    else:
        return redirect('/')   

@app.route('/mpesa2',methods=['POST','GET'])
def mpesa2():
    if request.method=='POST':
        phone=request.form['mpesa_number']
        product_id=request.form['product_id']

        conn = pymysql.connect(host='localhost',
                                     user='root',
                                     password="",
                                     database='swala_soko_garden')
        cursor = connection.cursor()   
        sql= "SELECT product_cost FROM products WHERE product_id=%s"
        cursor.execute(sql,(product_id))
        price =cur.fetchone()

        import mpesa
        mpesa.stk_push(phone,price[0])

    else:
        return redirect('/')   

@app.route('/vendors' , methods=['POST', 'GET'] )
def vendors():
    if request.method=='POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        county=request.form['county']
        password = request.form['password']
        password2 = request.form['confirm_password']
        email=request.form['email']

        if len(password) < 8:
                return render_template('vendors.html', error = 'Password too short - minimum 8 characters')
        elif password != password2:
                  return render_template('vendors.html', error = 'Passwords do not match')
        else:

        
        # connect to the database:
       
            connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password="",
                                     database='swala_soko_garden')
        
        data =(firstname,lastname,county,password,email)

        #cursor: Function that allow sql query to be executed in python

        cursor = connection.cursor()
        sq1 = "insert into vendors (firstname,lastname,county,password,email) values(%s, %s, %s, %s, %s)"

        cursor.execute(sq1, data)
        #save changes on database
        connection.commit()
        return render_template('vendors.html', success = 'Successful')


    else:
        return render_template('vendors.html', message= 'CREATE VENDOR ACCOUNT')  

@app.route('/vendor_profile')
def vendor_profile():
    dbconn = pymysql.connect(host='localhost', user='root', password='',database='swala_soko_garden')

    itemCursor = dbconn.cursor()
    query = "SELECT * FROM vendors WHERE email =%s"
    itemCursor.execute(query,id)
    itemRow = itemCursor.fetchone()
    print(itemRow)
    return render_template('vendor_profile.html',product=itemRow)          
       
if (__name__) == ('__main__'):
    app.run(debug= True)