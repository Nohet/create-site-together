from quart import Blueprint, render_template

index = Blueprint("index", __name__)


@index.route("/")
async def index_route():
    return await render_template("index.html")
