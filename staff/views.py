from django.shortcuts import render, get_object_or_404, redirect
from quiz.models import Quiz, Question
from .forms import *
from django.forms import formset_factory, modelformset_factory
from django.forms.models import model_to_dict


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
    request.session['quiz_pk'] = quiz_pk
    if request.method == 'POST':
        question_form = QuestionModelForm(request.POST or None)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()

            # question = Question.objects.create(
            #     quiz=quiz,
            #     title=question_form.cleaned_data['title'],
            #     answer_type=question_form.cleaned_data['answer_type'])

            request.session['question_pk'] = question.pk
            answer_type = question_form.cleaned_data['answer_type']
            context['answer_type'] = question_form.cleaned_data['answer_type']
            context['questions'] = Question.objects.filter(quiz=quiz)

            if answer_type == 'radio':
                context['multiple_choice_form'] = MultipleChoiceForm()
                context['choice_form'] = ChoiceModelForm()
                return render(request, 'staff/choice_view.html', context)

            elif answer_type == 'text':
                context['text_form'] = TextModelForm()
                return redirect('staff:text')

    else:
        context['question_form'] = QuestionModelForm()
        context['questions'] = Question.objects.filter(quiz=quiz)

    return render(request, 'staff/detail.html', context)


def radio_view(request):
    context = {
        'questions': Question.objects.all()
    }
    ChoiceFormSet = formset_factory(ChoiceModelForm)

    if request.method == 'POST':
        filled_formset = ChoiceFormSet(request.POST)
        if filled_formset.is_valid():
            choices = []
            for form in filled_formset:
                choice = form.save(commit=False)
                choice.save()
                question = Question.objects.get(pk=request.session['question_pk'])
                Radio(question=question, answer_option=choice).save()

            note = 'Choice have been Created!'
            context['note'] = note
            return redirect('staff:detail', request.session['quiz_pk'])

        else:
            note = 'Choices were not created, try again!'

        context['note'] = note
        return render(request, 'staff/radio_view.html', context)

    else:
        no_of_choices = int(request.session['number'])
        ChoiceFormSet = formset_factory(ChoiceModelForm, extra=no_of_choices)
        formset = ChoiceFormSet()
        context['formset'] = formset
    return render(request, 'staff/radio_view.html', context)


def choice(request):
    form = MultipleChoiceForm()
    context = {
        'multiple_choice_form': form
    }
    if request.method == 'POST':
        form = MultipleChoiceForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            print('Inside Choice: ', number)
            context['number'] = number
            request.session['number'] = number
            return redirect('staff:radio')
    else:
        return render(request, 'staff/choice_view.html', context)


def text_view(request):
    quiz_pk = request.session['quiz_pk']
    context = {
        'questions': Question.objects.filter(quiz=quiz_pk)
    }

    if request.method == 'POST':
        text_form = TextModelForm(request.POST)
        if text_form.is_valid():
            text = text_form.save(commit=False)
            text.question = Question.objects.get(pk=request.session['question_pk'])
            text.save()
            return redirect('staff:detail', quiz_pk)
    else:
        context['text_form'] = TextModelForm()
        return render(request, 'staff/text_view.html', context)