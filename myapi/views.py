from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,generics,status
from .serializers import *
from .models import * 


class BranchDetails(APIView):
	
	def get(self,request,*args,**kwargs):
		b_obj=Branches.objects.all()
		ifsccode=self.kwargs['ifsc_code']
		b_obj1=b_obj.filter(ifsc=ifsccode)
		resp={'error':'Ifsc_Code not found'}
		serializer=BranchesSerializer(b_obj1,many=True)
		if serializer.data:
			return Response(serializer.data)
		return Response(resp)

class BranchList(APIView):
	def get(self,request,*args,**kwargs):
		b_name=self.kwargs['bank_name']
		c_name=self.kwargs['city_name']
		b_obj=Banks.objects.filter(name=b_name).values('id')
		resp={'error':'No branches found'}
		for i in b_obj:
			b_id=i['id']
		#b=Banks.objects.raw('SELECT id from Banks where name=%s',[b_name])
		b_obj1=Branches.objects.raw('SELECT * from Branches where bank_id=%s AND city=%s',[b_id,c_name])
		serializer=BranchesSerializer(b_obj1,many=True)
		if serializer.data:
			return Response(serializer.data)
		return Response(resp)