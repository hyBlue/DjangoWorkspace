from django import forms
from .models import Post
from PR1.widgets.naver_map_widget import NaverMapPointWidget

"""
class PostForm(forms.Form):
    title = forms.CharField(validators = [min_length_validator])
    content = forms.CharField(widget = forms.Textarea)
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['title','tag_set', 'content']
        widgets ={
            'user_agent' : forms.HiddenInput,
            'lnglat' : NaverMapPointWidget,
        }
    """ 
    modelForm이 아닌 그냥 Form에서는 save를 만들어줘야됨.
    def save(self, commit= True):
        post = Post(title = self.cleaned_data['title'], content = self.cleaned_data['content'])
        post.user_id = '1'
        post.save()
        post.tag_set.add(1)
        return post
    """