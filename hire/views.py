from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm, UserProfileForm, CompanyProfileForm
from django.views.decorators.csrf import csrf_exempt
from hire.PayTm import Checksum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.mail import send_mail
from bs4 import BeautifulSoup
import requests
MERCHANT_KEY = 'neEU2tztbWhvm71i'

def home(request):
	obj1 = UserProfile1.objects.all()
	return render(request, 'hire/home.html', {"obj1":obj1})

def discussion(request):
	return render(request, 'hire/discussion.html')


def user_registerpage(request):
	print("intitiated")
	form = CreateUserForm(request.POST or None, request.FILES)
	profile_form = UserProfileForm(request.POST or None, request.FILES)
	print("constructor intitiated")
	if request.method == "POST":

		print("postmethod started... .............")
		for i in form:
			print(i)
		print(form.is_valid())

		print(profile_form.is_valid())
		if form.is_valid() and profile_form.is_valid():
			print("saving the form...................")
			user = form.save()
			print(user)
			print("user")
			profile = profile_form.save(commit = False)
			profile.user = user
			profile.save()
			print("saved forms.............")
	context = {"form":form, "profile_form":profile_form}
	return render(request, "hire/user_registerpage.html", context)





def company_registerpage(request):
	print("intitiated")
	form = CreateUserForm(request.POST or None, request.FILES)
	profile_form = CompanyProfileForm(request.POST or None, request.FILES)
	print("constructor intitiated")
	if request.method == "POST":

		print("postmethod started... .............")

		print(profile_form.is_valid())
		print(form.is_valid())
		if form.is_valid() and profile_form.is_valid():
			print("saving the form...................")
			user = form.save()
			print(user)
			print("user")
			profile = profile_form.save(commit = False)
			profile.user = user
			profile.save()
			print("saved forms.............")
	context = {"form":form, "profile_form":profile_form}
	return render(request, "hire/company_registerpage.html", context)





def loginpage(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			return render(request, 'hire/loginpage.html', {'error':'username or password is incorrect'})
	else:
		return render(request, 'hire/loginpage.html')




def logoutpage(request):
	logout(request)
	return redirect('loginpage')







def developers(request):
	print(request.user)
	obj1 = UserProfile1.objects.all()
	p2()
	return render(request, 'hire/developers.html', {"obj1":obj1})


def company_profiles(request):
	obj0 = CompanyProfile.objects.all()
	return render(request, 'hire/company_profiles.html',{"obj0":obj0})




def provileView(request, id):
	profileView_obj = UserProfile1.objects.filter(id=id)
	return render(request, 'hire/provileView.html',{"pv_obj":profileView_obj})


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    # h1=contactDB.objects.get()
    # user_name= h1.name
    # to_email = h1.user_email

    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            # user_message = f"hello {user_name}, \n\n\n we are pleased to inform you that you have been shortlisted for next round of interview by ........ \n please contact on +13333333333 for automated telephonic screening.\n\n we wish you all the very best for the remaining rounds :) \n\n\n Thanks and regards \n team iHireNow"
            # send_mail('no reply',user_message,'bloodconnectbb@gmail.com',[to_email], fail_silently=False,)
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'hire/paymentstatus.html', {'response': response_dict})


def payment(request):
	param_dict = {

                'MID': 'trRkea14983259577911',
                'ORDER_ID': "0008122",
                'TXN_AMOUNT': '20',
                'CUST_ID': "syedaziz873@gmail.com",
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/hire/handlerequest/',

        }
	param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
	return render(request, 'hire/paytm.html', {'param_dict': param_dict})

