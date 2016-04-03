from hashlib import sha1
import hmac
import base64

my_sign = hmac.new('2NHSfWYvdwnI3MlSfcX5UGdCdNXE6u7X', 'POSTcvm.api.qcloud.com/v2/index.php?Action=TextSentiment&Nonce=345122&Region=sz&SecretId=AKIDIJTFzGr1K0KMfHwpxWbi58LoWOkOR9fk&Timestamp=1459669409&instanceIds.0=qcvm12345&instanceIds.1=qcvm56789', sha1).digest()


my_sign = base64.b64encode(my_sign)
print my_sign
