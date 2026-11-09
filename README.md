# IoTUS-BOT
Bot de IoTUS para el servidor de Discord, hecho con [Pycord](https://pycord.dev).
Todos los comandos funcionan con prefijo `$` y como comandos `/`.

## Estructura

```
main.py            # Arranque del bot y carga automática de cogs
config.py          # Configuración (lee el .env)
.env               # Token y secretos (NO se sube al repositorio)
.env.example       # Plantilla del .env
cogs/
├── utilidades/    # help, embed
├── juego/         # dado
└── administracion/# limpiar
```

Para añadir un comando: crea un archivo `.py` dentro de la carpeta de su categoría
(o crea una carpeta nueva con su `__init__.py`) con una función `setup(bot)`. Se carga solo.

## Crear el bot e invitarlo al servidor

1. Entra en el [Discord Developer Portal](https://discord.com/developers/applications) e inicia sesión.
2. **New Application** → ponle nombre → **Create**.
3. En el menú **Bot**:
   - Pulsa **Reset Token** y copia el token (solo se muestra una vez).
   - Activa **Message Content Intent** en *Privileged Gateway Intents* (necesario para el prefijo `$`).
4. En **OAuth2 → URL Generator**:
   - *Scopes*: `bot` y `applications.commands`.
   - *Bot Permissions*: `Send Messages`, `Embed Links`, `Read Message History`, `Manage Messages`
     (o `Administrator` si es solo para pruebas).
5. Copia la URL generada, ábrela en el navegador, elige tu servidor y pulsa **Autorizar**.

## Instalación y ejecución

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # y pega tu token en DISCORD_TOKEN
python main.py
```

En `.env` puedes poner `GUILD_IDS` (ID de tu servidor; clic derecho en el servidor → *Copiar ID*,
con el modo desarrollador activo) para que los comandos `/` aparezcan al instante.
Sin él, Discord puede tardar hasta una hora en mostrarlos globalmente.

> ⚠️ Nunca compartas el token ni subas el `.env`. Si se filtra, resetéalo en el Developer Portal.

## Comandos

| Categoría | Comando | Descripción |
|---|---|---|
| Utilidades | `$help` · `/help` | Lista de comandos |
| Utilidades | `$embed "título" "texto" [#color] [#canal]` · `/embed` | Envía un embed (requiere *Gestionar mensajes*) |
| Juego | `$dado [caras]` · `/dado` | Tira un dado |
| Administración | `$limpiar <n>` · `/limpiar` | Borra mensajes (requiere *Gestionar mensajes*) |
