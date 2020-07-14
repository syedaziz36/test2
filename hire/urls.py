from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path("handlerequest/", views.handlerequest),
	path("loginpage/", views.loginpage, name="loginpage"),
	path("logoutpage/", views.logoutpage, name="logoutpage"),
	#path("testT1/", views.testT1, name="testT1"),
	path("developers/", views.developers, name="developers"),
	#path("testpaytm/", views.testpaytm, name="testpaytm"),
	path("user_registerpage/", views.user_registerpage, name="registerpage"),
	path("company_registerpage/", views.company_registerpage, name="registerpage"),
	path("company_profiles/", views.company_profiles, name="company_profiles"),
	path("provileView/<int:id>", views.provileView, name="provileView"),
	path("contactUser/<int:id>", views.contactUser, name="contactUser"),
	path("payment/", views.payment, name="payment"),
	path("discussion/", views.discussion, name="discussion"),
	path("apiss/", views.apiss, name="apiss"),
]
