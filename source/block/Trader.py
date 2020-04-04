from block.Signature import *
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA3_384, SHA3_256
import os


class Wallet:
    def __init__(self):
        self.number_of_transactions = 0
        self.keys = []

    def connect_to_private_key(self, keys_path):  # TODO public key can be created by private key
        private_path = keys_path + "/private.pem"
        public_path = keys_path + "/public.pem"
        if os.path.isfile(private_path) and os.path.isfile(public_path):
            public_key = open(public_path).read()
            private_key = open(private_path).read()
            coin_address = SHA3_256.new().update(public_key.encode('utf-8'))
            self.keys.append({'private': public_key, 'public': private_key, 'address': coin_address})
        else:
            permission = input('Keys are not valid. do you want to create them?')
            if permission == 'yes':
                private_key, public_key = rsa_keys()
                coin_address = SHA3_256.new().update(public_key.encode('utf-8'))
                self.keys.append({'private': public_key, 'public': private_key, 'address': coin_address})

    def sign(self, transaction_data):
        signer = pkcs1_15.new(RSA.import_key(self.private_key))
        hash_object = SHA3_384.new().update(transaction_data.encode('utf-8'))
        return signer.sign(hash_object)

    def pay(self, amount: float, recipient_public_key):
        """
        Broadcasts the wanted paying statement with signature

        :param recipient_public_key: The public key of the person who gets the payment
        :return:
        """
        payment = str(self.number_of_transactions) + str(self.public_key) + "  pays  " + \
                    str(recipient_public_key) + "  " + str(amount) + " quadrillioms.  signature:  "
        signature = self.sign(payment)
