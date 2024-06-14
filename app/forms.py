from django import forms
from .models import newRecipe

# class GridSearchForm(forms.Form):
#     search_query = forms.CharField(label='Search', max_length=100)
class newRecipeForm(forms.ModelForm):
    class Meta:
        model = newRecipe
        fields = "__all__"
    #     labels = {
    #         'firstname' : 'First Name',
    #         'lastname' : 'Last Name',
    #         'birthday':'Date of Birth',
    #         'bio':'Add a Bio to your Profile',
    #     }
    
    def __init__(self, *args, **kwargs):
        super(newRecipeForm, self).__init__(*args, **kwargs)

        self.fields['recipeimage'].widget.attrs.update({
            'style': 'display: none',
            'id':'upload'
        })

        self.fields['recipename'].widget.attrs.update({
            'placeholder':'Recipe Name'
        })

        self.fields['recipedesc'].widget.attrs.update({
            'placeholder':'Tell Us About the Recipe',
            'style' : 'height: 13.75rem'
        })

        self.fields['ingredients'].widget.attrs.update({
            'placeholder':'List of Ingredients (include quantity and measurement)'
        })

        self.fields['procedure'].widget.attrs.update({
            'placeholder':'Procedure'
        })

    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.image_path = 'media/pics/' + self.cleaned_data['recipeimage'].name
    #     if commit:
    #         instance.save()
    #     return instance

        

    



