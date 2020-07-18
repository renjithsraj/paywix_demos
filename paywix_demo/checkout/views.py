from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from checkout.payu import Payu
from django.conf import settings

payu_config = settings.PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')

payu = Payu(merchant_key, merchant_salt, surl, furl, mode)




import uuid

# Home page
def home(request):
    return render(request, 'home.html', {})


# Payu checkout page
@csrf_exempt
def payu_checkout(request):
    if request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        data.pop('csrfmiddlewaretoken')
        data.update({"txnid": payu.generate_txnid(prefix="tmk")})
        payu_data = payu.transaction(**data)
        return render(request, 'payu_checkout.html', {"posted": payu_data})
    return render(request, 'payu.html', {})



# Payu success return page
@csrf_exempt
def payu_success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)


# Payu failure page
@csrf_exempt
def payu_failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)
