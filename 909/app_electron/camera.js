
function openCamera() {
    const video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({ video: true })
      .then((stream) => {
        video.srcObject = stream;
        video.play();
        video.style.transform = 'scaleX(-1)'
        obtainfps(video)
      })
      .catch((error) => {
        console.log('Error accessing webcam: ' + error.toString());
      });
};
let intervalId;

function obtainfps(video) {
  intervalId = setInterval(() => {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d')
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageData = canvas.toDataURL('image/jpeg');
    sendImages(imageData)
  }, 200);
}

function closeCamera() {
  video.pause();
  video.srcObject.getTracks().forEach((track) => {
    track.stop();});
  video.srcObject = null;
  clearInterval(intervalId)
  //location.reload()
}
