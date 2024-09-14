from flask import Flask, render_template, request,send_file
from flask import *
from flask import session
from i2p import i2pconverter
# from pytube import YouTube
# import re
import os
# from pathlib import Path

# Create a Flask instance
app = Flask(__name__)
app.secret_key = 'as;dlkfj;alskdjf;lasdjfpoiuweoriuwoeiurpoiweursdfsdjkfhkjsdhk'

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converted',methods = ['GET','POST'])
def convert():
    uploaded_file = request.files['img']
    if uploaded_file.filename != '':
        f1 = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(f1)
        i2pconverter(f1)
        
        # Store the file name in the session
        session['f1'] = f1
    return render_template('converted.html')


    # global f1
    # fi = request.files['img']
    # fi = fi.filename
    # fi.save(f1)
    # i2pconverter(f1)
    # return render_template('converted.html')


@app.route('/download')
def download():
    f1 = session.get('f1')  # Retrieve the file path from the session
    if f1:
        filename = f1.split('.')[0] + 'converted.pdf'
        if os.path.exists(filename):
            return send_file(filename, as_attachment=True)
        else:
            return "File not found", 404
    else:
        return "File not found in session", 404
















# @app.route('/', methods=['GET', 'POST'])  # this is the URL
# def index():
#     message = ''
#     errorType = 0
#     if request.method == 'POST' and 'video_url' in request.form:
#         youtubeUrl = request.form['video_url']
#         print('url: ', youtubeUrl)
        
#         if youtubeUrl:
#             # Regex pattern to validate YouTube URL
#             validateVideoUrl = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/' \
#                                r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
#             valid = re.match(validateVideoUrl, youtubeUrl)
            
#             if valid:
#                 try:
#                     url = YouTube(youtubeUrl)
#                     video = url.streams.get_highest_resolution()
                    
#                     # Download directory
#                     downloadFolder = os.path.join(Path.home(), "Downloads/Youtube_download")
#                     os.makedirs(downloadFolder, exist_ok=True)  # Ensure the directory exists
                    
#                     video.download(downloadFolder)
#                     message = 'Video downloaded successfully!'
#                     errorType = 1
#                 except Exception as e:
#                     message = f'An error occurred: {str(e)}'
#                     errorType = 0
#             else:
#                 message = 'Invalid YouTube video link'
#                 errorType = 0
#         else:
#             message = 'Please enter a YouTube video link'
#             errorType = 0

#     return render_template('index.html', message=message, errorType=errorType)




if __name__ =='__main__':

    app.run(debug=True)