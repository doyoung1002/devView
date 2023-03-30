window.onload = () => {
  show_list();
  navbar_active();
}

// 전체 리스트
function show_list() {
  fetch("/modal", { headers: { Accept: "application / json", }, method: "GET" })
  .then((res) => res.json())
  .then(data => {
    const rows = data['result'];
    append_list(rows);
  })
  .catch((error) => {
    console.log(error)
  })
}

// 키워드 검색
document.querySelector('#searchIcon').addEventListener('click', async () => {
  // 검색어를 가져옴
  const keyword = document.querySelector('input[name="keyword"]').value;

  // 검색어를 서버로 전송하는 POST 요청
  const response = await fetch('/search', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ keyword }),
  });

  // 서버에서 받은 응답을 JSON 형태로 파싱
  const data = await response.json();

  if(data.length === 0) {
    alert('일치하는 추천영상이 없습니다!')
  } else {
    append_list(data);
  }
});

// 리스트 보여주기
function append_list(rows) {
  const element = document.querySelector('.list');
  element.replaceChildren();

  rows.forEach((element) => {
    const videolink = element['videolink'];
    const thumbnail = videolink.slice(-11);

    const temp_html = `
      <div class="item">
        <div class="itemImage">
          <a href="${videolink}" target="_blank">
            <img src="https://i1.ytimg.com/vi/${thumbnail}/sddefault.jpg" alt="">
          </a>
        </div>
        <div class="itemList">
          <div class="item__desc">
            <h1>${element['videoname']}</h1>
            <p>${element['videodesc']}</p>
          </div>
          <!-- 댓글 들어가는 영역 -->
          <div class="item__comment">
            <!-- 여기에 댓글 html 작성 -->
          </div>
        </div>
      </div>
    `;
    document.querySelector('.list').insertAdjacentHTML('beforeend', temp_html);
  })
}

// navbar JavaScript active
function navbar_active() {
  document.querySelector('.navbar__menu li:nth-child(2)').classList.add('active');
}