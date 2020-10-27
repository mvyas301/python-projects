import pymysql
#import frontend

def studentData():
        con = pymysql.connect(host="localhost",user="root",passwd="",database="student")
        cur=con.cursor()
       
        cur.execute("CREATE TABLE IF NOT EXISTS students(id integer primary key AUTO_INCREMENT,StdID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text)")
        con.commit()
        con.close()              
def addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con=con = pymysql.connect(host="localhost",user="root",passwd="")
        cur=con.cursor()
        cur.execute("use student")
        cur.execute("INSERT INTO students VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close() 
def viewData():
        con=con = pymysql.connect(host="localhost",user="root",passwd="")
        cur=con.cursor()
        cur.execute("use student")
        cur.execute("select * from students")
        row=cur.fetchall()
        con.close()       
        return row
def deleteRec(id):
        con=con = pymysql.connect(host="localhost",user="root",passwd="")
        cur=con.cursor()
        cur.execute("use student")
        cur.execute("DELETE FROM students WHERE id=%s",(id,))
        con.commit()
        con.close()         
def searchData(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con=con = pymysql.connect(host="localhost",user="root",passwd="")
        cur=con.cursor()
        cur.execute("use student")
        cur.execute("SELECT * FROM students WHERE StdID=%s or Firstname=%s or Surname=%s or DoB=%s or Age=%s or Gender=%s or Address=%s or Mobile=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        rows=cur.fetchall()
        con.close()        
        return rows
def dataUpdate(id,StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
        con = pymysql.connect(host="localhost",user="root",passwd="")
        cur=con.cursor()
        cur.execute("use student")
        cur.execute("UPDATE students SET StdID=%s,Firstname=%s,Surname=%s,DoB=%s,Age=%s,Gender=%s,Address=%s,Mobile=%s WHERE id=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close()    
