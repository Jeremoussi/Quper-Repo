from django import forms
from . import models

class EntityForm(forms.ModelForm):
    activity = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=models.Activity.objects.all())
    class Meta:
        model = models.Entity
        fields = ('entityName',
                'activity',
                'email',
                'address',
                'city',
                'postcode',
                'country',
                'description')

    def __init__(self, *args, **kwargs):
        super(EntityForm,  self).__init__(*args, **kwargs)
        self.fields['entityName'].label = "Naam Zaak"
        self.fields['activity'].label = "Activiteiten"
        self.fields['address'].label = "Adres"
        self.fields['city'].label = "Stad"
        self.fields['postcode'].label = "Postcode"
        self.fields['country'].label = "Land"
        self.fields['description'].label = "Omschrijving"

class ActivityForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ('activity',
                'activityGroup',
                'description')

        widgets = {
            'activity': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
    def __init__(self, *args, **kwargs):
        super(ActivityForm,  self).__init__(*args, **kwargs)
        self.fields['activity'].label = "Activiteiten"
        self.fields['activityGroup'].label = "Activiteiten Groep"
        self.fields['description'].label = "Omschrijving"

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
