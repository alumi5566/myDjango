# About
This is for learning purpose. The home app created an aggregate view and put the like to the rest of app in sidebar. 
Step by step following the tutorial in https://docs.djangoproject.com/zh-hans/4.2/contents/

# Instruction
This project involved OCI database connection and rest API, aside from git clone, you may need to install these tools to run the app locally
```
$pip3 install django
$pip3 install djangorestframework
$pip3 install cx_oracle
```

# Components
## Home
The home/base.html is the view for main page. Reserve a block content for showing context from other apps.

learning bullet point:
* Adding bootstrap (remote css repository): https://www.techwithtim.net/tutorials/django/adding-bootstrap
* Template: https://medium.com/sq-catch-and-note/django-30days-day8-blog%E5%AF%A6%E4%BD%9C%E7%AF%84%E4%BE%8B%E4%B8%80-template-1bc70e7b677

## Polls
This is copy and paste from the Django tutorial. Setup Question model and Choice model to store voting information. The data will be saved to the sqlite, which is a local database file. Every tool you need should come with the Django installation.

Using database API in shell (`$python manage.py shell`)

```
>>> from polls.models import Choice, Question
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> Question.objects.filter(id=1)
>>> Question.objects.get(pk=1)
```

learning bullet point:
* Creating model and associate with the sqlite database
* Adding url mapping and urlpatterns in main site
* Using template, generic view, and the static css 

## OracleDB

Setup Oracle database:
https://blogs.oracle.com/opal/post/connecting-to-oracle-cloud-autonomous-database-with-django#download_django

1 = Create auto DB in OCI

2 = Install (1) cx_Oracle (2) Oracle Instant Client (3) sqlplus

3 = Oracle Instant Client and sqlplus bin file are put under /opt/oracle/

4 = `$python manage.py migrate` and `$python manage.py makemigrations oracleDB`
* Adding database routers, so we can separate the database for different apps: https://stackoverflow.com/questions/53859629/how-to-add-database-routers-to-a-django-project

  https://reintech.io/blog/working-with-multiple-databases-in-django

  https://stackoverflow.com/questions/57676143/using-multiple-databases-with-django

  https://dboostme.medium.com/using-django-with-multiple-databases-introduction-8f0ffb409995
* If you follow the original tutorial, you will ended up store the secret and password in the GitHub and expose your credential. 
  Following https://stackoverflow.com/questions/42077532/django-security-and-settings and put the credential in the secrets.json. This file is excluded from git commit.

## AwsRDS
```
$ sudo pip3 install mysql-connector-python
$ sudo pip3 install mysql-python
$ sudo pip3 install mysqlclient
```
1 = Create RDS database in AWS

2 = Setup out bound rule to enable the external connection

3 = Assign host/port/username/password in setting (in aws_db)

4 = Update routing rule 

5 = 4 = `$python manage.py migrate database=aws_db` and `$python manage.py makemigrations awsRDS`

## Contact
Adding a form to allow user sending email. The backend connect to SMTP service held by Mailtrap

Reference: 
https://www.youtube.com/watch?v=dnhEnF7_RyM
https://docs.djangoproject.com/en/4.2/topics/email/

## reChat (real time chat)
Reference:
https://www.geeksforgeeks.org/realtime-chat-app-using-django/

## REST API
`$curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/questions/`

visit `http://127.0.0.1:8000/questions/` `http://127.0.0.1:8000/choices/`

Next: token auth for API: https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html

Reference: https://q1mi.github.io/Django-REST-framework-documentation/tutorial/quickstart_zh/


# Deploy to OCI
https://www.oracle.com/webfolder/technetwork/tutorials/obe/cloud/apaas/python/python-django-accs/python-django-accs.html#section4
https://www.youtube.com/watch?v=ZxyuWiEwFjo
```
// in requeriment.txt 
django==4.2.7
djangorestframework==3.6.2
```
```
> pip3 install -r requeriments.txt -t modules
Collecting django==4.2.7 (from -r requeriments.txt (line 1))
  Obtaining dependency information for django==4.2.7 from https://files.pythonhosted.org/packages/2d/6d/e87236e3c7b2f5911d132034177aebb605f3953910cc429df8061b13bf10/Django-4.2.7-py3-none-any.whl.metadata
  Using cached Django-4.2.7-py3-none-any.whl.metadata (4.1 kB)
Collecting djangorestframework==3.6.2 (from -r requeriments.txt (line 2))
  Downloading djangorestframework-3.6.2-py2.py3-none-any.whl (1.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 6.4 MB/s eta 0:00:00
Collecting asgiref<4,>=3.6.0 (from django==4.2.7->-r requeriments.txt (line 1))
  Obtaining dependency information for asgiref<4,>=3.6.0 from https://files.pythonhosted.org/packages/9b/80/b9051a4a07ad231558fcd8ffc89232711b4e618c15cb7a392a17384bbeef/asgiref-3.7.2-py3-none-any.whl.metadata
  Using cached asgiref-3.7.2-py3-none-any.whl.metadata (9.2 kB)
Collecting sqlparse>=0.3.1 (from django==4.2.7->-r requeriments.txt (line 1))
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Using cached Django-4.2.7-py3-none-any.whl (8.0 MB)
Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Installing collected packages: djangorestframework, sqlparse, asgiref, django
Successfully installed asgiref-3.7.2 django-4.2.7 djangorestframework-3.6.2 sqlparse-0.4.4
```
