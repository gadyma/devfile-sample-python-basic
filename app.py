from flask import Flask, request
import os


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name')
    
    return "Hello " + name + "!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
