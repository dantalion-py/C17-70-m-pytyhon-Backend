import os
from dotenv import load_dotenv

load_dotenv()

print(f"Nombre de la base de datos: {os.getenv('RAILWAY_DATABASE_NAME')}")
print(f"Usuario de la base de datos: {os.getenv('RAILWAY_DATABASE_USERNAME')}")
# No imprimas la contraseña por seguridad
# print(f"Contraseña de la base de datos: {os.getenv('RAILWAY_DATABASE_PASSWORD')}")
print(f"Host de la base de datos: {os.getenv('RAILWAY_DATABASE_HOST')}")
print(f"Puerto de la base de datos: {os.getenv('RAILWAY_DATABASE_PORT')}")
