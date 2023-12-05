from flask import Flask,render_template,request
import base64
from PIL import Image
from ultralytics import YOLO
import os
#from pdf2image import convert_from_bytes
#from pdf2image import convert_from_path

app=Flask(__name__)

model = YOLO("best.pt")

UPLOAD_FOLDER = 'pdfs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded image file
        file = request.files['file']
        print(is_image(file))
        print(is_image(file)==1)
        if is_image(file)==1:   
            image = Image.open(file)
        else:
           print(file)
           filename = file.filename
           # Saving the file
           file.save('pdfs/' + filename)
           #image=convert_from_path('pdfs/' + filename)

        os.makedirs('cvs', exist_ok=True)
        image_path = os.path.join('cvs', 'tmp.jpg')
        image.save(image_path)
        with open(image_path, 'rb') as file:
            img_data = file.read()
            img_in = base64.b64encode(img_data).decode('utf-8')

        # Process the image (perform YOLO prediction, etc.)
        model.predict(image_path,save= True, save_txt=True)

        directory_path = 'runs\\detect'
        count = len(os.listdir(directory_path))
        if count==1:
            i=''
        else:
            i=str(count)
        # Example: Convert the image to base64 for display
        with open("runs\\detect\\predict"+i+"\\tmp.jpg", 'rb') as file:
            img_data = file.read()
            img_out = base64.b64encode(img_data).decode('utf-8')

        # Return the result to the template
        return render_template('home.html', imgs=[img_in,img_out])

    return render_template('home.html')

#def convert_pdf_to_images(pdf_content):
#    # Convert PDF bytes to images
#    image = convert_from_bytes(pdf_content)

#    return image

def is_image(file_storage):
    try:
        # Read the content of the file
        test=Image.open(file_storage)
        return 1
    except Exception as e:
        # Failed to open the content as an image
        return 0
    

if __name__ == '__main__':
    app.run(debug=True)