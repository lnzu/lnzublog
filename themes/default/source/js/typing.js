let divTyping = document.getElementById('discription');
let ii = 0,
  timer = 0,
  str = $("#discription").text();

function typing () {
  if (ii <= str.length) {
    divTyping.innerHTML = str.slice(0, ii++) + '_';
    timer = setTimeout(typing, 100);
  }
  else {
    divTyping.innerHTML = str//结束打字,移除 _ 光标
    clearTimeout(timer);
  }
}
typing();