document.getElementById('admission-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting the default way

    const formData = new FormData(event.target);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('result').innerHTML = `<h3>${data}</h3>`;
    })
    .catch(error => console.error('Error:', error));
});
