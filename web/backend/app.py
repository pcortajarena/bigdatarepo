from flask import Flask, request
from model import WeatherRequest
from model import WeatherResponse
import jsonstruct as jst
app = Flask(__name__)

def body(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap

@app.route("/", methods=['POST'])
@body(WeatherRequest)
def get_energy(weatherRequest):
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()