from assets import *
from admin_panel import *
import os
import subprocess
import tabula
from tika import parser
from PIL import Image
import io
from pathlib import Path
import fitz # PyMuPDF
from flask import Flask, jsonify, request, render_template,  send_from_directory
from werkzeug.utils import secure_filename
from pdf2image import convert_from_path
import shutil
from typing import Tuple
import sys

app = Flask(__name__)

app.register_blueprint(admin_panel)
app.register_blueprint(assets)

app.config['UPLOAD_FOLDER'] = "/var/www/html/flask_pdf_cloned/PDF/"
# allow both GET and POST requests

@app.route('/pdf-word', methods=['GET', 'POST'])
def form_word():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system('unoconv -f doc /var/www/html/flask_pdf_cloned/PDF/'+filename)
        filename_docx = filename.split('.PDF')[0]
        filename_docx = filename_docx.split('.pdf')[0]
        print(filename_docx)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_docx+'.doc')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/word-pdf', methods=['GET', 'POST'])
def form_to_word():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system('unoconv -f pdf /var/www/html/flask_pdf_cloned/PDF/'+filename)
        filename_m = Path(filename).stem
        print(filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_m+'.pdf')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/ppt-pdf', methods=['GET', 'POST'])
def form_to_ppt():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system('unoconv -f pdf /var/www/html/flask_pdf_cloned/PDF/'+filename)
        filename_m = Path(filename).stem
        print(filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_m+'.pdf')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/excel-pdf', methods=['GET', 'POST'])
def form_to_excel():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system('unoconv -f pdf /var/www/html/flask_pdf_cloned/PDF/'+filename)
        filename_m = Path(filename).stem
        print(filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_m+'.pdf')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/jpg-pdf', methods=['GET', 'POST'])
def form_to_jpg():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system('unoconv -f pdf /var/www/html/flask_pdf_cloned/PDF/'+filename)
        filename_m = Path(filename).stem
        print(filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_m+'.pdf')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/png-pdf', methods=['GET', 'POST'])
def form_to_png():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system('unoconv -f pdf /var/www/html/flask_pdf_cloned/PDF/'+filename)
        filename_m = Path(filename).stem
        print(filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_m+'.pdf')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/tiff-pdf', methods=['GET', 'POST'])
def form_to_tiff():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system('unoconv -f pdf /var/www/html/flask_pdf_cloned/PDF/'+filename)
        filename_m = Path(filename).stem
        print(filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_m+'.pdf')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/txt-pdf', methods=['GET', 'POST'])
def form_to_txt():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.system('unoconv -f pdf /var/www/html/flask_pdf_cloned/PDF/'+filename)
        filename_m = Path(filename).stem
        print(filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_m+'.pdf')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/pdf-txt', methods=['GET', 'POST'])
def form_txt():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_data = parser.from_file("/var/www/html/flask_pdf_cloned/PDF/"+filename)
        output = file_data['content']
        os.mkdir('/var/www/html/flask_pdf_cloned/PDF/txt_and_images'+filename)
        with open('/var/www/html/flask_pdf_cloned/PDF/txt_and_images'+filename+'/'+filename+'.txt', 'w') as the_file:
           the_file.write(str(output))
        # Leer PDF
        pdf_leido = fitz.open('/var/www/html/flask_pdf_cloned/PDF/'+filename)
         
        # Procesar pagina por pagina
         
        for indice in range(len(pdf_leido)):
         
            # Obtener pagina
            pagina = pdf_leido[indice]
         
            # Obtener lista de imagenes en la pagina
            lista_imagenes = pagina.get_images()
         
            # Revisamos si tiene imagenes
            if lista_imagenes:
                print("la pagina numero " + str(indice + 1) + " tiene " + str(len(lista_imagenes)) + " imagenes")
            else:
                print("la pagina numero " + str(indice + 1) + " no tiene imagenes")
         
            # Procesamos imagen por imagen
            numero_imagen = 0
            for imagen in lista_imagenes:
         
                numero_imagen = numero_imagen + 1
         
                imagen_base = pdf_leido.extract_image(imagen[0])
                 
                data_imagen = imagen_base["image"]
                 
                # Extension de la imagen
                extension_imagen = imagen_base['ext']
                 
                imagen_objeto = Image.open(io.BytesIO(data_imagen))
         
                # Guardamos la Imagen
                imagen_objeto.save(open("/var/www/html/flask_pdf_cloned/PDF/txt_and_images"+filename+"/imagen_" + str(numero_imagen) + "_hoja_" + str(indice + 1) + "." + extension_imagen, "wb"))
        archivo_zip = shutil.make_archive("/var/www/html/flask_pdf_cloned/PDF/"+filename, "zip", "/var/www/html/flask_pdf_cloned/PDF/txt_and_images"+filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename+'.zip')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/pdf-excel', methods=['GET', 'POST'])
