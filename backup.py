import os
from dotenv import load_dotenv

load_dotenv()

# Configuración desde variables de entorno
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', '5432')  # Puerto por defecto
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')  # Importante para autenticación

# Nombre del archivo de backup con timestamp
backup_file = f"backup_{os.popen('date +%Y%m%d%H%M%S').read().strip()}.sql"

# Comando con parámetros esenciales
command = (
    f"PGPASSWORD={DB_PASSWORD} pg_dump "
    f"-h {DB_HOST} "
    f"-p {DB_PORT} "
    f"-U {DB_USER} "
    f"-d {DB_NAME} "
    f"-F c "  # Formato custom (permite restauración selectiva)
    f"-v "    # Modo verbose
    f"-f {backup_file}"
)

# Ejecutar el comando
try:
    exit_code = os.system(command)
    if exit_code == 0:
        print(f"Backup exitoso: {backup_file}")
        print(f"Tamaño: {os.path.getsize(backup_file)/1024/1024:.2f} MB")
    else:
        print(f"Error en el backup (Código: {exit_code})")
except Exception as e:
    print(f"Error inesperado: {str(e)}")