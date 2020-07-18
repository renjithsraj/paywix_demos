import requests

payu_config = {
    "test": "https://sandboxsecure.payu.in/_payment",
    "live": "https://secure.payu.in/_payment",
    "api_test": "https://test.payumoney.com/payment/",
    "api_live": "https://www.payumoney.com/payment/",
}

required_data = {
    "payu_request": ['txnid', 'amount', 'productinfo', 'firstname', 'email'],
    "payu_payment_resp": ['transaction_ids']
}


def api_access(method, url, header, data=None):
    if method == 'post':
        re




    try:
            r = requests.get(cf_api_url + url,
                             data=json.dumps(data), headers=headers)
        except (requests.ConnectionError,
                requests.RequestException,
                requests.HTTPError,
                requests.Timeout,
                requests.TooManyRedirects) as e:
            raise self.CONNError(str(e))
        try:
            api_result = json.loads(r.text)
        except ValueError:
            raise self.APIError('JSON parse failed.')
        if api_result['result'] == 'error':
            raise self.APIError(api_result['msg'])
        return api_result 



