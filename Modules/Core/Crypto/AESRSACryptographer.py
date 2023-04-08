from Modules.Core.Abstract.Crypto.Cryptographer import AbstractCryptographer
import rsa
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from AppData.Configs.CryptoConfig import RSA_KEY_SIZE
from AppData.Configs.CryptoConfig import AES_KEY_SIZE


class STDCryptographer(AbstractCryptographer):

    def __init__(self):
        self._cipher = None
        self._aes_key = None
        self._aes_key_size = AES_KEY_SIZE
        self._rsa_private_key = None
        self._rsa_public_key = None
        self._rsa_key_size = RSA_KEY_SIZE * 8

    def init_aes(self):
        self._cipher = AES.new(self._aes_key, AES.MODE_ECB)

    def _generate_rsa_keys(self):
        (self._rsa_public_key, self._rsa_private_key) = rsa.newkeys(self._rsa_key_size)
        public_pem = self._rsa_public_key.save_pkcs1()
        return public_pem

    def _generate_aes_key(self):
        self._aes_key = get_random_bytes(self._aes_key_size)
        return self._aes_key

    def _key_encryption(self, data):
        return rsa.encrypt(data, self._rsa_public_key)

    def generate_keys(self):
        rsa_public_key = self._generate_rsa_keys()
        aes_key = self._generate_aes_key()
        aes_key = self._key_encryption(aes_key)
        return rsa_public_key, aes_key

    def set_keys(self, *keys):
        if keys[0]:
            self._rsa_public_key = rsa.PublicKey.load_pkcs1(keys[0])
        if keys[1]:
            self._aes_key = self._key_decryption(keys[1])
            self.init_aes()

    def _key_decryption(self, encrypted_aes_key):
        return rsa.decrypt(encrypted_aes_key, self._rsa_private_key)

    def encrypt(self, data):
        encrypted_text = self._cipher.encrypt(pad(data, AES.block_size))
        return encrypted_text

    def decrypt(self, data):
        decrypted_text = unpad(self._cipher.decrypt(data), AES.block_size)
        return decrypted_text
