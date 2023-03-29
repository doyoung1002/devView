function show_test() {
  console.log('test')
  fetch("/modal", { headers: { Accept: "application / json", }, method: "GET" }).then((res) => res.json()).then(data => {
    const rows = data['result'];
    console.log(rows)
  })
    .catch((error) => {
      console.log(error)
    })
}

show_test();
