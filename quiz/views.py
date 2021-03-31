from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Question, Radio, Text, Quiz
from .forms import TextForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from pprint import pprint


def index(request):
    context = {
        'quizes': Quiz.objects.all(),
    }

    return render(request, 'quiz/index.html', context)


def detail(request):
    qs = Question.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(qs, 1)
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'questions': qs,
        'user': request.user.username,
        'text_form': TextForm()
    }

    # for q in qs:
        # if content_type == 'radio':
        #     radios = Radio.objects.filter(question__id=q.id)
            # radios = q.radio_set.all
            # radios = q.radio_set.all()
        # else:
            # text = Text.objects.get(question__id=q.id)
            # pprint(vars(text))
        # print(q.content_type)

    return render(request, 'quiz/detail.html', context)
