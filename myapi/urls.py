from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
	#path('/<ifsccode>',views.BranchDetails)
	#path('branchlist/<str:bankname>',views.branchList)
	#url(r'^admin/',admin.site.urls),
	url(r'^branchdetails/(?P<ifsc_code>\w+)/$',views.BranchDetails.as_view()),
	url(r'^branchlist/(?P<bank_name>.+?)/(?P<city_name>\w+)/$',views.BranchList.as_view())
]
