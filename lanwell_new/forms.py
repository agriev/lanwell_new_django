from django.forms import ModelForm, Textarea
from lanwell_new.models import CustomerRequest

class CustomerForm(ModelForm):
    class Meta:
        model = CustomerRequest
        fields = '__all__'
        widgets = {
            'description' : Textarea(attrs={'rows' : 10})
        }