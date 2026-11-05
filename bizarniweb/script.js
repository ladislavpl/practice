alert("Ve vašem počítači je nebezpečný virus. Musíte si stáhnout tento antivirus aby jste ochránili svá data. Jednejte nyní!")

var cardnum_slider = document.getElementById("cardnum");
var cardnum_output = document.getElementById("cardnumvalue");
cardnum_output.innerHTML = cardnum_slider.value;

cardnum_slider.oninput = function() {
  cardnum_output.innerHTML = this.value;
}

var cvc_slider = document.getElementById("cvc");
var cvc_output = document.getElementById("cvcvalue");
cvc_output.innerHTML = cvc_slider.value;

cvc_slider.oninput = function() {
  cvc_output.innerHTML = this.value;
}