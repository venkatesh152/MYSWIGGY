from django import  forms
from resturant.models import ResturantModel

class ResturantForm(forms.ModelForm):
    rest_password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    class Meta:
        model = ResturantModel
        fields = "__all__"
        exclude = ("rest_id","res_otp","res_status")