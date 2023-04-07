from sqlalchemy import Integer, Column
from sqlalchemy.orm import relationship

from transactions_with_broker.db.config import BaseModel
from transactions_with_broker.db.models.clients import Clients


class Wallets(BaseModel):
    __tablename__ = "wallets"
    id = Column(Integer, primary_key=True)
    account = Column(Integer, nullable=False, unique=True)
    cash = Column(Integer, nullable=False)  # проверить, дефолт 0
    clients = relationship(Clients, backref="wallets")

    def __repr__(self):
        return f'<Wallets "{self.number_wallet}">'
