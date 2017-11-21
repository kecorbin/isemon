from flask_restful_swagger import swagger
from flask_restful import fields

@swagger.model
class FailureReasonObject(object):
    resource_fields = {
      '@id': fields.String,
      'code': fields.String,
      'cause': fields.String
      }

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
