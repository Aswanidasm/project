#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8" />

<meta http-equiv="X-UA-Compatible" content="IE=edge" />

<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="stylesheet" href="common.css" />
<link rel="stylesheet" href="nav.css" />



<title>Document</title>

</head>

<body>
 <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>

<nav class="navbar">



<ul class="nav-links">







<div class="menu">

<li><a href="/">Home</a></li>

<li><a href="/">About</a></li>

<li class="services">

<a href="/">Services</a>



<ul class="dropdown">

<li><a href="/">Dropdown 1 </a></li>

<li><a href="/">Dropdown 2</a></li>

<li><a href="/">Dropdown 2</a></li>

<li><a href="/">Dropdown 3</a></li>

<li><a href="/">Dropdown 4</a></li>

</ul>

</li>

<li><a href="/">Pricing</a></li>

<li><a href="/">Contact</a></li>

</div>

</ul>

</nav>
 <div class="footer">
        <h6>© 2023 All Rights Reserved By Study World Education Holding Group's.</h6>
    </div>
</body>

</html>
""")
