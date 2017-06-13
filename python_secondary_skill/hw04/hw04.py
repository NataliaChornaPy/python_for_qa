import os, time, os.path
from flask import Flask, request, url_for, render_template,redirect,send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image

extensions=['jpg','jpeg']


def check_file_extension(filename,extensions):

        for extension in extensions:
            if filename.endswith(extension.upper()):
                return True
        return False


def BlackWhite_foto(img):
    if img.mode <> 'L':
        converted = img.convert('L')
        print time.strftime("%c"), '-- photo is black/white now'
        return converted
    else:
        return img


def landscape_orient(image):
    width, height = image.size
    if height > width:
        rotated_img = image.rotate(90.0)
        print time.strftime("%c"), '-- photo is rotated'
        return rotated_img
    else:
        return image


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'D:\photo2\\'
directory = os.path.dirname(app.config['UPLOAD_FOLDER'])
if not os.path.exists(directory):
        os.makedirs(directory)


@app.route ( '/' )
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    file = request.files['path']
    filename = secure_filename(file.filename)
    if check_file_extension(file.filename,extensions):
        img = Image.open(file)
        file = BlackWhite_foto(img) # convert to black/white
        changed_file = landscape_orient(file)  # rotate
        changed_file.save (os. path. join(app.config['UPLOAD_FOLDER'], filename)) # save photo
        return redirect(url_for('uploaded_file',
                            filename=filename,as_attachment=True))
    else:
        return render_template('selected.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(debug=True)
