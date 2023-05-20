#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()
q = """select max(id) from staff"""
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
id1 = "staff" + z + str(n + 1)
print("""
<!DOCTYPE html>
<head>
<link rel="stylesheet" href="common.css">
  <link rel="stylesheet" href="nav.css">

     <meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
   

body {

  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}         
   






</style>
   </head>
<body style="background-image:url('images/stl.jpg');">
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
<div class="box">
  <form method="post" align="center" enctype="multipart/form-data">
    <h1 style=color:black>STAFF REGISTRATION</h1><br>

        <input type="text" value="%s" name="staff_id"><br><br>
        <input type="text" placeholder="Name" name="sname"><br><br>
        <input type="email" placeholder="Email" name="email"><br><br>
        <input type="date" placeholder="Dob" name="dob"><br><br>
        <input type="password" placeholder="Enter password" name="pass"><br><br>
        <input type="file" name="profile">
        <input type="submit" name="sub" value="insert"> 
        </div>

  </form>
</div>
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



""" % (id1))
import cgi

f = cgi.FieldStorage()
pstaff_id = f.getvalue("staff_id")
pname = f.getvalue("sname")
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
            Hello %s, this is your employee Id:%s, and password:%s
            """ % (pname, pstaff_id, ppass)
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
        q = """insert into staff(staff_id,name,email,dob,password,profile) values('%s','%s','%s','%s','%s','%s')""" % (
            pstaff_id, pname, pemail, pdob, ppass, fn)
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

