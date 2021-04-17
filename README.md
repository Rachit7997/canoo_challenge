# canoo web application challenge
Home Automation
----------------
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

### Auto Logging in the terminal window of Django

