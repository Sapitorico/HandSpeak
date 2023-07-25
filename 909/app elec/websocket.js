let socket = new WebSocket('ws://127.0.0.1:8000');
let reconnectionAttempts = 0;
const maxReconnectionAttempts = 3;

function connectWebSocket() {
  // Solución: Mantén la misma instancia de WebSocket y restablécela en caso de desconexión.
  socket = new WebSocket('ws://127.0.0.1:8000');
  socket.onopen = function() {
    console.log('WebSocket connection established');
    reconnectionAttempts = 0; // Reinicia el contador de intentos de reconexión al conectarse exitosamente.
  };

  socket.onmessage = function(event) {
    const message = event.data;
    // El mensaje es lo que devuelve el modelo.
    console.log(message);
    document.getElementById("letter").innerHTML = message;
  };

  socket.onclose = function() {
    console.log('WebSocket connection closed');
    if (reconnectionAttempts < maxReconnectionAttempts) {
      reconnectionAttempts++;
      setTimeout(connectWebSocket, 2000); // Intenta reconectar después de un intervalo de tiempo (2 segundos en este ejemplo).
    } else {
      console.log('Exceeded maximum reconnection attempts');
    }
  };
}

function sendImages(imageData) {
  if (socket.readyState === WebSocket.OPEN) {
    let hand = document.querySelectorAll('input[name="options"]');
    if (hand[0].checked) {
      hand = "Right";
    } else {
      hand = "Left";
    }
    let model = document.querySelectorAll('input[name="model"]');
    if (model[0].checked) {
      model = "Letter";
    } else {
      model = "Number";
    }
    socket.send(JSON.stringify([imageData, hand, model]));
  } else {
    connectWebSocket();
  }
}

connectWebSocket(); // Inicia la conexión WebSocket al cargar la página o ejecutar el script.


// let socket = new WebSocket('ws://127.0.0.1:8000')
//
// function sendImages(imageData) {
//   // Envia las imágenes al servidor
//   if (socket.readyState === WebSocket.OPEN) {
//     //console.log('enviando imagen...');
//     let hand = document.querySelectorAll('input[name="options"]')
//     if (hand[0].checked) {
//       hand = "Right"
//     } else hand = "Left"
//     let model = document.querySelectorAll('input[name="model"]')
//     if (model[0].checked) {
//       model = "Letter"
//     } else model = "Number"
//     socket.send(JSON.stringify([imageData, hand, model]));
//   } else {
//     // Problema: Intenta crear una nueva instancia de WebSocket dentro del bloque 'else',
//     // lo que hace que se pierdan los eventos y propiedades asociados a la instancia anterior.
//     socket = new WebSocket('ws://127.0.0.1:8000');
//     socket.onopen = function() {
//       console.log('webSocket connection established');
//     };
//   };
//
//   socket.onmessage = function(event) {
//     const message = event.data;
//     //message es lo que devuelve el modelo
//     console.log(message);
//     document.getElementById("letter").innerHTML = message;
//   }
//
//   socket.onclose = function() {
//     console.log('WebSocket connection closed');
//   };
// }