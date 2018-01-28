# simple-content-post

##Problem Statement:
   * user should be able to register/sign-in
   * once sign-in, user should be able to to
      - create a post
      - like a post
      - unlike a post
      - view who all liked a post
   * likes should be unique
   * logout
   
##Technology Used:

 **Front end:** Html, Javascript, Bootstrap
 
 **Backend:** Python 2.7, Django 1.10.4, DjangoRestFramework
 
 **Database:** PostgreSQL

 * Used ajax for client server communication
 * Note:- Instead of django auth user, used separate user model and for authentication used middleware.
        - Instead of serialization used manual validation method. 
        
# django project setup and run on your local machine

##Database Setup:

Follow below step to setup the database

1. 
   * sudo apt-get install postgresql
   * sudo apt-get install libpq-dev 
2. 
 * Create user and database
 * sudo -u postgres psql
 * create user navneet;
 * alter user navneet with password 'post03nav';
 * CREATE DATABASE content_post_db OWNER navneet;
     
* Note: You can give user name and password own your choice then change the same from setting/base.py file.
      
##Install Dependency:

1. Run requirement.sh file in your choice directory
    * Give execute permission to your script
    * chmod +x /path/to/yourscript.sh
    *  And to run your scrip
    * RUN pip install -r /path/to/requirement.sh
##Run:

1. cd /path/to/simple-content-post(project dir)

2.  python manage.py makemigrations
   * python manage.py migrate
   * also migrate the all other app
3. ./manage.py collectstatic
   * rm -rf static/
   * mv os.path.join\(BASE_DIR\,\ \"static\"\)/ static
4. python manage.py runserver  
    
  

