from django import forms
from main_gusto.models import Category, Dish


class CategoryForm(forms.ModelForm):
    title = forms.CharField(max_length=15,
                            widget=forms.TextInput(attrs={'placeholder': "Название", 'required': "required"}))
    category_order = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': "Порядок категории в меню", 'required': "required"}))
    photo = forms.ImageField(widget=forms.FileInput())
    is_visible = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Category
        fields = ('title', 'photo', 'category_order', 'is_visible')


class DishForm(forms.ModelForm):


    class Meta(object):
        model = Dish
        fields = ('title', 'photo', 'price', 'is_visible', 'desc')


