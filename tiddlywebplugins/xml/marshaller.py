"""
Specialization of pyxml's marshaling to apply 
more document style markup and handle Unicode.
"""

from __future__ import absolute_import

import os
os.environ['PY_USE_XMLPLUS'] = '1'

from xml.marshal import generic

class Marshaller(generic.Marshaller):
    tag_unicode = 'unicode'

    def m_unicode(self, value, dict):
        name = self.tag_unicode
        L = ['<' + name + '>']
        s = value.encode('utf-8')
        if '&' in s or '>' in s or '<' in s:
            s = s.replace('&', '&amp;')
            s = s.replace('<', '&lt;')
            s = s.replace('>', '&gt;')
        L.append(s)
        L.append('</' + name + '>')
        return L


class Unmarshaller(generic.Unmarshaller):
    def __init__(self):
        self.unmarshal_meth['unicode'] = ('um_start_unicode','um_end_unicode')
        generic.Unmarshaller.__init__(self)

    um_start_unicode = generic.Unmarshaller.um_start_generic

    def um_end_unicode(self, name):
        ds = self.data_stack
        ds[-1] = ''.join(ds[-1])
        self.accumulating_chars = 0

def dumps(input_string):
    return Marshaller().dumps(input_string)

def loads(object):
    return Unmarshaller().loads(object)
