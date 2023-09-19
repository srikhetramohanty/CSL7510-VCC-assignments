from flask import Flask, request, render_template
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

# Configure MySQL connection
DATABASE_URI = 'mysql+pymysql://root:password@192.168.29.15/assignment'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            data_frame = pd.read_csv(file)
            engine = create_engine(DATABASE_URI)
            data_frame.to_sql('data', con=engine, index=False, if_exists='append')
            return "File Uploaded and Data Inserted Successfully"
    return "Failed to Upload"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
