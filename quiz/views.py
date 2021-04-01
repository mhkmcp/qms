from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *
from .forms import *

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

    if request.method == 'POST':
        page = request.session['page']
    else:
        page = request.GET.get('page', 1)
        request.session['page'] = page
    paginator = Paginator(qs, 1)

    try:
        qs = paginator.page(page)
        question = objs[qs.end_index()-1]
        print(question.id, question.answer_type, question.title)

        # for radio in Radio.objects.filter(question_id=question.id):
        #     print(radio.answer_option, radio.answer_option.is_correct)

        if request.method == 'POST':
            if question.answer_type == 'radio':
                data = list(request.POST.items())[1]
                selected_choice = list(data)[1]
                print(selected_choice)
                Choice.objects.filter(question_id=question.id).update(is_selected=False)
                dcts = {
                    'question': question.id,
                    'is_selected': True
                }
                Choice.objects.filter(id=selected_choice).update(**dcts)
                # 'Female': ['57'],
                # if choice_form.is_valid():
                #     form = choice_form.save(commit=False)
                #     print('Form: ', choice_form)
                    # answer = form.cleaned_data['text']
                    # print('Selected Ans: ', answer)

            else:
                text_form = TextForm(request.POST)
                if text_form.is_valid():
                    print(question.id, question.answer_type, question.title)
                    Text.objects.filter(question_id=question.id).update(input_answer=text_form.cleaned_data['input_answer'])

    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'quiz_pk': quiz_pk,
        'questions': qs,
        'user': request.user.username,
        'text_form': TextForm(),
        'choice_form': ChoiceForm(),
        'choices': Choice.objects.filter(question_id=question.id) or None
    }

    return render(request, 'quiz/detail.html', context)


def submit(request):
    if request.method == 'POST':
        pass


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
        # 'radio_form': RadioModelForm()
    }

    return render(request, 'quiz/test.html', context)
