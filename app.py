# config.json
import json
with open("config.json", "r", encoding="utf-8") as f:
  config = json.load(f)

# pymongo
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient(config["dbUrl"], tlsCAFile=ca)
db = client.dbTest

# flask
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('page.html')

@app.route("/modal", methods=["GET"])
def value_get():
  test_data = list(db.value.find({}, {'_id': False}))
  print("adfadsfasdfasdfadfasdf")
  return jsonify({'result': test_data})


# flask port
if __name__ == '__main__':  
  # 5000포트 사용 중이라고 뜨면 포트 번호를 5001로 변경!
  app.run('0.0.0.0',port=5002,debug=True)


