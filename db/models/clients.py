from sqlalchemy import Column, ForeignKey, Integer, String


from transactions_with_broker.db.app import BaseModel


class Clients(BaseModel):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    wallet_id = Column(Integer, ForeignKey('wallets.id'))
