from flask_restful_swagger_2 import swagger, Schema
from flask_restful import fields


class FailureReasonSwaggerModel(Schema):
    type = 'object'
    properties = {
        'id': {
            'type': 'string',
            'example': '100001'
        },
        'code': {
            'type': '100001 AUTHMGR-5-FAIL Authorization failed for client'
        },
        'cause': {
            'type': 'This may or may not be indicating a violation'
        },
        'resolution': {
            'type': "Please review and resolve according to your organization's policy"
        }
    }

class FailureReasonObject(object):
    def __init__(self, **kwargs):
        self._attributes = kwargs

    @classmethod
    def from_dict(cls, dikt):
        obj = cls(**dikt)
        return obj

    @property
    def id(self):
        print self._attributes
        return self._attributes.get("@id", None)

    @property
    def code(self):
        return self._attributes.get("code", None)

    @property
    def cause(self):
        return self._attributes.get("cause", None)

    @property
    def resolution(self):
        return self._attributes.get("resolution", None)
