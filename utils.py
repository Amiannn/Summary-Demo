from app import app

from flask import request
from flask import jsonify
from flask import make_response
from flask import render_template

class response():
    def __init__(self):
        self.message    = ''
        self.data       = {}
        self.statusCode = 200

    def toDict(self):
        return {'message': self.message, 'data': self.data}

class router():
    index = 0
    @staticmethod
    def _getcontrollername():
        router.index += 1
        return 'controller_{}'.format(router.index)

    @staticmethod
    def _route(url, methods, authentication, adminAuthorization, controller):
        def _controller(*args, **kwds):
            req, res = request, response()
            try:
                req.url_variable = kwds
                # check authentication
                if authentication is not None:
                    authentication(req, res)
                    if res.statusCode >= 400:
                        return make_response(jsonify(res.toDict()), res.statusCode)
                # check adminAuthorization
                if adminAuthorization is not None:
                    adminAuthorization(req, res)
                    if res.statusCode >= 400:
                        return make_response(jsonify(res.toDict()), res.statusCode)
                # do the control
                controller(req, res)
                return make_response(jsonify(res.toDict()), res.statusCode)
            except Exception as e:
                res.message, res.statusCode = 'Something went worng: {}'.format(str(e)), 400
                return make_response(jsonify(res.toDict()), res.statusCode)
        # change endpoint name
        _controller.__name__ = router._getcontrollername()
        # add to route
        app.route(url, methods=methods)(_controller)

    @staticmethod
    def get(url, authentication=None, adminAuthorization=None, controller=None):
        router._route(url, ['GET'], authentication, adminAuthorization, controller)
        
    @staticmethod
    def post(url, authentication=None, adminAuthorization=None, controller=None):
        router._route(url, ['POST'], authentication, adminAuthorization, controller)
        
    @staticmethod
    def put(url, authentication=None, adminAuthorization=None, controller=None):
        router._route(url, ['PUT'], authentication, adminAuthorization, controller)

    @staticmethod
    def delete(url, authentication=None, adminAuthorization=None, controller=None):
        router._route(url, ['DELETE'], authentication, adminAuthorization, controller)