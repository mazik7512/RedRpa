from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from RRPA.Modules.Core.Abstract.Crypto.Cryptographer import AbstractCryptographer
from RRPA.AppData.Configs.CryptoConfig import AES_KEY_SIZE


class STDAESCryptographer(AbstractCryptographer):

    def __init__(self):
        self._cipher = None
        self._aes_key = None
        self._aes_key_size = AES_KEY_SIZE

    def set_keys(self, *keys):
        self._aes_key = keys[0]
        self._init_aes()

    def generate_keys(self, key_type=None):
        self._aes_key = get_random_bytes(self._aes_key_size)
        return self._aes_key

    def encrypt(self, data):
        encrypted_text = self._cipher.encrypt(pad(data, AES.block_size))
        return encrypted_text

    def decrypt(self, data):
        decrypted_text = unpad(self._cipher.decrypt(data), AES.block_size)
        return decrypted_text

    def _init_aes(self):
        self._cipher = AES.new(self._aes_key, AES.MODE_ECB)
