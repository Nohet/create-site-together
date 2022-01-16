from quart import Quart

from routes.api import api
from routes.index import index


app = Quart(__name__)

app.register_blueprint(api)
app.register_blueprint(index)


# if __name__ == "__main__":
#    app.run()
# hypercorn --bind "ip:port" base:app