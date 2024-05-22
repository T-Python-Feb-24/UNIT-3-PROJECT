from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST
from .models import Survey, Question, Response, Choice, Answer

def home(request):
    return render(request, 'main/home.html')

def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'main/survey_list.html', {'surveys': surveys})

def survey_detail(request, id):
    survey = get_object_or_404(Survey, pk=id)
    questions = survey.questions.all()
    if request.method == 'POST':
        return redirect('main:survey_results', survey_id=survey.id)
    return render(request, 'main/survey_detail.html', {'survey': survey, 'questions': questions})

def learn_more(request):
    return render(request, 'main/learn_more.html')

@login_required
def create_survey(request):
    if 'survey_data' not in request.session:
        request.session['survey_data'] = {
            'title': '',
            'description': '',
            'questions': [{'text': '', 'answers': ['', '']}]
        }

    if request.method == 'POST':
        init_data = request.session['survey_data']
        init_data['title'] = request.POST.get('title', '')
        init_data['description'] = request.POST.get('description', '')

        for index, question in enumerate(init_data['questions']):
            question['text'] = request.POST.get(f'question_text_{index+1}', question['text'])
            question['answers'] = [
                request.POST.get(f'question_{index+1}_answer_{i+1}', '') for i in range(len(question['answers']))
            ]

        if 'add_question' in request.POST:
            init_data['questions'].append({'text': '', 'answers': ['', '']})

        if 'add_answer' in request.POST:
            question_index = int(request.POST['add_answer']) - 1
            if 0 <= question_index < len(init_data['questions']):
                if len(init_data['questions'][question_index]['answers']) < 5:
                    init_data['questions'][question_index]['answers'].append('')

        request.session.modified = True

        if 'submit_form' in request.POST:
            for question in init_data['questions']:
                if len(question['answers']) < 2:
                    return render(request, 'main/create_survey.html', {
                        'form_data': request.session['survey_data'],
                        'error': 'Each question must have at least 2 answers.'
                    })

            survey = Survey(title=init_data['title'], description=init_data['description'], creator=request.user)
            survey.save()
            for question_data in init_data['questions']:
                question = Question(survey=survey, text=question_data['text'])
                question.save()
                for answer_text in question_data['answers']:
                    choice = Choice(question=question, text=answer_text)
                    choice.save()
            del request.session['survey_data']
            return redirect('main:survey_list')

    return render(request, 'main/create_survey.html', {
        'form_data': request.session.get('survey_data', {})
    })

@login_required
def survey_results(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = survey.questions.all()
    results = []

    for question in questions:
        choices = question.choices.all()
        question_data = {
            'text': question.text,
            'choices': []
        }

        for choice in choices:
            count = choice.answers.count()
            question_data['choices'].append({
                'text': choice.text,
                'count': count
            })

        results.append(question_data)

    debug_info = "\n".join([f"Question: {q['text']}, Choices: {', '.join([c['text'] + ' (' + str(c['count']) + ')' for c in q['choices']])}" for q in results])
    return render(request, 'main/survey_results.html', {'survey': survey, 'results': results, 'debug_info': debug_info})

@login_required
def submit_survey(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.method == 'POST':
        response = Response(survey=survey, user=request.user)
        response.save()

        questions = survey.questions.all()
        for question in questions:
            choice_id = request.POST.get(f'question{question.id}')
            if choice_id:
                try:
                    choice = Choice.objects.get(id=choice_id)
                    Answer.objects.create(response=response, question=question, choice=choice)
                except Choice.DoesNotExist:
                    return HttpResponse(f"Choice with ID {choice_id} does not exist.", status=400)

        return redirect('main:survey_results', survey.id)
    return redirect('main:survey_detail', id=survey_id)

@login_required
@require_POST
def delete_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    if request.user == survey.creator or request.user.is_superuser:
        survey.delete()
        return redirect('main:survey_list')
    else:
        return HttpResponseForbidden("You are not allowed to delete this survey.")

@login_required
def manage_users(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to manage users.")

    users = User.objects.all()  # type: ignore 
    return render(request, 'main/manage_users.html', {'users': users})
