from flask import Flask, render_template, request
from google.genai import Client
from google.genai import types
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = Client(api_key=gemini_api_key)

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp", "bmp", "tiff", "svg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def summarize_image(file_path, mime_type="image/jpeg"):
    with open(file_path, "rb") as f:
        image_bytes = f.read()

    # Use the correct Part.from_bytes for image + text prompt
    contents = [
        types.Part.from_bytes(data=image_bytes, mime_type=mime_type),
        "Describe this image in detail, including all visible objects, text, and layout. Keep it easy to understand."
    ]

    response = client.models.generate_content(
        model="gemini-2.5-flash",  # or whichever Gemini model you want
        contents=contents
    )

    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    uploaded_image = ""
    if request.method == "POST":
        file = request.files.get("file")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join("static", filename)
            file.save(filepath)
            uploaded_image = filename

            try:
                # Attempt to detect mime-type from extension (basic approach)
                ext = filename.rsplit(".", 1)[1].lower()
                mime = f"image/{'jpeg' if ext in ['jpg','jpeg'] else ext}"
                summary = summarize_image(filepath, mime_type=mime)
            except Exception as e:
                summary = f"Error summarizing image: {e}"
        else:
            summary = "Unsupported file type. Please upload a valid image."
    return render_template("index.html", summary=summary, uploaded_image=uploaded_image)

if __name__ == "__main__":
    app.run(debug=True)