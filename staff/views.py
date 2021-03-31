from django.shortcuts import render, get_object_or_404, redirect
from quiz.models import Quiz, Question
from .forms import *
from django.forms import formset_factory


def index(request):
    context = {
        'quizes': Quiz.objects.all()
    }
    return render(request, 'staff/index.html', context)


def detail(request, quiz_pk):
    question_form = QuestionModelForm(request.POST or None)
    choice_form = ChoiceModelForm(request.POST or None)
    answer_type = None

    try:
        quiz = get_object_or_404(Quiz, pk=quiz_pk)
    except Exception as ex:
        print(ex)

    context = {'quiz': quiz, 'quiz_pk': quiz_pk}
    if request.method == 'POST':
        question_form = QuestionModelForm(request.POST or None)

        if question_form.is_valid():
            # print(question_form)
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()
            answer_type = question_form.cleaned_data['answer_type']
            if answer_type == 'radio':
                context['multiple_choice_form'] = MultipleChoiceForm()
            elif answer_type == 'text':
                context['text_form'] = TextModelForm()
            context['answer_type'] = question_form.cleaned_data['answer_type']
            context['choice_form'] = ChoiceModelForm()
            context['questions'] = Question.objects.filter(quiz=quiz)
            return render(request, 'staff/detail.html', context)

        multiple_choice_form = MultipleChoiceForm(request.POST)
        if multiple_choice_form.is_valid():
            no_of_choices = multiple_choice_form.cleaned_data['number']
            print(no_of_choices)
            ChoiceFormSet = formset_factory(ChoiceModelForm, extra=no_of_choices)
            formset = ChoiceFormSet()
            context['formset'] = formset
            # print(formset)
            if request.method == 'POST':
                filled_formset = ChoiceFormSet(request.POST)
                print("FILLED_FORMSET: ", filled_formset)

                if filled_formset.is_valid():
                    for form in filled_formset:
                        answer = form.cleaned_data['answer']
                        is_correct = form.cleaned_data['is_correct']
                        print(answer, is_correct)
            # return redirect('radio-form-view', quiz_pk=quiz_pk, no_of_choices=no_of_choices, answer_type=answer_type)
            return render(request, 'staff/detail.html', context)


    else:
        context['question_form'] = QuestionModelForm()
        context['questions'] = Question.objects.filter(quiz=quiz)

    return render(request, 'staff/detail.html', context)


def radio_view(request, quiz_pk, no_of_choices=2, answer_type='radio'):
    ChoiceFormSet = formset_factory(ChoiceModelForm, extra=no_of_choices)
    formset = ChoiceFormSet()
    if request.method == 'POST':
        filled_formset = ChoiceFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                answer = form.cleaned_data['answer']
                is_correct = form.cleaned_data['is_correct']
                print(answer, is_correct)
    context = {
        'formset': formset,
        'answer_type': answer_type,
        'quiz': get_object_or_404(Quiz, pk=quiz_pk)
    }
    return render(request, 'staff/detail.html', context)
