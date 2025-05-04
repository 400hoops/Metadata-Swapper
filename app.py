from flask import Flask, request, send_file, render_template, redirect, url_for, make_response
import os
import uuid

app = Flask(__name__)

# Ensure you have the secret key for cookie signing
app.secret_key = os.urandom(24)

# The rest of your app setup...

@app.route("/", methods=["GET", "POST"])
def index():
    dark_mode = request.cookies.get("dark_mode", "false") == "true"

    if request.method == "POST":
        source = request.files["source"]
        dest = request.files["destination"]

        source_path = os.path.join(UPLOAD_FOLDER, source.filename)
        dest_path = os.path.join(UPLOAD_FOLDER, dest.filename)

        source.save(source_path)
        dest.save(dest_path)

        dest_jpeg = convert_to_jpeg(dest_path)

        if source.filename.lower().endswith((".jpg", ".jpeg")):
            try:
                exif_data = piexif.load(Image.open(source_path).info.get("exif", b""))
                exif_bytes = piexif.dump(exif_data)
                img = Image.open(dest_jpeg).convert("RGB")
                final_path = os.path.join(UPLOAD_FOLDER, f"output_{uuid.uuid4()}.jpg")
                img.save(final_path, "jpeg", exif=exif_bytes)
            except Exception as e:
                return f"Error loading EXIF from source: {e}"
        else:
            final_path = os.path.join(UPLOAD_FOLDER, f"output_{uuid.uuid4()}.jpg")
            os.rename(dest_jpeg, final_path)
            copy_metadata_with_exiftool(source_path, final_path)

        log_metadata_swap(source_path, dest_path, final_path)

        response = make_response(render_template("success.html", file_path=final_path, dark_mode=dark_mode))

        # Save dark mode preference in cookies
        dark_mode_cookie = "true" if dark_mode else "false"
        response.set_cookie("dark_mode", dark_mode_cookie)

        return response

    return render_template("index.html", dark_mode=dark_mode)