def contactUser(request, id):
	profileView_obj = UserProfile1.objects.get(pk=id)
	user_name1 = profileView_obj.user
	user_mail = User.objects.get(username=user_name1)
	user_email1=user_mail.email
	sn = request.user 
	# contactDB.objects.all().delete()
	# cont=contactDB(name= user_name1, user_email= user_email1, sender_name = sn)
	# cont.save()
	param_dict = {

                'MID': 'trRkea14983259577911',
                'ORDER_ID': "020034",
                'TXN_AMOUNT': '20',
                'CUST_ID': "syedaziz373@gmail.com",
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/hire/handlerequest/',

        }
	param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
	user_message = f"hello {user_name1}, \n\n\n we are pleased to inform you that you have been shortlisted for next round of interview by {sn} \n please contact on +13333333333 for automated telephonic screening.\n\n we wish you all the very best for the remaining rounds :) \n\n\n Thanks and regards \n team iHireNow" 
	send_mail('no reply',user_message,'bloodconnectbb@gmail.com',['syedaziz373@gmail.com'], fail_silently=False,)
	return render(request, 'hire/paytm.html', {'param_dict': param_dict})




# APIS ki kahani shuru....................................................
# APIS ki kahani shuru....................................................
# APIS ki kahani shuru....................................................
# APIS ki kahani shuru....................................................



# def getStackoverflowPoints(pro_url0):
# 	return("2")


# def getStackoverflowPoints(pro_url1):
# 	return("4")


# def getStackoverflowPoints(pro_url2):
# 	return("6")


# def getStackoverflowPoints(pro_url3):
# 	return("8")

# def getApis(request, lp):
# 	list_of_points = []
# 	for us in usrp1:
# 		p1 = getStackoverflowPoints(us.)
# 		p2 = getCodechefPoints(us.)
# 		p3 = getTechgigPoints(us.)
# 		p4 = getCodeforcesPoints(us.)
# 		l1=[p1,p2,p3,p4]
# 		list_of_points.append(l1,)


def p2():
	print("hello mai p2 hu")

def apiss(request):
	for i in range(1,3):
		p1 = UserProfile1.objects.get(id = i)
		print(p1.stackoverflow_link)
	p2 = UserProfile1.objects.get(id = 1)
	url 		=	p2.stackoverflow_link #url stackeroverflow
	url1		=	"https://www.codechef.com/users/gennady.korotkevich"   #url codechef
	url2		=	"https://www.hackerearth.com/@abhishek2018/activity/hackerearth/"    # url hacker earth
	url3		=	"http://codeforces.com/profile/ainta"		# url codeforce
	val		=	stkval(url)
	val1	=	codechef(url1)
	val2	=	hackerearth(url2)
	val3	=	codeforces(url3)
	return render(request, 'hire/apiss.html',{"h2_val":val, "val1":val1, "val2":val2, "val3":val3})

def codechef(codechef_url):
	url = codechef_url #url
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	source=requests.get(url, headers=headers).text
	soup = BeautifulSoup(source, 'html.parser')
	val = soup.find('div', {"class" : "rating-number"})
	#val0= soup.find('div', {"class": "inline-list"})
	val1=val.string
	return(val1)



def stkval(pro_url):
	url = pro_url #url
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	source=requests.get(url, headers=headers).text
	soup = BeautifulSoup(source, 'html.parser')
	val = soup.find('div', attrs={"id":"avatar-card"}).text
	st = val.split()
	st1=st.pop(1)
	return(st)


def hackerearth(hackerearth_url):
	url = hackerearth_url #url
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	source=requests.get(url, headers=headers).text
	soup = BeautifulSoup(source, 'html.parser')
	val = soup.find('table', attrs={"class" : "nice-table-2 align-center"})
	val0=val
	print(val0)
	#print(val.children)
	#val0= soup.find('div', {"class": "inline-list"})
	return(val)


def codeforces(codeforces_url):
	url = codeforces_url #url
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	source=requests.get(url, headers=headers).text
	soup = BeautifulSoup(source, 'html.parser')
	val = soup.find_all('span', attrs={"class" : "user-red"})
	print("lol")
	rating = val[1]
	print(rating.text)
	#print(val.children)
	#val0= soup.find('div', {"class": "inline-list"})
	return(rating.text)


# def codechef1(request, id):
# 	Scraped1 = Scraped.objects.filter(id=id)
# 	print(Scraped1)
# 	for i in Scraped1:
# 		print(i.id)
# 	return render(request, "hire/codechef.html", {"id":id,"Scraped1":Scraped1})

