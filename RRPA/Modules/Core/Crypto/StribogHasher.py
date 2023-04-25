from RRPA.Modules.Core.Abstract.Crypto.Hasher import AbstractHasher
import ctypes
from RRPA.AppData.Configs.CryptoConfig import STRIBOG_DLL_PATH
from RRPA.AppData.Configs.CryptoConfig import HASH_SIZE


class STDHasher(AbstractHasher):
    def __init__(self, hash_size=HASH_SIZE):
        self._lib_path = STRIBOG_DLL_PATH
        self._hash_size = hash_size
        self._hasher = ctypes.CDLL(self._lib_path)
        if self._hash_size == 64:
            self._hash_func = self._hasher.StribogHash512
        elif self._hash_size == 32:
            self._hash_func = self._hasher.StribogHash256

    def _get_empty_string(self):
        return '0' * self._hash_size

    def hash_string(self, data: str):
        result = self._get_empty_string().encode('utf-8')
        self._hash_func(data, len(data), result)
        return int.from_bytes(result, "big")

    def hash_array(self, data):
        result = self._get_empty_string().encode('utf-8')
        self._hash_func(data, len(data), result)
        return int.from_bytes(result, "big")

    def hash_int(self, data: int):
        result = self._get_empty_string().encode('utf-8')
        iv_data = data.to_bytes(data.__sizeof__(), "big")
        self._hash_func(iv_data, len(iv_data), result)
        return int.from_bytes(result, "little")
