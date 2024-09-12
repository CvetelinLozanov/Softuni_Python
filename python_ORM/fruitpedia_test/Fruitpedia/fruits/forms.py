from django import forms
from .models import Category, Fruit


# Base form can be used for searched bar.
# class Category(forms.Form):
#     name = forms.CharField(
#         required=True,
#         max_length=30,
#     )


class CategoryBaseModel(forms.ModelForm):
    #name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Category Name'}))

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category Name'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class CategoryAddForm(CategoryBaseModel):
    pass


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'description': forms.TextInput(attrs={'placeholder': 'Enter the decription'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Enter the image_url'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Enter the nutrition'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''


class AddFruitForm(BaseFruitForm):
    pass


class EditFruitForm(BaseFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
