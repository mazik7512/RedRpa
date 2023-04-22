from RRPA.Modules.Core.Abstract.Crypto.Cryptographer import AbstractCryptographer
from RRPA.Modules.Core.Crypto.AESCryptographer import STDAESCryptographer
from RRPA.Modules.Core.Crypto.RSACryptographer import STDRSACryptographer
from RRPA.AppData.Configs.CryptoConfig import RSA_KEY_SIZE
from RRPA.AppData.Configs.CryptoConfig import AES_KEY_SIZE


class STDAESRSACryptographer(AbstractCryptographer):

    def __init__(self):
        self._aes = STDAESCryptographer()
        self._rsa = STDRSACryptographer()

    def generate_keys(self):
        rsa_public_key = self._rsa.generate_keys()
        _aes_key = self._aes.generate_keys()
        aes_key = self._rsa.encrypt(_aes_key)
        return rsa_public_key, aes_key

    def set_keys(self, *keys):
        if keys[0]:
            self._rsa.set_keys(keys[0], None)
        if keys[1]:
            key = self._rsa.decrypt(keys[1])
            self._aes.set_keys(key)

    def encrypt(self, data):
        encrypted_text = self._aes.encrypt(data)
        return encrypted_text

    def decrypt(self, data):
        decrypted_text = self._aes.decrypt(data)
        return decrypted_text
