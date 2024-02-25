from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Quiz(models.Model):
    """Quiz test turi"""
    owner=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(default=timezone.now)
    name=models.CharField(max_length=255)



class Question(models.Model):
    """ Savollar """
    title=models.TextField()
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)

    @property
    def correct_answer(self, *args, **kwargs):
        try:
            data = Option.objects.get(question_id=self.id, is_correct=True)   
        except:
            data = False
        return data


class Option(models.Model):
    """ Variantlar """
    title=models.CharField(max_length=255)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        option = Option.objects.filter(question=self.question, is_correct=True)
        if option and self.is_correct:
            raise ValueError('Ikkita to`g`ri javob kiritish mumkin emas')
        elif not self.is_correct :
            raise ValueError('Birinchi to`g`ri javob kiriting ')
        super(Option, self).save(*args, **kwargs)


class Test_Solver(models.Model):
    """ Test topshiruvchi malumotlari """
    name=models.CharField(max_length=255)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=255)


class  Answer(models.Model):
    """ Javoblar """
    solver=models.ForeignKey(Test_Solver, on_delete=models.CASCADE)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct=models.BooleanField()



class Result(models.Model):
    """ Natija"""
    solver = models.ForeignKey(Test_Solver, on_delete=models.CASCADE)
    correct_answers = models.IntegerField()
    incorrect_answers = models.IntegerField()

    @property
    def questions(self, *args, **kwargs):
        quiz = self.taker.quiz
        result = Question.objects.filter(quiz=quiz).count()
        return result
    
    @property
    def percentage(self, *args, **kwargs):
        return self.correct_answers / self.questions * 100
    



    