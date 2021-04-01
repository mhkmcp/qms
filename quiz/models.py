from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Quiz(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    # timeline = models.PositiveIntegerField(default=0, blank=False, null=False)
    time = models.PositiveIntegerField(default=0, blank=False, null=False)
    is_available = models.BooleanField(default=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'
        ordering = ('created_at',)

    def __str__(self):
        return self.title


ANS_TYPE = (
    ('radio', 'Radio'),
    ('text', 'Text')
)


class Question(models.Model):   # Module
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)

    answer_type = models.CharField(max_length=31, default='radio', choices=ANS_TYPE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ('id',)

    def __str__(self):
        return self.title

    
class Text(models.Model):
    question = models.ForeignKey(Question, related_name='texts', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, blank=True, null=True)
    input_answer = models.TextField(null=True, blank=True)
    correct_answer = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
        ordering = ('created_at',)

    def __str__(self):
        return self.question.title


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, blank=True, null=True)
    text = models.CharField(max_length=255, null=True, blank=True)
    is_correct = models.BooleanField(default=False, null=True, blank=True)
    is_selected = models.BooleanField(default=False, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


# class Answer(models.Model):
#     question = models.ForeignKey(Question, related_name='%(class)s_related', verbose_name='question ', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
#         ordering = ['created_at']
#
#     def __str__(self):
#         return self.question.title


# class Radio(Answer):
#     answer_option = models.ForeignKey(Choice,
#                                       default=None,
#                                       related_name='radio_options',
#                                       on_delete=models.DO_NOTHING,
#                                       null=True, blank=True)
    # selected_answer = models.OneToOneField(Choice, default=None,
    #                                        related_name='radio_selected',
    #                                        on_delete=models.DO_NOTHING,
    #                                        null=True, blank=True)

    # answer_options = ArrayField(
    #     models.ForeignKey(Choice, default=None,
    #                       on_delete=models.DO_NOTHING,
    #                       null=True, blank=True),
    #     blank=True, null=True,
    #     default=list()
    # )

    # def __str__(self):
    #     return self.question.title
