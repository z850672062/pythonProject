# pip install pycryptodome
# pip install python-alipay-sdk

from alipay import AliPay
import time
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArsU2tVMYttHJcngtAIcPu9QYe3xvIUKEW3nVMixdI6T5uSW9eySjGfxdETjNDcT1nTsDVLQ3k6wwm8zLzIUCytseZWeJFkATD/VhbHptnT5fzNJ2hE150A98jM5XEp2w/1IjRh2J6f98LPKt664fQizSEjPhLmL4OdRLLUjDqo5veouerPMqSkttlIIVy0qNxYO8JjrRozmWi1mlbQURMr6jZYwZxowb8PY04OQ/U/zgNdDV298ovwZ3VFCHWVMGRIKdF46RTgMo4FSTlMWB/lwQex6pyfTKbt5v7TQvcjSEu5mx8Cxt
-----END PUBLIC KEY-----"""
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEArsU2tVMYttHJcngtAIcPu9QYe3xvIUKEW3nVMixdI6T5uSW9eySjGfxdETjNDcT1nTsDVLQ3k6wwm8zLzIUCytseZWeJFkATD/VhbHptnT5fzNJ2hE150A98jM5XEp2w/1IjRh2J6f98LPKt664fQizSEjPhLmL4OdRLLUjDqo5veouerPMqSkttlIIVy0qNxYO8JjrRozmWi1mlbQURMr6jZYwZxowb8PY04OQ/U/zgNdDV298ovwZ3VFCHWVMGRIKdF46RTgMo4FSTlMWB/lwQex6pyfTKbt5v7TQvcjSEu5mx8Cxt+T27wOQXx9kSdIlq01L9c+tKzlrROd+WCQIDAQABAoIBAQCfIUIm53phO7LIX1PaXx+cTgncpfgpuH77K3tLK8nCYrxeMFbOgRVg27+Bps5N80AP4WOvBEh2VRoNQfNuTM22Fr0eZ58Se1Tf+vSx6OdVfS2NOTRgUorPPsqRCm+Nq7c1QnyLoumn/c/6vRxOs0QS5OyBVmt56PNK9Fle6hn+eCDL8p7+a6oKVVrcpjaoyNIcaeW5l51Qs7TSCwA+MZkF6AmWLArYZ2SLijFIqZ97QImsx7UUSAUuGac8pNYLqbBGiItQYJ4KQyK0kNfBE6VBcQUcRx+bcNjCKiQvH1X3vC53tJqYbe4rEm3V2yrgymHOCJ8LPILMytHFqFJmYQXhAoGBANzgjxMicXZ/yuq0QxQA+BFjN0z7iQPTWCP0CXS0fLI+S8zuRkj/inV3GXZp9eozOeaiJCO8UE9onx8qo93PwIWIHVFSfVVhxXjkVzZFPI+MLQTp+Ui8+ygV7KFoIW1NZU1UDn0482EEhmLUZky8vPTGvLT/iR1HZnLEUptGmDA/AoGBAMqPvoO2Hf96MYz99qTsD9tCS1OpJPSX5hdxu4lVGNTH5TtO/XZs8EwHGTJjdWKGzDhuFlPlJ/uZD1tcqG3iq610hiri6OEhrHREZEZF6RZS7L5Jq+9VmKjSOO1EFq72XSz0R+SFNwgcxCUqpG91Rrs+n6jNmHZA/AMtt4WdZKe3AoGAY2tkmy1Guxr8gDaRduCUyGbLToht/N3Vb6F53CEde7GUtvKNinATp5nrSSSav0c9ibVz5O3vjD7AWOv9hGrt8mz5HVCu/46ZrzfAlboGb2qeHPcf8QC3YCy2LVTMrwFGVs8+EllfG01JHBUU0veladxGtoXK9vXbhE8gC6pz+EsCgYEAvH4Aod4Bki/qFjJpptSIeNb685HtcrI7Ccvq4IPQhIizFnqNv/rlrUnZt5r3q8SWG1jN7CnNCAJJWRIjJYYNjW5mP1hBruW/7b2Kth3uJbjq1rQFi8RSN57QHHIEzbExyVhT4iHYsPLbz14cAB/YvvsqZVFUM46LNIYBRhPNi4cCgYEAkbTB73ZSA74PgdyML1WQCVIJff9NjEcl+O/xlRpxaWsflAcRcxChqpJKIoGIrwHBn/pKNoLscgwjMWFqGhiJHu1rd3rJEy62hyBYSZfElw/E3oSnpNL/lYQ1P8hfe0hztI60KzSGezysPE1sXpViYytHqzEQgdTK4scZbGt0RKg=
-----END RSA PRIVATE KEY-----"""

def get_pay(out_trade_no, total_amount, return_url):
    # 实例化支付应用
    alipay = AliPay(
        appid="2016102000726748",
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2"
    )
    # 发起支付请求
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单号，每次发送请求都不能一样
        out_trade_no=out_trade_no,
        # 支付金额
        total_amount=str(total_amount),
        # 交易信息
        subject="测试",
        return_url=return_url + '?t=' + out_trade_no,
        notify_url=return_url + '?t=' + out_trade_no
    )
    return 'https://openapi.alipaydev.com/gateway.do?'+ order_string
