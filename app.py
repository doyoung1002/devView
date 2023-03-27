# config.json
import json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# pymongo
from pymongo import MongoClient
client = MongoClient(config["dbUrl"])
db = client.dbView

# flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

# flask port
if __name__ == '__main__':  
	 # 5000포트 사용 중이라고 뜨면 포트 번호를 5001로 변경!
   app.run('0.0.0.0',port=5000,debug=True)