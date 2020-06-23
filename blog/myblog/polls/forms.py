from django import forms

from django import forms

from .models import post


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'post_data', 'date_posted', 'author', 'post_img')


# from myblog.polls.models import post


class UploadForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'post_data', 'post_img')


from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
