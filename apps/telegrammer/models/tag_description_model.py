import sqlalchemy
from config.db import metadata, db


tag_description = sqlalchemy.Table(
    "messworks_tag_description",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("tag", sqlalchemy.String, unique=True),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=True)
)


class TagDescription:
    @classmethod
    async def get(cls):
        query = tag_description.select()
        data = await db.fetch_one(query)
        return data

    @classmethod
    async def create(cls, **data):
        query = tag_description.insert().values(**data)
        created = await db.execute(query)
        return created
