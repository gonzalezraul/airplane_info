const express = require('express');
const app = express();

// Ruta principal
app.get('/', (req, res) => {
    res.send('¡Hola, mundo desde Node.js!');
});

app.get('/añadir_info', (req, res) => {
    res.send();
});

// Iniciar el servidor
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
