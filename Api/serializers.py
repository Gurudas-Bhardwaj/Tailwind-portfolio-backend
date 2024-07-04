from rest_framework import serializers
from MyApp.models import ContactModel

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model=ContactModel
        fields=['Name',"Email","Number","Subject","Message"]