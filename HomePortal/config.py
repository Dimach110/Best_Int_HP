import os

PG_USER = os.getenv("PG_USER", 'BestInt')
PG_PASSWORD = os.getenv("PG_PASSWORD", 'user2psql')
PG_HOST = os.getenv("PG_HOST", '127.0.0.1')
PG_PORT = int(os.getenv("PG_PORT", 5431))
PG_DB = os.getenv("PG_DB", 'advdb')
PG_DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'
#
PG_DSN = os.getenv("PG_DSN", f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}")
# PG_DSN = 'postgresql://user2:user2psql@127.0.0.1:5431/advdb'
TOKEN_TTL = int(os.getenv("TOKEN_TTL", 86400))  # Указываем длительность хранения токена по умолчанию 86400
# PASSWORD_LENGTH = int(os.getenv("PASSWORD_LENGTH", 12))