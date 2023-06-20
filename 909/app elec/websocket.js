let socket = new WebSocket('ws://127.0.0.1:8000')

function sendImages(imageData) {
  //envia las imagenes la server
  if (socket.readyState === WebSocket.OPEN) {
    //console.log('enviando imagen...');
    let hand = document.querySelectorAll('input[name="options"]')
    if (hand[0].checked) {
      hand = "Right"
    } else hand = "Left"
    let model = document.querySelectorAll('input[name="model"]')
    if (model[0].checked) {
      model = "Letter"
     } else model = "Number"
    socket.send(JSON.stringify([imageData, hand, model]));
  } else {
    socket = new WebSocket('ws://127.0.0.1:8000');
    socket.onopen = function() {
      console.log('webSocket connection established');
    };
  };


  socket.onmessage = function(event) {
    const message = event.data;
  //message es lo que devuelve el modelo
    console.log(message);
    document.getElementById("letter").innerHTML = message;
    
}

  socket.onclose = function() {
    
    console.log('WebSocket connection closed');
  };

}