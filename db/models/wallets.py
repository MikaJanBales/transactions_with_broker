from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from transactions_with_broker.db.app import BaseModel
from transactions_with_broker.db.models.clients import Clients


class Wallets(BaseModel):
    __tablename__ = "wallets"
    id = Column(Integer(), primary_key=True)
    account = Column(Integer, nullable=False, unique=True)
    cash = Column(Integer, nullable=False)
    clients = relationship(Clients, backref="wallets")
