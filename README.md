# Visual Summarizer

**Visual Summarizer** is a web application that allows students and staff to upload images and receive a detailed, easy-to-understand description of their contents. It supports multiple image formats, including JPEG, PNG, GIF, WebP, BMP, TIFF, and SVG. The app uses **Google Gemini** AI to analyze and summarize the images.

---

## Features

* Upload images in popular formats: `JPEG/JPG`, `PNG`, `GIF`, `WebP`, `BMP`, `TIFF`, `SVG`.
* Get a comprehensive description of all visible objects, text, and layout.
* Easy-to-use web interface with responsive design.
* Accessible design with keyboard-friendly navigation.
* Preview uploaded images alongside the generated summaries.

---

## Interface
<img width="994" height="751" alt="Burger" src="https://github.com/user-attachments/assets/f8f9ab04-3307-4e20-9677-788a0d692aa0" />


## Installation

1. **Clone or download the repository**:

```bash
git clone <your-repo-url>
cd visual_summarizer
```

2. **Create a virtual environment (recommended)**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the project root with your Gemini API key:

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Usage

1. **Run the app**:

```bash
python app.py
```

2. **Open your browser** and go to:

```
http://127.0.0.1:5000/
```

3. **Upload an image** using the "Choose image" button and click **Summarize Image**.

4. The app will display the uploaded image alongside its AI-generated summary.

---

## Supported Image Formats

* **JPEG / JPG** – Joint Photographic Experts Group
* **PNG** – Portable Network Graphics
* **GIF** – Graphics Interchange Format
* **WebP** – Modern format by Google
* **BMP** – Bitmap
* **TIFF** – Tag Image File Format
* **SVG** – Scalable Vector Graphics

---

## Technologies Used

* **Python 3.9+**
* **Flask** – Web framework
* **Google Gemini API** – AI model for content generation
* **Werkzeug** – Secure file handling
* **Dotenv** – Environment variable management
* **HTML, CSS** – Frontend layout and styling

---

## Project Structure

```
visual_summarizer/
├─ app.py
├─ requirements.txt
├─ templates/
│  └─ index.html
├─ static/
│  └─ style.css
└─ .env
```

---

## Notes

* Make sure your **Gemini API key** is valid and has the necessary permissions for image summarization.
* For large images, the summary may take a few seconds depending on the model's processing time.
* Only the listed formats are supported. Other file types will be rejected.
