from django import forms

class QuizForm (forms.Form):
    title = forms.CharField (max_length=100)

class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=255)

class AnswerForm(forms.Form):
    answer_text = forms.CharField(max_length=255)
    is_correct = forms.BooleanField(required=False)
