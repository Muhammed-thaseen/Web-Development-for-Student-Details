from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
#MYSQL CONNECTION
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="MDthaseen2004"
app.config["MYSQL_DB"]="zah"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)


#Loading Home Page
@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT * FROM users"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html",datas=res)
    
#New User
@app.route("/addUsers",methods=['GET','POST'])
def addUsers():
    if request.method=='POST':
        name=request.form['name']
        section=request.form['section']
        department=request.form['department']
        con=mysql.connection.cursor()
        sql="insert into users(NAME,SECTION,DEPARTMENT) value (%s,%s,%s)"
        con.execute(sql,[name,section,department])
        mysql.connection.commit()
        con.close()
        flash('User Details Added')        
        return redirect(url_for("home"))
    return render_template("addUsers.html")
#update User
@app.route("/editUser/<string:id>",methods=['GET','POST'])

def editUser(id):
    con=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        section=request.form['section']
        department=request.form['department']
        sql="update users set NAME=%s,SECTION=%s,DEPARTMENT=%s where ID=%s"
        con.execute(sql,[name,section,department,id])
        mysql.connection.commit()
        con.close()
        flash('User Detail Updated')
        return redirect(url_for("home"))
        con=mysql.connection.cursor()
        
    sql="select * from users where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("editUser.html",datas=res)
#Delete User
@app.route("/deleteUser/<string:id>",methods=['GET','POST'])
def deleteUser(id):
    con=mysql.connection.cursor()
    sql="delete from users where ID=%s"
    con.execute(sql,id)
    mysql.connection.commit()
    con.close()
    flash('User Details Deleted')
    return redirect(url_for("home"))

if(__name__=='__main__'):
    app.secret_key="abc123"
    app.run(debug=True)






