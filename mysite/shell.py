# reference: https://stackoverflow.com/questions/16853649/how-to-execute-a-python-script-from-the-django-shell
#This is replacement for $python3 manage.py shell
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from polls.models import Choice, Question
print("from polls, set of questions: ")
print(Question.objects.all())
q = Question.objects.filter(pk=1)
q = Question.objects.filter(question_text__startswith="What")
q = Question.objects.get(id=2)
print("question = %s" % q)
print("q.pk = %s" % q.pk)
print("q.was_published_recently = %s" % q.was_published_recently())
# q.save()

from awsRDS.models import Choice, Question
print("from aws, set of questions: ")
print(Question.objects.all())
q = Question.objects.filter(pk=1)
q = Question.objects.filter(question_text__startswith="What")
q = Question.objects.get(id=1)
print("question = %s" % q)
print("q.pk = %s" % q.pk)
print("q.was_published_recently = %s" % q.was_published_recently())