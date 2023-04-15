from Modules.Core.Abstract.Exceptions.Exceptions import AbstractException


class STDException(AbstractException):
    def __init__(self, exception_data, *args):
        super().__init__(args)
        self._exception_data = exception_data

    def get_exception_data(self):
        return self._exception_data

    def __str__(self):
        return super().__str__() + str(self._exception_data)


class STDCompileException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDLexicalException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDSyntaxException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDNameBoundException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDTranslationException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDHasherException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDEncryptException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDDecryptException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDObjectNotFoundException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDREXCorruptionException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDRVMRuntimeException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDConnectionException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDCorruptedDataException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDServerInitializingException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDClientInitializingException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)


class STDOSManagerException(STDException):
    def __init__(self, exception_data, *args):
        super().__init__(exception_data, args)
