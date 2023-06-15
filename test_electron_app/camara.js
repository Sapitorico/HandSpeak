const imgContainer = document.getElementById('imagen-container');
const clsValueElement = document.getElementById('cls-value');
const cuadros = document.getElementsByClassName('cuadro');
let socket;
let isConnected = false;

function toggleConnection() {
  if (isConnected) {
    disconnectWebSocket();
  } else {
    connectWebSocket();
  }
}

function connectWebSocket() {
  if (isConnected) {
    console.log('Ya hay una conexión WebSocket abierta.');
    return;
  }

  socket = new WebSocket('ws://127.0.0.1:8000/ws');

  socket.onopen = function () {
    console.log('Conexión establecida');
    isConnected = true;
    document.getElementById('connect-btn').disabled = true;
    document.getElementById('disconnect-btn').disabled = false;
  };

  socket.onmessage = function (event) {
    const data = JSON.parse(event.data);

    if (data.image) {
      const imageBase64 = data.image;

      // Crear una nueva imagen en memoria
      const newImg = new Image();
      newImg.onload = function () {
        // Reemplazar la imagen anterior con la nueva
        imgContainer.innerHTML = '';
        imgContainer.appendChild(newImg);
      };
      newImg.src = 'data:image/jpeg;base64,' + imageBase64;
    }

    if (data.cls) {
      const clsValue = data.cls;
      clsValueElement.textContent = 'Valor de cls: ' + clsValue;

      for (let i = 0; i < cuadros.length; i++) {
        cuadros[i].classList.remove('verde');
      }

      const cuadroIndex = clsValue.charCodeAt(0) - 65;
      if (cuadroIndex >= 0 && cuadroIndex < cuadros.length) {
        cuadros[cuadroIndex].classList.add('verde');
      }
    }
  };

  socket.onclose = function (event) {
    console.log('Conexión cerrada: ', event);
    isConnected = false;
    document.getElementById('connect-btn').disabled = false;
    document.getElementById('disconnect-btn').disabled = true;
    resetImage();
  };
}

function disconnectWebSocket() {
  if (socket) {
    socket.close();
    console.log('Conexión WebSocket cerrada');
  }
}

function resetImage() {
  imgContainer.innerHTML = '';
}