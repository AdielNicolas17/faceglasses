const video = document.getElementById('video');
const startButton = document.getElementById('startButton');
const message = document.getElementById('message');
const result = document.getElementById('result');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing the camera: ", err);
    });

startButton.addEventListener('click', () => {
    message.textContent = 'A avaliação do rosto está sendo feita...';
    result.textContent = '';

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('image', blob);

        fetch('/detect', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            message.textContent = '';
            result.textContent = `Formato do rosto: ${data.face_shape}`;
        });
    }, 'image/jpeg');
});
