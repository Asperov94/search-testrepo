from flask import Flask, request
import json
import r



app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    result = request.get_json(force=True)
    x=result[6:]
    print(x)
    return(result)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
