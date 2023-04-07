from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

from transactions_with_broker.db.config import BaseModel
from transactions_with_broker.db.models.wallets import Wallets


class Transactions(BaseModel):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('wallets.id'))
    amount = Column(Float, nullable=False)
    recipient_id = Column(Integer, ForeignKey('wallets.id'))
    is_done = Column(Boolean, nullable=False, default=False)

    sender = relationship(Wallets, foreign_keys=[sender_id])
    recipient = relationship(Wallets, foreign_keys=[recipient_id])

    def to_dict(self):
        return {
            'sender_id': self.sender_id,
            'amount': self.amount,
            'recipient_id': self.recipient_id,
            'is_done': self.is_done,
        }

    # def __repr__(self):
    #     return f'<Transactions "{self.sender_number}" --- "{self.recipient_number}">'
