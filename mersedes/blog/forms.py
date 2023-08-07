from django import forms

class CommentsForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        min_length=5,
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Укажите ваше имя здесь'
            }
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Укажите ваш комментарий здесь'
            }
        )
    )

