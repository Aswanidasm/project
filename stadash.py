#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
import cgi
f=cgi.FieldStorage()
pid=f.getvalue("id")

conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()

print("""
<!DOCTYPE html>
<head>
    <link rel='stylesheet.css'>
    <link rel="stylesheet" type="text/css" href="css/navigation.css">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="common.css">
     <link rel="stylesheet" href="nav.css">


   </head>

<body style="background-image:url('images/admi.jpg');">
   <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>
    <nav class="navbar">



<ul class="nav-links">







<div class="menu">

<li><a href="/">Home</a></li>

<li><a href="/">About</a></li>

<li><a href=staprofile.py?id=%s>Profile</a></li>

<li><a href=staform.py?id=%s>Leave</a></li>
<li class="services">
<a href="#">Approved student leave</a>
<ul class="dropdown">
<li><a href="stuleaverequ.py">New request</a></li>

<li><a href="viewstudentleave.py">Reviewed leaves</a></li>
</ul>
</li>

</div>

</ul>

</nav>

              <div class="footer">
        <h6>© 2023 All Rights Reserved By Study World Education Holding Group's.</h6>
    </div>
</body>
</html>
"""%(pid,pid))








