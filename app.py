# config.json
import json
with open("config.json", "r", encoding="utf-8") as f:
   config = json.load(f)

#pymongo
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient(config["dbUrl"],  tlsCAFile=ca)
db = client.dbView

# flask
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 메인화면 (한솔)
@app.route('/')
def home():
   return render_template('index.html')

# 상세페이지
@app.route('/page')
def page():
  return render_template('page.html')

# 상세페이지 - 리스트 조회 (도영)
@app.route("/modal", methods=["GET"])
def value_get():
  test_data = list(db.board.find({}, {'_id': False}))
  return jsonify({'result': test_data})

# 상세페이지 - 키워드검색 (유리)
@app.route("/search", methods=["POST"])
def search():
  # POST 요청으로부터 검색어를 가져옴
  keyword = request.json['keyword']
  # MongoDB에서 검색
  result = db.board.find({'videoname': {'$regex': keyword}})
  # 검색 결과를 리스트로 변환
  data = []
  for doc in result:
    data.append({
      'videoname': doc['videoname'],
      'videodesc': doc['videodesc'],
      'videolink': doc['videolink'],
    })
  # 검색 결과를 JSON 형태로 반환
  return jsonify(data)

# 상세페이지 - 글 작성 (용식)
@app.route('/modal', methods=['POST'])
def modal_post():
   videoname_receive = request.form['videoname_give']
   videodesc_receive = request.form['videodesc_give']
   videolink_receive = request.form['videolink_give']
   board_receive = request.form['id_give']
   url_receive = request.form['url_give']
   doc = {
      'boardId'   : board_receive,
      'videoname' : videoname_receive,
      'videodesc' : videodesc_receive,
      'videolink' : videolink_receive,
      'url'       : url_receive,
   }
   db.board.insert_one(doc)
   return jsonify({'msg': '저장완료'})
   
# flask port
if __name__ == '__main__':  
	 # 5000포트 사용 중이라고 뜨면 포트 번호를 5001로 변경!
   app.run('0.0.0.0',port=5001,debug=True)