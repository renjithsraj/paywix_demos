from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from paywix.payu import PAYU
from paywix.paytm import PayTm
from paywix.cashfree import  Cashfree
payu = PAYU()
paytm = PayTm()
cashfree = Cashfree()

import uuid

# Home page
def home(request):
    return render(request, 'home.html', {})


# Payu checkout page
@csrf_exempt
def payu_checkout(request):
    if request.method == 'POST':
        data = dict(zip(request.POST.keys(), request.POST.values()))
        data['txnid'] = payu.generate_txnid()
        payu_data = payu.initiate_transaction(data)
        return render(request, 'payu_checkout.html', {"posted": payu_data})
    return render(request, 'payu.html', {})


def paytm_checkout(request):
    amount = 10
    if amount:
        order_id = paytm.id_generater()
        data_dict = {
            'ORDER_ID': order_id,
            'TXN_AMOUNT': amount,
            'CUST_ID': "renjithsraj@live.com",
        }
        param_dict = paytm.initiate_transaction(data_dict)
        return render(request, "paytm_checkout.html", {'paytmdict': param_dict})

# Payu success return page
@csrf_exempt
def payu_success(request):
    data = dict(zip(request.POST.keys(), request.POST.values()))
    response = payu.check_hash(data)
    return JsonResponse(response)


# Payu failure page
@csrf_exempt
def payu_failure(request):
    data = dict(zip(request.POST.keys(), request.POST.values()))
    response = payu.check_hash(data)
    return JsonResponse(response)

@csrf_exempt
def paytm_response(request):
    print("paytm response")
    data = dict(zip(request.POST.keys(), request.POST.values()))
    response = paytm.verify_hash(data)
    return JsonResponse(response)


def stripe_checkout(request):
    stripe_data = {
        "STRIPE_TOKEN": "pk_test_FIqmXI5IJDXr7Mt9OjsJ2Wda",
        "amount": 10, "order_id": str(uuid.uuid1()),
        "currency": "usd", "description": "TEST Prodcut"}
    return render(request, 'stripe.html', {'data': stripe_data})

def cashfree_checkout(request):
    data = {}
    data.update({'order_id': cashfree.generate_txnid()})

    if request.method == 'POST':
        # Make sure that the details are stored in the db
        data = dict(zip(request.POST.keys(), request.POST.values()))
        data.pop('csrfmiddlewaretoken')
        pgdata = cashfree.initiate_transaction(data)
        return render(request, 'cashfree_checkout.html', {'postData': pgdata})
    else:
        return render(request, 'cashfree.html', {'posted': data})

@csrf_exempt
def cashfree_response_return(request):
    data = dict(zip(request.POST.keys(), request.POST.values()))
    response = cashfree.verify_hash(data)
    return JsonResponse(response)