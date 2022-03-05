from curses import flash
from email import message
import redirect,url_for,session,request
import re
import form #waiting on frontend 
from sqlite3 import Cursor
from unicodedata import category
from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="12345678"
app.config["MYSQL_DB"]="hni_wm_app"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql=MySQL(app)
 @app.route('/bookapp',methods=["GET","POST"])
 def bookapp():
    if not session["isHNI"]:
         flash("You are only allowed to rescehdule an appointment")
         return redirect(url_for(""))   #need to be filled after making the frontend
    if request.method=="GET":
        form=BookApp(request.form)
        cursor=mysql.connection.cursor();
        query= "SELECT * FROM hni where "  #need to be filled after making the database
        cursor.execute(query,(session[]))  #need to be filled after making the database
        wm=cursor.fetchone()
        req_id=wm["req_id"]

        month=datetime.today().month
        day=datetime.today().day
        year=datetime.today().year
        
        
        query= #too test appointment database

        cursor.execute(query,(req_id,day,month,year))
        upcome_app=cursor.fetchall()

        if upcome_app:
            flash(message="There is an appointment scheduled for you in the following days")
            cursor.close()
            return redirect(url_for("")) #need to be filled after making the frontend
        
        else:
            form=BookApp(request.form)
            if request.method=="POST";
            cursor= mysql.connection.cursor()
            wm_id=form.wm.dat
            date=form.date.data
            hour=form.hour.data
            today=datetime.today()
            if today.year==date.year and today.month==date.month and today.day=date.day and datetime.now().hour >int(hour):
                flash(message="The time to have schedule the appointment has passed")
                return redirect(url_for("book_an_appointment"))
            query= #need to be filled after making the database
            cursor.execute(query,(wm_id))
            wm=cursor.fetchone()
            wm_name=wm['name']
            query=" SELCT * appointments WHERE d_id= %s and `year` = %s and `month` = %s and `day` = %s and `hour` = %s"
            result=cursor.execute(query,(wm_id,date.year,date.month,date.day,hour))
            if result:
                flash(message=wm_name+" has already scheduled an appointment on "+str(date.day)+"/"+str(date.month)+"/"str(date.year)+"at"+hour)
                return redirect(url_for(""))  #need to be filled after making the frontend
            query = query = "SELECT * FROM  wm WHERE  wm_id= %s"
            cursor.execute(query, (wm_id,))
            wm = cursor.fetchone()
            query="SELECT * FROM hni WHERE hni_id=%s"
            cursor.execute(query,(session["id"],))
            hni=cursor.fetchone()
            hni_id=hni["hni_id"]
            query="INSERT INTO appointments(wm_id,hni_id,`hour`, `month`, `day`, `year`) VALUES(%s, %s, %s, %s, %s, %s)"
            cursor.execute(query,(wm_id,hni_id,hour,date.month,date.day,date.year))
            mysql.connection.commit()
            cursor.close()
            flash(message=" Your appointment has been booked",category="success")
            return redirect(url_for())  #need to be filled after making the frontend
        else:
            flash(message="Criteria not passed",category="danger")
            return redirect(url_for())  #need to be filled after making the frontend
    

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(url_for()) #need to be filled after making the frontend


    if __name__== '__main__':
        app.run()




            


    
    

