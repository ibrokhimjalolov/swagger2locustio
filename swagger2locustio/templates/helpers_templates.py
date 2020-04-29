from jinja2 import Template

HELPER_MAPPING = {}
HELPER_MAPPING.update(dict.fromkeys(["int", "integer", "int32", "int64"], "Helper.get_int_value"))
HELPER_MAPPING.update(dict.fromkeys(["float", "double", "number"], "Helper.get_float_value"))
HELPER_MAPPING.update(dict.fromkeys(["bool", "boolean"], "Helper.get_float_value"))
HELPER_MAPPING.update(dict.fromkeys(["null"], "Helper.get_null_value"))
HELPER_MAPPING.update(dict.fromkeys(["str", "string"], "Helper.get_string_value"))

HELPER_CLASS_TEMPLATE = Template("""import datetime
import random
import string


class Helper:
    @staticmethod
    def get_int_value(start: int = -100, end: int = 100):
        return random.randint(start, end)
        
    @staticmethod
    def get_float_value(start: int = -100, end: int = 100):
        return random.random() * Helper.get_int_value(start, end)
        
    @staticmethod
    def get_bool_value():
        return random.choice([True, False])
        
    @staticmethod
    def get_null_value():
        return None
        
    @staticmethod
    def get_string_value(min_len: int = 0, max_len: int = 100):
        string_len = Helper.get_int_value(min_len, max_len)
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=string_len))

""")
