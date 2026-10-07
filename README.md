# Beta Paletas - Página web

Esta página está hecha con Python + Flask y contiene:
- Logo de Beta Paletas
- Presentación con estilo artesanal
- Sabores de agua
- Sabores de leche
- Sabores especiales
- Botones directos a WhatsApp, Instagram y Facebook
- Diseño adaptable para celular, tablet y computadora

## Probarla en tu computadora

1. Instala Python.
2. Abre una terminal dentro de esta carpeta.
3. Ejecuta:

    pip install -r requirements.txt

4. Después:

    python app.py

5. Abre en el navegador:

    http://127.0.0.1:5000

## Subirla a internet con Render

El proyecto ya incluye `render.yaml`.

La forma sencilla es:
1. Crear una cuenta de GitHub.
2. Crear un repositorio nuevo llamado `beta-paletas`.
3. Subir todos los archivos de esta carpeta al repositorio.
4. Entrar a Render y conectar GitHub.
5. Crear un Web Service usando el repositorio `beta-paletas`.
6. Si Render no toma automáticamente el archivo `render.yaml`, usar:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
7. Al terminar el deploy Render dará una dirección pública `onrender.com`.

## Importante

El número, Instagram y Facebook ya están colocados en la página. Si después quieren
agregar precios, dirección, horarios, fotografías de las paletas, pedidos en línea
o un dominio propio, se pueden agregar al mismo proyecto.
