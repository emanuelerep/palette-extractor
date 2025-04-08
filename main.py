from flask import Flask, request, jsonify
from PIL import Image
from colorthief import ColorThief
import io

app = Flask(__name__)

@app.route("/api/palette", methods=["POST"])
def get_palette():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    img_bytes = image.read()
    color_thief = ColorThief(io.BytesIO(img_bytes))
    palette = color_thief.get_palette(color_count=5)
    hex_palette = ['#%02x%02x%02x' % rgb for rgb in palette]

    return jsonify({"palette": hex_palette})