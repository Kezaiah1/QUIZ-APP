from django.shortcuts import render, redirect
from .forms import QuizForm, QuestionForm, AnswerForm

# In-memory data structures
quizzes = {}
questions = {}
answers = {}

def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz_id = len(quizzes) + 1
            quizzes[quiz_id] = {'title': form.cleaned_data['title'], 'questions': []}
            return redirect('add_questions', quiz_id=quiz_id)
    else:
        form = QuizForm()
    return render(request, 'quiz/create_quiz.html', {'form': form})

def add_questions(request, quiz_id):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_id = len(questions) + 1
            questions[question_id] = {'quiz_id': quiz_id, 'text': question_form.cleaned_data['question_text'], 'answers': []}
            quizzes[quiz_id]['questions'].append(question_id)
            return redirect('add_answers', question_id=question_id)
    else:
        question_form = QuestionForm()
    return render(request, 'quiz/add_questions.html', {'form': question_form})

def add_answers(request, question_id):
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_id = len(answers) + 1
            answers[answer_id] = {'question_id': question_id, 'text': answer_form.cleaned_data['answer_text'], 'is_correct': answer_form.cleaned_data['is_correct']}
            questions[question_id]['answers'].append(answer_id)
            return redirect('add_answers', question_id=question_id)
    else:
        answer_form = AnswerForm()
    return render(request, 'quiz/add_answers.html', {'form': answer_form})

def take_quiz(request, quiz_id):
    quiz = quizzes[quiz_id]
    quiz_questions = [questions[q_id] for q_id in quiz['questions']]
    if request.method == 'POST':
        score = 0
        for question in quiz_questions:
            selected_answer = request.POST.get(str(question['id']))
            if selected_answer:
                answer = answers[int(selected_answer)]
                if answer['is_correct']:
                    score += 1
        return render(request, 'quiz/results.html', {'quiz': quiz, 'score': score, 'total': len(quiz_questions)})
    return render(request, 'quiz/take_quiz.html', {'quiz': quiz, 'questions': quiz_questions})
