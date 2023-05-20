#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",database="studyworld")
cur=conn.cursor()

q="""select * from stuleave where status='PENDING'"""
cur.execute(q)
a=cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>New leave Requests of Student</title>
   <link rel="stylesheet" href="common.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
<style>
.footer-distributed{

background:#020a26;
box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.12);
box-sizing: border-box;
width: 100%;
text-align: left;
font: bold 16px sans-serif;
padding: 55px 50px;
position:relative;
bottom:0;
}

.footer-distributed .footer-left,
.footer-distributed .footer-center,
.footer-distributed .footer-right{
display: inline-block;
vertical-align: top;
}



.footer-distributed .footer-left{
width: 40%;
}



.footer-distributed h3{
color:  #ffffff;
font: normal 36px 'Open Sans', cursive;
margin: 0;
}

.footer-distributed h3 span{
color:  lightseagreen;
}



.footer-distributed .footer-links{
color:  #ffffff;
margin: 20px 0 12px;
padding: 0;
}

.footer-distributed .footer-links a{
display:inline-block;
line-height: 1.8;
  font-weight:400;
text-decoration: none;
color:  inherit;
}

.footer-distributed .footer-company-name{
color:  #222;
font-size: 14px;
font-weight: normal;
margin: 0;
}



.footer-distributed .footer-center{
width: 35%;
}

.footer-distributed .footer-center i{
background-color:  #33383b;
color: #ffffff;
font-size: 25px;
width: 38px;
height: 38px;
border-radius: 50%;
text-align: center;
line-height: 42px;
margin: 10px 15px;
vertical-align: middle;
}

.footer-distributed .footer-center i.fa-envelope{
font-size: 17px;
line-height: 38px;
}

.footer-distributed .footer-center p{
display: inline-block;
color: #ffffff;
  font-weight:400;
vertical-align: middle;
margin:0;
}

.footer-distributed .footer-center p span{
display:block;
font-weight: normal;
font-size:14px;
line-height:2;
}

.footer-distributed .footer-center p a{
color:  lightseagreen;
text-decoration: none;;
}

.footer-distributed .footer-links a:before {
  content: "|";
  font-weight:300;
  font-size: 20px;
  left: 0;
  color: #fff;
  display: inline-block;
  padding-right: 5px;
}

.footer-distributed .footer-links .link-1:before {
  content: none;
}

.footer-links a:hover{
   color:#ff8800
}



.footer-distributed .footer-right{
width: 20%;
}

.footer-distributed .footer-company-about{
line-height: 20px;
color:  #ffffff;
font-size: 14px;
font-weight: normal;
margin: 0;
}

.footer-distributed .footer-company-about span{
display: block;
color:  #ffffff;
font-size: 20px;
font-weight: bold;
margin-bottom: 20px;
}

.footer-distributed .footer-icons{
margin-top: 25px;
}

.footer-distributed .footer-icons a{
display: inline-block;
width: 35px;
height: 35px;
cursor: pointer;
background-color:  #33383b;
border-radius: 2px;

font-size: 25px;
color: #ffffff;
text-align: center;
line-height: 35px;

margin-right: 3px;
margin-bottom: 5px;
}




@media (max-width: 880px) {

.footer-distributed{
font: bold 14px sans-serif;
}

.footer-distributed .footer-left,
.footer-distributed .footer-center,
.footer-distributed .footer-right{
display: block;
width: 100%;
margin-bottom: 40px;
text-align: center;
}

.footer-distributed .footer-center i{
margin-left: 0;
}
         body {
position:relative;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
</head>

<body>
<div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>
 <div style="min-height:850px;">
  <table class=" container table table-bordered margin-toppest caption-top">
    <caption class="text-center display-5 text-primary mb-1">Student Details</caption>
    <thead>
      <tr>
        <th>Leave ID</th>
        <th>Student ID</th>
        <th>Student Name</th>
        <th>Reason</th>
        <th>From date</th>
        <th>To date</th>
        <th>TotalDays</th>
        <th>Action</th>
      </tr>
    </thead>
    """)
for i in a:
    print("""
    <tbody>
      <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
          <a href="approvestuleave.py?id=%s" class="btn btn-success">Approve</a>
          <a href="rejectstuleave.py?id=%s" class="btn btn-danger">Reject</a>
        </td>
      </tr>
      """%(i[1],i[2],i[3],i[4],i[5],i[6],i[0],i[0],i[0]))

print("""
    </table>
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
""")