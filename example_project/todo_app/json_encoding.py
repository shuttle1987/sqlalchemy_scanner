"""Helper utility for encoding JSON"""
import enum
from flask.json import JSONEncoder

class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, enum.Enum):
            return o.value
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Let the base class default method raise the TypeError
        return JSONEncoder.default(self, o)