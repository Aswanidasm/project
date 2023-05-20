#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()
q = """select * from student"""
cur.execute(q)
a = cur.fetchall()

print("""
<head>
<link rel="stylesheet" href="nav.css" />
<link rel="stylesheet" href="common.css" />

    <style>



            *{
                margin: 0;
                padding: 0%;
                box-sizing: border-box;
            }
            .header img{
                float: left;
                height: 50px;
                width:50px;
              padding: 5px;
              margin-top: 5px;
              background-color: aliceblue;
              margin-left: 50px;
              border-radius: 50px;


            }
            table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 10px;
}
table#alter tr:nth-child(even) {
    background-color: #eee;
}
table#alter tr:nth-child(odd) {
    background-color: #fff;
}
table#alter th {
    color: white;
    background-color: gray;
}
        
          th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

tr:hover {background-color: 0081B4;}

          body  {
              background-image:url("C:/Users/SWCE/Desktop/word_a s/img.jpg");
          }
          .menu-bar{
                background-color: rgb(220, 220, 230);
                height: 50px;
                width: 100%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 5%;
                position: relative;
            }
            .menu-bar ul{
                list-style: none;
                display: flex;
                padding-top: 5px;
            }
            .menu-bar ul li{
                padding: 10px 30px;
                position: relative;

            }


            .menu-bar ul li a{
                font-size: 20px;
                color: rgb(38, 0, 255);
                text-decoration: none;
                transition: all 0.35;
            }
            .menu-bar ul li a:hover{
                color: rgb(127, 145, 247);
            }

            .dropdown-menu{
               display: none;
            }
            .menu-bar ul li:hover .dropdown-menu{
               position: absolute;
                left: 0;
                  display: block;
               top: 100%;
                background-color: rgb(255, 255, 255);
            }
               .menu-bar ul li:hover .dropdown-menu ul{
                display: block;
                margin: 10px;

            }
            .menu-bar ul li:hover .dropdown-menu ul li{
                width: 150px;
                padding: 10px;

            }
            .dropdown-menu-1{
                display: none;
            }
            .dropdown-menu ul li:hover .dropdown-menu-1{
                display: block;
                position: absolute;
                left: 150px;
                top:0;
                background-color: rgb(255, 251, 250);   }
                  table {
               margin-left: auto;
               margin-right: auto;
 
  footer{
            background:#020a26;
            box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.12);
            box-sizing: border-box;
            width: 100%;
            text-align: left;
            font: bold 16px sans-serif;
            padding: 55px 50px;
            position:absolute;
            bottom:0;
            height:auto;
            font: bold 16px sans-serif;
            padding: 55px 50px;
          }                   
.footer-distributed{

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




    
          marquee{
              font-size: large;
              scroll-behavior: smooth;

          }
          body {

  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}




        </style>
</head>

 <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>  <nav class="navbar">



<ul class="nav-links">







<div class="menu">

<li><a href=index.html>Home</a></li>

<li><a href=dashboard.py>Dashboard</a></li>


</div>

</ul>

</nav>
<br>
<br>
   

<body style="background-image:url('images/stuview.jpg');">
<div style="min-height:850px;">
    <table border="1">
    <tr>
    <th>student_id</th>
    <th>name</th>

    <th>email</th>
    <th>dob</th>

    <th>password</th>
     <th>profile</th>
     <th colspan="2">Action</th>
    </tr>""")
for i in a:
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    
     <td><img src="images/%s" height="40px" width="40px"></td>


    <td><a href="edit.py?id='%s'">Edit</a></td>
    <td><a href="delete.py?id='%s'">Delete</a></td>

    </tr>
    """ % (i[1], i[2], i[3], i[4], i[5], i[6], i[0], i[0]))
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


    </body>""")
