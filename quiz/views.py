from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import *
from .forms import *
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pprint import pprint
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):
    quizzes = Quiz.objects.all().exclude(id__in=QuizList.objects.filter(user_id=request.user.id, is_available=False))
    context = {
        'quizzes': quizzes,
    }

    return render(request, 'quiz/index.html', context)


# def get_remaining_time(remaining, lost=0):


@login_required(login_url='/accounts/login/')
def detail(request, quiz_pk):


    request.session['quiz_pk'] = quiz_pk
    qs = Question.objects.filter(quiz_id=quiz_pk)
    quiz = Quiz.objects.get(id=quiz_pk)
    # print("QUIZ TIME: ", quiz.time)
    obj = Question.objects.filter(quiz_id=quiz_pk)

    if request.method == 'POST':
        page = request.session['page']
    else:
        page = request.GET.get('page', 1)
        request.session['page'] = page
    paginator = Paginator(qs, 1)

    try:
        qs = paginator.page(page)
        question = obj[qs.end_index()-1]
        print(question.id, question.answer_type, question.title)

        if request.method == 'POST':
            if question.answer_type == 'radio':
                # existing_choice = Choice.objects.filter(question_id=question.id,
                #                                         user_id=request.user.id, is_selected=True)
                # choice_form = ChoiceModelForm(request.POST,
                #                               data=existing_choice[0])
                data = list(request.POST.items())[1]
                print(data)
                text_choice = list(data)[0]
                selected_choice = list(data)[1]
                print(text_choice, selected_choice)
                # pass

                existing_choice = Choice.objects.filter(question_id=question.id,
                                                        user_id=request.user.id, is_selected=True)

                ''' create '''

                if len(existing_choice) == 0:
                    Choice.objects.create(question_id=question.id,
                                          user_id=request.user.id,
                                          is_selected=True,
                                          )
                # update
                else:
                    # toggle False to already selected once
                    Choice.objects.filter(user_id=request.user.id,
                                          question_id=question.id,
                                          is_selected=True).update(is_selected=False)
                    # update newly input one
                    Choice.objects.filter(id=selected_choice,
                                          user_id=request.user.id,
                                          question_id=question.id).update(is_selected=True)
                # 'Female': ['57'],

            else:
                text_form = TextForm(request.POST)
                if text_form.is_valid():
                    existing_text = Text.objects.filter(question_id=question.id, user=request.user)
                    if len(existing_text) == 0:
                        Text.objects.create(question_id=question.id,
                                            user_id=request.user.id,
                                            input_answer=text_form.cleaned_data['input_answer'])
                    else:
                        Text.objects.filter(question_id=question.id, user_id=request.user.id).update(
                                            input_answer=text_form.cleaned_data['input_answer'])

    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'quiz_pk': quiz_pk,
        'quiz': quiz,
        'questions': qs,
        'user': request.user.username,
        # 'remaining_time': x
    }

    if question.answer_type == 'radio':
        try:
            choices = Choice.objects.filter(question_id=question.id).exclude(text=None)
            choice_text = Choice.objects.filter(question_id=question.id, user_id=request.user.id)[0].id

            context['choice_text'] = choice_text or None
        except Exception as ex:
            print(ex)

        context['choices'] = choices or None
        context['choice_form'] = ChoiceForm()

    else:
        input_answer = None
        try:
            existing_text = Text.objects.filter(question_id=question.id, user_id=request.user.id)
            if len(existing_text):
                input_answer = existing_text[0].input_answer
            context['text'] = existing_text or None
        except Exception as ex:
            print(ex)

        context['text_form'] = TextForm(initial={'input_answer': input_answer} or None)

    # QuizList.objects.filter(user_id=request.user.id).update(is_available=True)

    return render(request, 'quiz/detail.html', context)


@login_required(login_url='/accounts/login/')
def finish_exam(request):
    QuizList.objects.create(user_id=request.user.id, quiz_id=request.session['quiz_pk'], is_available=False)
    return redirect('quiz:home')
