function generarContraseña() {
    let longitud = document.getElementById("longitud").value;

    fetch("/generar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ longitud: longitud })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("resultado").innerText = "Contraseña generada: " + data.contraseña;
    })
    .catch(error => console.error("Error:", error));
}
