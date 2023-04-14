from Modules.Core.Abstract.Exceptions.Exceptions import AbstractException


class STDException(AbstractException):
    pass


class STDCompileException(STDException):
    pass


class STDLexicalException(STDException):
    pass


class STDSyntaxException(STDException):
    pass


class STDNameBoundException(STDException):
    pass


class STDTranslationException(STDException):
    pass


class STDHasherException(STDException):
    pass


class STDEncryptException(STDException):
    pass


class STDDecryptException(STDException):
    pass


class STDObjectNotFoundException(STDException):
    pass


class STDREXCorruptionException(STDException):
    pass


class STDRVMRuntimeException(STDException):
    pass


class STDConnectionException(STDException):
    pass


class STDCorruptedDataException(STDException):
    pass


class STDServerInitializingException(STDException):
    pass


class STDClientInitializingException(STDException):
    pass


class STDOSManagerException(STDException):
    pass
