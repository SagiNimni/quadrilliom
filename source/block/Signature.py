from Crypto.PublicKey import RSA


def rsa_keys(address):
    length = 1024
    key = RSA.generate(length)
    private_key = key.export_key('PEM')
    file_out = open(address + '/private.pem', 'wb')
    file_out.write(private_key)

    public_key = key.publickey().export_key('PEM')
    file_out = open(address + '/public.pem', 'wb')
    file_out.write(public_key)
    return private_key, public_key
