from RRPA.Modules.Core.Abstract.Policies.CompilerPolicies.NameBoundingPolicies.InitPolicy import AbstractInitPolicy


class STDInitPolicy(AbstractInitPolicy):

    @staticmethod
    def generate_init_api(*args):
        return "{} = {}({})".format(args[0], args[1], args[2])

    @staticmethod
    def generate_init_tools(*args):
        init_string = args[0] + " = " + "{"
        init_string += "'os': " + args[1] + ", "
        init_string += "'web': " + args[2]
        init_string += "}"
        return init_string
