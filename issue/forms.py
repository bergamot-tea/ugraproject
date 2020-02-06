from django import forms
from . models import Message


#class ChatForm(forms.Form):
#    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#    file1 = forms.FileField()
#    image1 = forms.ImageField()



class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('text', 'file1', 'file2', 'file3')