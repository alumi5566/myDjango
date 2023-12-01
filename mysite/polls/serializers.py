from django.utils.timezone import now
from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        # fields = '__all__'
        fields = ('id', 'question_text', 'pub_date')
    def get_days_since_created(self, obj):
        return (now() - obj.pub_date).days

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        # fields = '__all__'
        fields = ('id', 'question', 'choice_text', 'votes')