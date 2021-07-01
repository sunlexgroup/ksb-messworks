from databases import Database
import sqlalchemy

from config.main import settings

db = Database(settings.DATABASE_URI)
metadata = sqlalchemy.MetaData()
