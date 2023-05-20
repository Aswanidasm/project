#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
import cgi
from datetime import datetime
f= cgi.FieldStorage()
pid = f.getvalue("id")
conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()
q1 = """select student_id from student where id= %s """%(pid)
cur.execute(q1)
r = cur.fetchone()
q = """select max(id) from stuleave"""
cur.execute(q)
max = cur.fetchone()
if max[0] != None:
    n = max[0]
else:
    n = 0
if n <= 9:
    z = "000"
elif n >= 10 and n <= 99:
    z = "00"
elif n >= 100 and n <= 999:
    z = "0"
id1 = "LID" + z + str(n + 1)


print("""
 <!DOCTYPE html>
<html>
<head>
   <link rel="stylesheet" href="common.css">
       <link rel="stylesheet" href="nav.css">
        <link rel="stylesheet" href="stulform.css">
<style>
form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color:rgba(255,255,255,0.5);
    border-radius: 10px;
  }

  h2 {
    text-align: center;
    margin-bottom: 20px;
  }

  .form-group {
    margin-bottom: 15px;
  }

  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  input[type="text"],
  input[type="email"],
  input[type="tel"],
  input[type="password"],
  select {
    width: 100px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }

  input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    float: right;
  }

  input[type="submit"]:hover {
    background-color: #45a049;
  }

</style>
</head>
<body style="background-color:aliceblue">
  <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>
      <nav class="navbar">
<ul class="nav-links">
<div class="menu">

<li><a href=index.html>Home</a></li>



<li><a href=dashboard.py>Dashboard</a></li>



</div>

</ul>

</nav>
 <div style="min-height:850px;">
<form method="post">
    <h2>Student Leave Form</h2>
    
    <div class="form-group">
      <label>Leave id</label>
      <input type="text" id="Leave_id" name="leave_id" value="%s" required>
    </div>
    <div class="form-group">
      <label>Student_id</label>
      <input type="text" id="Student_id" name="student_id" value="%s" placeholder="Enter Student Name" required>
    </div>
    <div class="form-group">
      <label>name</label>
      <input type=text name="name">
      </div>

    <div class="form-group">
      <label>Reason</label>
      <textarea name="reason"></textarea>

    </div>
    <div class="form-group">
      <label>From date</label>
      <input type="date" id="fromdate" name="from_date" placeholder="Enter From date" required>
    </div>
    <div class="form-group">
      <label>To date</label>
      <input type="date" id="todate" name="to_date" placeholder="Enter To date" required>
    </div>

    <div class="form-group">
      <input type="submit" value="Register" name="sub">
    </div> 
     </form></div>
       <footer class="footer-distributed">

      <div class="footer-left">

         <img src="images/logo-swce-white.png"width="200" height="150">

         <p class="footer-links">
            <a href="#" class="link-1">Home</a>

            <a href="#">Blog</a>

            <a href="#">Pricing</a>

            <a href="#">About</a>

            <a href="#">Faq</a>

            <a href="#">Contact</a>
         </p>

         <p class="footer-company-name">© 2023 All Rights Reserved By Study World Education Holding Group's.</p>
      </div>

      <div class="footer-center">

         <div>
            <i class="fa fa-map-marker"></i>
            <p><span>1/2A-1</span>Alagu Nachiamman Kovil Road,Palathurai,Madukkarai,Coimbatore - 641105.</p>
         </div>

         <div>
            <i class="fa fa-phone"></i>
            <p>+91 9944911933</p>
         </div>

         <div>
            <i class="fa fa-envelope"></i>
            <p><a href="mailto: coimbatore@swehg.com"> coimbatore@swehg.com</a></p>
         </div>

      </div>

      <div class="footer-right">

         <p class="footer-company-about">
            <span>About</span>
                 <i>Study World College of Engineering, started in 2009, is one of the renowned private institutions of Coimbatore, India.The college offers a range of courses approved by AICTE and affiliated to Anna University. Study World College of Engineering is a part of Study World Education Holding Group.</i></p>

           <div class="footer-icons">

            <a href="#"><i class="fa fa-facebook-square"></i></a>
            <a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a>
            <a href="#"><i class="fa fa-instagram" aria-hidden="true"></i></a>


         </div>


      </div>

   </footer>

</body>
</html>

""" % (id1,r[0]))


pleave_id = f.getvalue("leave_id")
pstudent_id = f.getvalue("student_id")
pstudent_name = f.getvalue("name")
preason=f.getvalue("reason")
pfrom_date = f.getvalue("from_date")
pto_date = f.getvalue("to_date")
psub = f.getvalue("sub")
d1 = datetime.strptime(pfrom_date,"%Y-%m-%d")
d2 = datetime.strptime(pto_date,"%Y-%m-%d")
total_days=d2-d1
total=total_days.days
if psub != None:
        q2 = """insert into stuleave(leave_id,student_id,name,reason,from_date,to_date,total_days,status)values('%s','%s','%s','%s','%s','%s','%s','PENDING')""" % (
           pleave_id,pstudent_id, pstudent_name,preason, pfrom_date, pto_date, total)
        cur.execute(q2)
        conn.commit()
        print("""
        <script>
        alert("data inserted successfully");
        </script>

        """)
        conn.close()
