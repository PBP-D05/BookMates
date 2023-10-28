from django.forms import ModelForm, CharField, Form
from .models import *
 
class CreateCommunity(ModelForm):
    class Meta:
        model = Community
        fields = "__all__"

class JoinCommunityForm(Form):
    join_code = CharField(max_length=6, required=True)