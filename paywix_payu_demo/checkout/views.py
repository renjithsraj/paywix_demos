from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from paywix.payu import Payu
from django.conf import settings
from django.contrib.auth.decorators import login_required
from checkout.models import Transaction
from django.shortcuts import get_object_or_404


payu_config = settings.PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')

payu = Payu(merchant_key, merchant_salt, surl, furl, mode)

# Home page


def home(request):
    return render(request, 'home.html', {})


# Payu checkout page
@csrf_exempt
@login_required
def payu_checkout(request):
    checkout_payload = {"amount": 130,
                        "firstname": "renjith", "email": "renjithsraj@live.com",
                        "phone": 9746272610, "lastname": "s raj", "productinfo": "Test Product",
                        "address1": "Test address 1", "address2": "Test Address 2", "city": "Test city",
                        "state": "Test state", "country": "Test country", "zipcode": 673576}
    if request.method == 'POST':
        import uuid
        data = {k: v[0] for k, v in dict(request.POST).items()}
        # No Transactio ID's
        txnid = uuid.uuid1()
        data.pop('csrfmiddlewaretoken')
        data.update({"txnid": txnid})
        payu_data = payu.transaction(**data)
        # # data save db
        transaction = Transaction.objects.create(user=request.user, txn_id=txnid, txn_status='SIN',
                                                 amount=data.get('amount'), request_data=data,
                                                 requested_hash=payu_data.get('hashh'))
        return render(request, 'payu_checkout.html', {"posted": payu_data})
    return render(request, 'payu.html', {'posted': checkout_payload})


# Payu success return page
@csrf_exempt
def payu_success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    txn_id = data.get('txnid')
    transaction = get_object_or_404(Transaction, txn_id=txn_id)
    transaction.response_data = data
    transaction.reponse_hash = data['recived_hash']
    transaction.payumoney_id = data['return_data']['payuMoneyId']
    transaction.save()
    response = payu.verify_transaction(data)
    return JsonResponse(response)


# Payu failure page
@csrf_exempt
def payu_failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)
