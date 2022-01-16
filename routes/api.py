import aiofiles

from quart import Blueprint, jsonify, request
from codecs import decode, encode

api = Blueprint("api", __name__)


@api.route("/api/update", methods=["POST"])
async def api_update():
    request_body = await request.json

    if not request_body:
        return jsonify({"error": "parameter 'json' is unfilled"})

    new_code = request_body.get("newCode")
    new_code = encode(new_code.encode(), "base-64")

    async with aiofiles.open("./static/temporaryCode.txt", "w") as w:
        await w.write(new_code.decode())

    return jsonify({"success": "Successfully uploaded new code!"})


@api.route("/api/code")
async def api_code():
    async with aiofiles.open("./static/temporaryCode.txt", "r") as r:
        content = await r.read()

    content = decode(bytes(content.encode()), "base-64")

    return jsonify({"code": content.decode()})
