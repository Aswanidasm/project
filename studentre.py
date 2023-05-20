#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()
q = """select max(id) from student"""
cur.execute(q)
r = cur.fetchone()
if r[0] != None:
    n = r[0]
else:
    n = 0
if n <= 9:
    z = "000"
elif n >= 10 and n <= 99:
    z = "00"
elif n >= 100 and n <= 999:
    z = "0"
id1 = "student" + z + str(n + 1)
print("""
<!DOCTYPE html>
<head>
<link rel="stylesheet" href="common.css">
<link rel="stylesheet" href="nav.css">
<style>
body {
  background-image: url('img_girl.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
</head>
<body style="background-image:url('images/adbga.jpg');">
   <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>
       <nav class="navbar">



<ul class="nav-links">







<div class="menu">

<li><a href="/">Home</a></li>
<li class="services">
<a href="/">Staff</a>
<ul class="dropdown">
<li><a href="/">New </a></li>
<li><a href="/">Existing</a></li>
</ul>
</li>


<li class="services">

<a href="/">Student</a>



<ul class="dropdown">

<li><a href=studentre.py>New </a></li>

<li><a href=studentview.py>Existing</a></li>



</ul>

</li>

<li><a href="/">About us</a></li>



</div>

</ul>

</nav>
   

<div class="box" >
  <div class="form" method="post" align="center" enctype="multipart/form-data">
    <h1 style=color:black>STUDENT REGISTRATION</h1><br>

        <input type="text" value="%s" name="student_id"><br><br>
        <input type="text" placeholder="Name" name="name"><br><br>
        <input type="email" placeholder="Email" name="email"><br><br>
        <input type="date" placeholder="Dob" name="dob"><br><br>
        <input type="password" placeholder="Enter password" name="pass"><br><br>
        <input type="file" name="profile">
        <input type="submit" name="sub" value="insert"> 
        </div>

  </form>

        

</body>
</html>



""" % (id1))
import cgi

f = cgi.FieldStorage()
pstudent_id = f.getvalue("student_id")
pname = f.getvalue("name")
pemail = f.getvalue("email")
pdob = f.getvalue("dob")
ppass = f.getvalue("pass")
psub = f.getvalue("sub")
if psub != None:
    pprofile = f['profile']
    if pprofile.filename:

        import smtplib

        fromaddr = 'shikhamolks5221@gmail.com'
        toaddr = pemail
        msg = """
            Hello %s, this is your student Id:%s, and password:%s
            """ % (pname, pstudent_id, ppass)
        password = 'ewfd qnkf amby etox'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()
        import os
        fn = os.path.basename(pprofile.filename)
        open("images/" + fn, "wb").write((pprofile.file.read()))
        q = """insert into student(student_id,name,email,dob,password,profile) values('%s','%s','%s','%s','%s','%s')""" % (
            pstudent_id, pname, pemail, pdob, ppass, fn)
        cur.execute(q)
        conn.commit()
        print("""
        <script>
            alert("data inserted");
        </script>""")
    else:
        print("""
                   <script>
                       alert("mail not send");
                   </script>
                    """)
    conn.close()

