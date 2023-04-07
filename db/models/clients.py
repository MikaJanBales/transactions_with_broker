from sqlalchemy import Integer, Column, String, ForeignKey

from transactions_with_broker.db.config import BaseModel


class Clients(BaseModel):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    wallet_id = Column(Integer, ForeignKey('wallets.id'))

    def __repr__(self):
        return f'<Clients "{self.client_name}">'
