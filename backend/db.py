import uuid
import time
from sqlalchemy import MetaData, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import BigInteger

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(), primary_key=True, default=uuid.uuid4, autoincrement="auto")
    created_at = Column(BigInteger, default=int(time.time()))
    updated_at = Column(BigInteger, default=int(time.time()))