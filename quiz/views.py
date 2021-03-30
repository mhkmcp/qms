from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Question, Radio, Text, Quiz

from pprint import pprint


def index(request):
    context = {
        'quizes': Quiz.objects.all(),
    }

    return render(request, 'quiz/index.html', context)


def detail(request):
    qs = Question.objects.all()
    context = {
        'questions': qs,
    }

    print('\n Question')

    for q in qs:
        content_type = str(q.content_type).split(' | ')[-1]
        # pprint(vars(q))
        if content_type == 'radio':
            radios = Radio.objects.filter(question__id=q.id)
            # radios = q.radio_set.all
            # radios = q.radio_set.all()
            print(radios)
            # pprint(vars(radio[0]))
            # print(radio[0].actual_answer)
            # print(q.text_actual_answer)
            pass
        else:
            # text = Text.objects.get(question__id=q.id)
            # pprint(vars(text))
            pass
        # print(q.content_type)

    return render(request, 'quiz/detail.html', context)
