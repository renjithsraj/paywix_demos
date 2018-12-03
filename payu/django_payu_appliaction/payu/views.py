from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.template.loader import get_template
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from paywix.payu import PAYU
from django.conf import settings
payu = PAYU()

def payment(request):
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	# payment_data = {
	# 				'txnid': txnid,
	# 				'amount': '10',
	# 				'firstname': 'Renjith',
	# 				'email': 'leena102795@gmail.com',
	# 				'phone': '9746272610',
	# 				'productinfo': 'trst',
	# 				'lastname': 's raj',
	# 				'address1': 'No 14 , OLD NO 6 A, first floor #1, Karunanithi Nagar 6th steet, taramani',
	# 				'address2': 'dsadasd',
	# 				'city': 'Chennai',
	# 				'state': 'Tamilnadu',
	# 				'country': 'India',
	# 				'zipcode': '600113',
	# 				'udf1': 'dsad',
	# 				'udf2': 'dsfsf',
	# 				'udf3': 'sdffsdf',
	# 				'udf4': 'dfsfds',
	# 				'udf5': 'fsdfsdf'
	# 				}
	payment_data = {
					'txnid': txnid,
					'amount': '10',
					'firstname': 'Renjith',
					'email': 'leena102795@gmail.com',
					'phone': '9746272610',
					'productinfo': 'trst'
					}
	payu_data = payu.initate_transaction(payment_data)
	return render(request, 'payment_form.html',{"posted":payu_data})





@csrf_protect
@csrf_exempt
def payment_success(request):
	payu_success_data = payu.check_hash(dict(request.POST))
	return JsonResponse(payu_success_data)


@csrf_protect
@csrf_exempt
def payment_failure(request):
	payu_failure_data = payu.check_hash(dict(request.POST))
	return JsonResponse(payu_failure_data)