def form_excel():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        df = tabula.read_pdf('/var/www/html/flask_pdf_cloned/PDF/'+filename, pages='all')
        # convert PDF into CSV
        filename_csv = filename.split('.PDF')[0]
        filename_csv = filename_csv.split('.pdf')[0]
        tabula.convert_into('/var/www/html/flask_pdf_cloned/PDF/'+filename, '/var/www/html/flask_pdf_cloned/PDF/'+filename_csv+'.csv', output_format="csv", pages='all')
        print(filename_csv)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_csv+'.csv')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/pdf-ppt', methods=['GET', 'POST'])
def form_ppt():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filename_ppt = filename.split('.PDF')[0]
        filename_ppt = filename_ppt.split('.pdf')[0]
        list_files = subprocess.run(["pdf2pptx", '/var/www/html/flask_pdf_cloned/PDF/'+filename])
        print(filename_ppt)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename_ppt+'.pptx')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/pdf-jpg', methods=['GET', 'POST'])
def form_jpg():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.mkdir('PDF/'+ filename+'.images')
        pages = convert_from_path('/var/www/html/flask_pdf_cloned/PDF/'+filename)
        for i in range(len(pages)):
          # save pdf as jpg
          pages[i].save('PDF/'+filename+'.images/page'+ str(i) +'.jpg', 'JPEG')
        archivo_zip = shutil.make_archive("PDF/"+filename, "zip", "PDF/"+filename+'.images/')
        print(filename+'.zip')
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename+'.zip')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/pdf-png', methods=['GET', 'POST'])
def form_png():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.mkdir('PDF/'+ filename+'.images')
        pages = convert_from_path('/var/www/html/flask_pdf_cloned/PDF/'+filename)
        for i in range(len(pages)):
          # save pdf as jpg
          pages[i].save('PDF/'+filename+'.images/page'+ str(i) +'.png', 'PNG')
        archivo_zip = shutil.make_archive("PDF/"+filename, "zip", "PDF/"+filename+'.images/')
        print(filename+'.zip')
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename+'.zip')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/pdf-tiff', methods=['GET', 'POST'])
def form_tiff():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.mkdir('PDF/'+ filename+'.images')
        pages = convert_from_path('/var/www/html/flask_pdf_cloned/PDF/'+filename)
        for i in range(len(pages)):
          # save pdf as jpg
          pages[i].save('PDF/'+filename+'.images/page'+ str(i) +'.tiff', 'TIFF')
        archivo_zip = shutil.make_archive("PDF/"+filename, "zip", "PDF/"+filename+'.images/')
        print(filename+'.zip')
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename+'.zip')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/pdf-zip', methods=['GET', 'POST'])
def form_zip():
    # handle the POST request
    if request.method == 'POST':
        os.system('rm -rf /var/www/html/flask_pdf_cloned/PDF/*')
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        os.mkdir('/var/www/html/flask_pdf_cloned/PDF/'+filename+'_zip')
        shutil.move('/var/www/html/flask_pdf_cloned/PDF/'+filename, '/var/www/html/flask_pdf_cloned/PDF/'+filename+'_zip')
        archivo_zip = shutil.make_archive("/var/www/html/flask_pdf_cloned/PDF/"+filename, "zip", "/var/www/html/flask_pdf_cloned/PDF/"+filename+'_zip')
        print(archivo_zip)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename+'.zip')
    # otherwise handle the GET request
    return render_template('form.html')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
    
if __name__=="__main__":
    app.run(debug=True)
