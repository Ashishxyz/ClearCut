#JAI SHRI RAM || JAI HANUMAN

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from u2net_utils import load_model, remove_background

# Initialize Flask app
app = Flask(__name__)

# Directory setup
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = os.path.join(UPLOAD_FOLDER, 'results')
os.makedirs(RESULT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load U²-Net model (once on app start)
model = load_model()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded file
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        
        # Save uploaded file
        if file.filename != "":
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            
            # Remove background using U²-Net
            result_path = remove_background(model, file_path)
            return render_template("index.html", result_image=url_for("uploaded_file", filename=os.path.join("results", os.path.basename(result_path))))

    return render_template("index.html", result_image=None)

@app.route("/uploads/results/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(RESULT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)