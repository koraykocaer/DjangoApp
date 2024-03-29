from django import forms
from .models import Article
from .models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'article_image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_author', 'comment_content']