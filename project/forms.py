from django import forms
from . models import Chat


#class ChatForm(forms.Form):
#    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#    file1 = forms.FileField()
#    image1 = forms.ImageField()



class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ('text', 'file1')