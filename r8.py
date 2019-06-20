Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> def k():
	a=input("servername:")
	b=input("dbname:")
	c=input("username:")
	d=input("passward:")
	return"server={};dbname={};username={};passward={}".format(a,b,c,d)
