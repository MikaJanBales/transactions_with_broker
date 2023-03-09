from flask import request, jsonify
from flasgger import SwaggerView
from flask_sqlalchemy_session import current_session

from transactions_with_broker.db.models import Transactions


class TransactionsView(SwaggerView):
    tags = ['transactions']
    responses = {
        200: {
            "description": "Ok",
            "content": {
                "application/json": {
                    "examples": {
                        "get": {
                            "value": {
                                "data": [{
                                    "amount": 1000.0,
                                    "is_done": True,
                                    "recipient_id": 2,
                                    "sender_id": 1
                                }]
                            }
                        },
                        "post": {
                            "value": {'transaction': 1},
                        },
                    }
                }
            }
        },
        400: {"description": "Bad Request"},
        500: {"description": "Server Error"},
    }

    def get(self):
        transactions = current_session().query(Transactions).all()
        transactions = [transaction.to_dict() for transaction in transactions]
        return jsonify({'data': transactions}), 200

    def post(self):
        session = current_session()
        data = request.json
        amount = data.get('amount')
        sender_id = data.get('sender_id')
        recipient_id = data.get('recipient_id')
        if not all([amount, sender_id, recipient_id]):
            return jsonify({'message': 'bad request'}), 400
        transaction = Transactions(
            amount=amount, sender_id=sender_id, recipient_id=recipient_id
        )
        session.add(transaction)
        session.commit()
        return jsonify({"transaction": transaction.id}), 200
