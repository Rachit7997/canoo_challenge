# canoo web application challenge
Home Automation
----------------
The Backend of the web application is built using django-rest framework. The django by default uses squlite for RDBMS. It also provides Templates for view in the absense of frontend.

The frontend of the web application is developed in ReactJS that provides dynamic html rendering by handling states of the frontend running on the client software (browser).  

## Installation instructions
###    Backend
#### Open a terminal window in Home Automation directory
1.  source canoo-env/bin/activate
2.  cd backend/  
3.  python3 manage.py makemigrations
4.  python3 manage.py migrate
5.  python3 manage.py initialize
6.  python3 manage.py runserver

#### In case, the virtual environment doesn't work as expected
1.  pip3 install django
1.  pip3 install djangorestframework
2.  pip3 install django-filter
1.  pip3 install django-cors-headers

###    Frontend
####   Open another teminal window in Home Automation directory
1.  cd frontend/
2.  npm install
3.  npm start

### **Auto Logging in the terminal window of Django**

### If the frontend is different than http://localhost:3000, let's say 3001
### then replace the following in canoo_challenge-main/beckend/settings.py
####    CORS_ORIGIN_WHITELIST = [
####    'http://localhost:3000'
####    ]
### with
####    CORS_ORIGIN_WHITELIST = [
####    'http://localhost:3001'
####    ]

