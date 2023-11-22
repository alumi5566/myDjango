# About
This is for learning purpose. The home app created an aggregate view and put the like to the rest of app in sidebar. 
Step by step following the tutorial in https://docs.djangoproject.com/zh-hans/4.2/contents/

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