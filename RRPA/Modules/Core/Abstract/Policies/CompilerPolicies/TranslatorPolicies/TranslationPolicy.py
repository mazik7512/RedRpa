from abc import ABC, abstractmethod


class AbstractTranslationPolicy(ABC):

    @staticmethod
    @abstractmethod
    def translate_expr(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_loop(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_loop_header(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_func_def(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_func_def_arg_list(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_body(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_func_def_arg(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_func_call(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_func_call_arg_list(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_func_call_arg(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_assigment(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_body_line(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_line(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_scenario(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_object(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_str_literal(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_number_literal(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_return(node):
        pass

    @staticmethod
    @abstractmethod
    def translate_return_arg(node):
        pass
