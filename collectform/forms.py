from django.forms import ModelForm
from .models import DistributionRequests

class DistributionRequestForm(ModelForm):

    class Meta:
        model = DistributionRequests
