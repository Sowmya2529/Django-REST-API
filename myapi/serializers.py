# serializers.py
from .models import *
from rest_framework import serializers, fields


class BanksSerializer(serializers.ModelSerializer):
	#branch_details = BranchesSerializer(read_only=True,many=True)
	class Meta:
		model = Banks
		fields = '__all__'


class BranchesSerializer(serializers.ModelSerializer):
   class Meta:
   		model = Branches
   		fields = '__all__'


