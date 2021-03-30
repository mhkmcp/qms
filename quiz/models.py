from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Quiz(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    timeline = models.TimeField(blank=False, null=False)

    def __str__(self):
        return self.title


class Question(models.Model):   # Module
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    
    content_type = models.ForeignKey(ContentType, 
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('text', 'radio')})

    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    
    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='%(class)s_related', verbose_name='question ', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_at']

    def __str__(self):
        return self.question.title
    
    
class Text(Answer):
    offered_answer = models.TextField(null=True, blank=True)
    actual_answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question.title

    # @property
    # def type(self):
    #     return "text"


class Option(models.Model):
    answer = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.answer


class Radio(Answer):
    offered_answer = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='radios_offered')
    actual_answer = models.OneToOneField(Option, on_delete=models.CASCADE, related_name='radios_actual')

    def __str__(self):
        return self.question.title

    # @property
    # def type(self):
    #     return "radio"


