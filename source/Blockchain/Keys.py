from Crypto.PublicKey import RSA
from Crypto.Hash import SHA3_256, SHA3_384
from Crypto.Signature import pkcs1_15
import os


class KeysRSA:
    def __init__(self, save_path):
        if not os.path.isfile(save_path + '/private.pem') and os.path.isfile(save_path + '/public.pem'):
            length = 1024
            key = RSA.generate(length)
            private_key = key.export_key('PEM')
            file_out = open(save_path + '/private.pem', 'wb')
            file_out.write(private_key)

            public_key = key.publickey().export_key('PEM')
            file_out = open(save_path + '/public.pem', 'wb')
            file_out.write(public_key)
            self.private_key = private_key
            self.public_key = public_key
        else:
            self.private_key = open(save_path + '/private.pem').read()
            self.public_key = open(save_path + '/public.pem').read()

        self.address = SHA3_256.new().update(self.public_key)

    def sign(self, transaction_data: str):
        signer = pkcs1_15.new(RSA.import_key(self.private_key))
        hash_object = SHA3_384.new().update(transaction_data.encode('utf-8'))
        return signer.sign(hash_object)
