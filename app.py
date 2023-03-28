# config.json
import json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

#pymongo
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient(config["dbUrl"],  tlsCAFile=ca)
db = client.dbTest



# flask
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/modal', methods=['POST'])
def modal_post():
   videoname_receive = request.form['videoname_give']
   videodesc_receive = request.form['videodesc_give']
   videolink_receive = request.form['videolink_give']

   doc = {
      'videoname' :  videoname_receive,
      'videodesc' : videodesc_receive,
      'videolink' :   videolink_receive
   }
   db.value.insert_one(doc)
   print(doc)
   return jsonify({'msg': '저장완료'})



# flask port
if __name__ == '__main__':  
	 # 5000포트 사용 중이라고 뜨면 포트 번호를 5001로 변경!
   app.run('0.0.0.0',port=5000,debug=True)