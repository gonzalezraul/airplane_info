const express = require('express');
const app = express();

// Ruta principal
app.get('/', (req, res) => {
    res.send('¡Hola, mundo desde Node.js!');
});

// Iniciar el servidor
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
