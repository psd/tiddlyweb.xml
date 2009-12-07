"""
XML TiddlyWeb serializer.
"""

from tiddlywebplugins.simplerizer import Simplerization as SerializationInterface
from tiddlywebplugins.xml.marshaller import dumps, loads

__version__ = "0.1"
 
def init(config):
    # register serializer
    content_type = "text/xml"
    config["extension_types"]["xml"] = content_type
    config["serializers"][content_type] = [__name__, "text/xml; charset=UTF-8"]

class Serialization(SerializationInterface):
    """Access TiddlyWeb resources using the XML representation."""

    def dump(self, object):
        """Dump a dictionary object to a XML string."""
        return dumps(object)

    def load(self, input_string):
        """Load a dictionary object from a XML string."""
        return loads(input_string)
