from flask import Flask
app = Flask(__name__)

def make_lowercase(function):
    def wrapper():
        func = function()
        lowercase = func.lower()
        return lowercase
    
    return wrapper

@app.route('/')
@make_lowercase
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()