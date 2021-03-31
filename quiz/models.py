from django.contrib.postgres.fields import ArrayField
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


ANS_TYPE = (
    ('radio', 'Radio'),
    ('text', 'Text')
)


class Question(models.Model):   # Module
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)

    answer_type = models.CharField(max_length=31, default='radio', choices=ANS_TYPE, blank=False, null=False)
    
    # content_type = models.ForeignKey(ContentType,
    #                                  on_delete=models.CASCADE,
    #                                  limit_choices_to={'model__in': ('text', 'radio')})
    #
    # object_id = models.PositiveIntegerField()
    # item = GenericForeignKey('content_type', 'object_id')
    #
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
    input_answer = models.TextField(null=True, blank=True)
    correct_answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question.title


class Choice(models.Model):
    choice_option = models.CharField(max_length=255, null=True, blank=True)
    is_correct = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.choice_option


class Radio(Answer):
    answer_option = models.ForeignKey(Choice,
                                      default=None,
                                      related_name='radio_options',
                                      on_delete=models.DO_NOTHING,
                                      null=True, blank=True)
    selected_answer = models.OneToOneField(Choice, default=None,
                                           related_name='radio_selected',
                                           on_delete=models.DO_NOTHING,
                                           null=True, blank=True)

    # answer_options = ArrayField(
    #     models.ForeignKey(Choice, default=None,
    #                       on_delete=models.DO_NOTHING,
    #                       null=True, blank=True),
    #     blank=True, null=True,
    #     default=list()
    # )

    def __str__(self):
        return self.question.title
