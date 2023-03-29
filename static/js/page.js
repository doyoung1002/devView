function show_test() {
  console.log('test')
  fetch("/modal", { headers: { Accept: "application / json", }, method: "GET" }).then((res) => res.json()).then(data => {
    const rows = data['result'];
    rows.forEach((element) => {
      // commentId, videoname, videodesc, videolink
      const temp_html = `
        <section class="list">
          <div class="item">
            <a href="${element['videolink']}">
              <img src="../static/images/test.png" alt="">
            </a>
          </div>
          <div class="container">
            <article>
              <h1>${element['videoname']}</h1>
              <p>${element['videodesc']}</p>
            </article>
          </div>
        </section>
      `;

      

      document.querySelector('.container').insertAdjacentHTML('beforeend', temp_html);
    })
  })
  .catch((error) => {
    console.log(error)
  })
}

show_test();
