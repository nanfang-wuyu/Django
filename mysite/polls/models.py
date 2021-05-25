import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class User(models.Model):
    user_id = models.IntegerField()

    def __str__(self):
        return self.user_id


class Test(models.Model):
    userId = models.CharField(max_length=200)
    testType = models.IntegerField()
    degreeA = models.FloatField()
    degreeB = models.FloatField()
    degreeC = models.FloatField()


class Filters(models.Model):
    userId = models.CharField(max_length=200, default="-1")  # -1 means default values
    filterType = models.IntegerField(default=0)  # 0, 1, 2, 3
    r1 = models.FloatField()
    r2 = models.FloatField()
    r3 = models.FloatField()
    g1 = models.FloatField()
    g2 = models.FloatField()
    g3 = models.FloatField()
    b1 = models.FloatField()
    b2 = models.FloatField()
    b3 = models.FloatField()


class Images(models.Model):
    image_type = models.IntegerField(default=0)
    image_path = models.CharField(max_length=200)
