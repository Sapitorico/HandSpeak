let socket = new WebSocket('ws://127.0.0.1:8000')

function sendImages(imageData) {
  //envia las imagenes la server
  if (socket.readyState === WebSocket.OPEN) {
    //console.log('enviando imagen...');
    socket.send(imageData);
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