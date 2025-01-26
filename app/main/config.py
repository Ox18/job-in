import environ
import os

# Inicializar entorno
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()

env_file = os.path.join(BASE_DIR, '../app', 'config', '.env')
if os.path.exists(env_file):
    environ.Env.read_env(env_file)

# Leer las variables de entorno
APP_NAME = env('APP_NAME', default=None)
DEBUG = env.bool('DEBUG', default=False)