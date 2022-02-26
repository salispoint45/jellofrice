import hashlib


def return_password():
    secret = 'the rain in Spain falls mainly in the plain'
    bsecret = secret.encodes()
    m = hashlib.md5()
    m.update(bsecret)
    return m.digest()
