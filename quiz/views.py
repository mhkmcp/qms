from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Question, Radio, Text, Quiz
from .forms import TextForm, RadioModelForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from pprint import pprint


def index(request):
    context = {
        'quizzes': Quiz.objects.all(),
    }

    return render(request, 'quiz/index.html', context)


def detail(request, quiz_pk):
    request.session['quiz_pk'] = quiz_pk
    qs = Question.objects.filter(quiz_id=quiz_pk)
    objs = Question.objects.filter(quiz_id=quiz_pk)
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 1)
    try:
        qs = paginator.page(page)
        # print('QS: ', qs)
        question = objs[qs.start_index()-1]
        print(question.id, question, question.answer_type)
        if request.method == 'POST':
            if question.answer_type == 'radio':
                radio_form = RadioModelForm(request.POST)
                print(radio_form)
                if radio_form.is_valid():
                    answer = radio_form.cleaned_data['answer_option']
                    print('Selected Ans: ', answer)
                    radio = radio_form.save()
                    print(radio)
            elif question.answer_type == 'text':
                text_form = TextForm(request.POST)
                print(text_form)
                # if text_form.is_valid():
                #     text = text_form.save()
                #     print(text)

    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'quiz_pk': quiz_pk,
        'questions': qs,
        'user': request.user.username,
        'text_form': TextForm(),
        'radio_form': RadioModelForm()
    }

    return render(request, 'quiz/detail.html', context)


def test(request, quiz_pk):
    request.session['quiz_pk'] = quiz_pk
    qs = Question.objects.filter(quiz_id=quiz_pk).order_by('id')

    if request.method == 'POST':
        question = request.GET.get('question')
        print('QUESTION TSET: ', question)

    context = {
        'quiz_pk': quiz_pk,
        'questions': qs,
        'user': request.user.username,
        'text_form': TextForm(),
        'radio_form': RadioModelForm()
    }

    return render(request, 'quiz/test.html', context)
