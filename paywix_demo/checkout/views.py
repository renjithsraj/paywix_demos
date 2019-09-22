from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from paywix.payu import PAYU
from paywix.paytm import PayTm
payu = PAYU()
paytm = PayTm()

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
        print ("payu data us", payu_data)
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
        print ("before request", param_dict)
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

