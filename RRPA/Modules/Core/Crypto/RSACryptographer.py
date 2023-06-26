import rsa
from RRPA.Modules.Core.Abstract.Crypto.Cryptographer import AbstractCryptographer
from RRPA.AppData.Configs.CryptoConfig import RSA_KEY_SIZE


class STDRSACryptographer(AbstractCryptographer):

    def __init__(self):
        self._rsa_private_key = None
        self._rsa_public_key = None
        self._rsa_key_size = RSA_KEY_SIZE * 8

    def set_keys(self, *keys):
        if keys[0]:
            self._rsa_public_key = rsa.PublicKey.load_pkcs1(keys[0])
        if keys[1]:
            self._rsa_private_key = rsa.PrivateKey.load_pkcs1(keys[1])

    def generate_keys(self, key_type=None):
        (self._rsa_public_key, self._rsa_private_key) = rsa.newkeys(self._rsa_key_size)
        public_pem = self._rsa_public_key.save_pkcs1()
        return public_pem

    def encrypt(self, data):
        encrypted_text = rsa.encrypt(data, self._rsa_public_key)
        return encrypted_text

    def decrypt(self, data):
        decrypted_text = rsa.decrypt(data, self._rsa_private_key)
        return decrypted_text
