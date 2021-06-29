from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 2, 'placeholder': 'Поле для комментария',
                "class": "form-control"}),
        max_length=500, label='Новый комментарий')
        
    class Meta:
        model = Comments
        fields = ('message',)