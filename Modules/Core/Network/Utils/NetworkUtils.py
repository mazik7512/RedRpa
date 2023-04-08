from Modules.Core.Abstract.Network.Utils.NetworkUtils import AbstractUtils
from Modules.Core.Crypto.StribogHasher import STDHasher


class STDUtils(AbstractUtils):
    __HASHER = STDHasher()

    @staticmethod
    def hash_data(raw_data):
        if type(raw_data) == str:
            return STDUtils.__HASHER.hash_string(raw_data)
        elif type(raw_data) == int:
            return STDUtils.__HASHER.hash_int(raw_data)
        elif type(raw_data) == bytes:
            return STDUtils.__HASHER.hash_array(raw_data)

    @staticmethod
    def parse_protocol(raw_data):
        temp_data = raw_data.split(":")
        if len(temp_data) != 3:
            return None, None, None
        operation_type = temp_data[0]
        raw_data = temp_data[1]
        _hash = temp_data[2]
        return int(operation_type), raw_data, _hash



