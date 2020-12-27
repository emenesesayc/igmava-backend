import os
import random

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
bind_port = int(os.environ['BIND_PORT'])


@app.route('/')
def hello():
    redis.incr('hits')
    total_hits = redis.get('hits').decode()
    random.seed(int(total_hits))
    tarot=["La Muerte","La Torre","La Ardilla","La Estrella","El Sol","La Luna","El Mundo","El Diablo","El Ahorcado","El Emperador","La Emperatriz","El Mago","El Hermitaño"]
    carta=tarot[random.randint(0,len(tarot)-1)]
    return 'Tu destino esta en manos de '+carta+'.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=bind_port)
