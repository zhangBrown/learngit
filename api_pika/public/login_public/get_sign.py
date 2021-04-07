# -*- coding: utf-8 -*-
import json
import time
import base64

from Crypto.PublicKey import RSA as rsa
from Crypto.Cipher import PKCS1_v1_5

PUBLIC_KEY = u"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3SvlUR+LCJmHXqB4OADa
y1p2WEddfo8V7CnhdWtlAKYhj9V/joGJ6Y43L42+EKm6gELBXiOz77Q8xKi8x1HR
m6FGqHgrXx+7NsNxXR+gaL8WrY+WEPYvMFOxkDmWrcPfN0FvYWezwjZ+HQ/5bepJ
pqvXCibnDWSB3gCedxHKA9DGZHwzJfyB3KvYNMF81FvfvPlhf6L8YiUkXFGoSnqh
IpYEd7JEP2wWEbtxg+KnU86+l0T06d5A4AMXKXk/PtL/PMRWci1BUbeB+Ypre04n
hpcDwbgxR8EYdgBGxwb9DoTXxlOR55KoZXSuwu0GwPsgI/HtDl9k+ESiBQtsVyCY
MQIDAQAB
-----END PUBLIC KEY-----
"""


def get_sign(appkey="ac41@72*{%o}q@,8", length=200):
    """生成签名

    Parameters:
        appkey -- 分配给客户端App的key (问程序要)
        length -- 公钥是2048位证书，length=200
    """
    if appkey is None or len(appkey) < 16:
        raise RuntimeError(u'appkey长度不能小于16')
    cipher = PKCS1_v1_5.new(rsa.importKey(PUBLIC_KEY))
    data = {
        'timestamp': int(time.time()),
        'appkey': appkey,
    }
    raw = json.dumps(data)
    raw = raw.encode("utf8")
    ret = [
        cipher.encrypt(raw[i:i + length])
        for i in range(0, len(raw), length)
    ]
    return base64.b64encode(b''.join(ret))

if __name__ == '__main__':
    res = get_sign()
    print(res)
