from RRPA.Modules.Core.Abstract.Network.Utils.NetworkUtils import AbstractUtils
from RRPA.Modules.Core.Crypto.StribogHasher import STDHasher


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
        len_tmp = len(temp_data)
        if len_tmp < 3:
            return None, None, None
        elif len_tmp > 3:
            data = temp_data[1]
            for i in range(2, len_tmp - 1):
                data += temp_data[i]
            return temp_data[0], data, temp_data[len_tmp - 1]
        operation_type = temp_data[0]
        raw_data = temp_data[1]
        _hash = temp_data[2]
        return int(operation_type), raw_data, _hash



