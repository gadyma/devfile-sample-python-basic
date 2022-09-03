from flask import Flask, request
import os


app = Flask(__name__)

name_list = []

@app.route('/')
def hello():
    name = request.args.get('name')
    
    if name != None:
        name_list.append(name)    

    name_str = "\n".join(name_list)
    return "Hello users\n" + name_str

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
