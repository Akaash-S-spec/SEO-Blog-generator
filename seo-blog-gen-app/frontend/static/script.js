// static/script.js

document.getElementById("generate-form").addEventListener("submit", function (e) {
    e.preventDefault();
    
    const keywords = document.getElementById("keywords").value.split(",").map(k => k.trim());
    fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ keywords }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerHTML = `<h2>Generated Blog:</h2><p>${data.content}</p>`;
    })
    .catch(err => {
        document.getElementById("output").innerHTML = `<p>Error: ${err.message}</p>`;
    });
});
