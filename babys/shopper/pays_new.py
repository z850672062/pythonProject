# pip install pycrypto
# pip install alipay-sdk-python
# 买家账号：ltyavg2644@sandbox.com
# 登录和支付密码：111111



import logging
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')


alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArsU2tVMYttHJcngtAIcPu9QYe3xvIUKEW3nVMixdI6T5uSW9eySjGfxdETjNDcT1nTsDVLQ3k6wwm8zLzIUCytseZWeJFkATD/VhbHptnT5fzNJ2hE150A98jM5XEp2w/1IjRh2J6f98LPKt664fQizSEjPhLmL4OdRLLUjDqo5veouerPMqSkttlIIVy0qNxYO8JjrRozmWi1mlbQURMr6jZYwZxowb8PY04OQ/U/zgNdDV298ovwZ3VFCHWVMGRIKdF46RTgMo4FSTlMWB/lwQex6pyfTKbt5v7TQvcjSEu5mx8Cxt+T27wOQXx9kSdIlq01L9c+tKzlrROd+WCQIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEArsU2tVMYttHJcngtAIcPu9QYe3xvIUKEW3nVMixdI6T5uSW9eySjGfxdETjNDcT1nTsDVLQ3k6wwm8zLzIUCytseZWeJFkATD/VhbHptnT5fzNJ2hE150A98jM5XEp2w/1IjRh2J6f98LPKt664fQizSEjPhLmL4OdRLLUjDqo5veouerPMqSkttlIIVy0qNxYO8JjrRozmWi1mlbQURMr6jZYwZxowb8PY04OQ/U/zgNdDV298ovwZ3VFCHWVMGRIKdF46RTgMo4FSTlMWB/lwQex6pyfTKbt5v7TQvcjSEu5mx8Cxt+T27wOQXx9kSdIlq01L9c+tKzlrROd+WCQIDAQABAoIBAQCfIUIm53phO7LIX1PaXx+cTgncpfgpuH77K3tLK8nCYrxeMFbOgRVg27+Bps5N80AP4WOvBEh2VRoNQfNuTM22Fr0eZ58Se1Tf+vSx6OdVfS2NOTRgUorPPsqRCm+Nq7c1QnyLoumn/c/6vRxOs0QS5OyBVmt56PNK9Fle6hn+eCDL8p7+a6oKVVrcpjaoyNIcaeW5l51Qs7TSCwA+MZkF6AmWLArYZ2SLijFIqZ97QImsx7UUSAUuGac8pNYLqbBGiItQYJ4KQyK0kNfBE6VBcQUcRx+bcNjCKiQvH1X3vC53tJqYbe4rEm3V2yrgymHOCJ8LPILMytHFqFJmYQXhAoGBANzgjxMicXZ/yuq0QxQA+BFjN0z7iQPTWCP0CXS0fLI+S8zuRkj/inV3GXZp9eozOeaiJCO8UE9onx8qo93PwIWIHVFSfVVhxXjkVzZFPI+MLQTp+Ui8+ygV7KFoIW1NZU1UDn0482EEhmLUZky8vPTGvLT/iR1HZnLEUptGmDA/AoGBAMqPvoO2Hf96MYz99qTsD9tCS1OpJPSX5hdxu4lVGNTH5TtO/XZs8EwHGTJjdWKGzDhuFlPlJ/uZD1tcqG3iq610hiri6OEhrHREZEZF6RZS7L5Jq+9VmKjSOO1EFq72XSz0R+SFNwgcxCUqpG91Rrs+n6jNmHZA/AMtt4WdZKe3AoGAY2tkmy1Guxr8gDaRduCUyGbLToht/N3Vb6F53CEde7GUtvKNinATp5nrSSSav0c9ibVz5O3vjD7AWOv9hGrt8mz5HVCu/46ZrzfAlboGb2qeHPcf8QC3YCy2LVTMrwFGVs8+EllfG01JHBUU0veladxGtoXK9vXbhE8gC6pz+EsCgYEAvH4Aod4Bki/qFjJpptSIeNb685HtcrI7Ccvq4IPQhIizFnqNv/rlrUnZt5r3q8SWG1jN7CnNCAJJWRIjJYYNjW5mP1hBruW/7b2Kth3uJbjq1rQFi8RSN57QHHIEzbExyVhT4iHYsPLbz14cAB/YvvsqZVFUM46LNIYBRhPNi4cCgYEAkbTB73ZSA74PgdyML1WQCVIJff9NjEcl+O/xlRpxaWsflAcRcxChqpJKIoGIrwHBn/pKNoLscgwjMWFqGhiJHu1rd3rJEy62hyBYSZfElw/E3oSnpNL/lYQ1P8hfe0hztI60KzSGezysPE1sXpViYytHqzEQgdTK4scZbGt0RKg=
-----END RSA PRIVATE KEY-----"""
alipay_client_config = AlipayClientConfig()
alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
alipay_client_config.app_id = '2021000117675633'
alipay_client_config.app_private_key = app_private_key_string
alipay_client_config.alipay_public_key = alipay_public_key_string
client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)

def get_pay(out_trade_no, total_amount, return_url):
    model = AlipayTradePagePayModel()
    model.out_trade_no = out_trade_no
    model.total_amount = str(total_amount)
    model.subject = "测试"
    model.body = "支付宝测试"
    model.product_code = "FAST_INSTANT_TRADE_PAY"

    request = AlipayTradePagePayRequest(biz_model=model)

    request.notify_url = return_url + '?t=' + out_trade_no
    request.return_url = return_url + '?t=' + out_trade_no
    response = client.page_execute(request, http_method="GET")
    return response