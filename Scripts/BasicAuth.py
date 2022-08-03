from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

USER_DATA = {
    'admin':'atCh_5K}?g'
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

class HelloWorld(Resource):
    @auth.login_required
    def get(self):
        return {'Hello':'World'}

api.add_resource(HelloWorld, '/hello_world')

if __name__ == '__main__':
    app.run(debug=True)