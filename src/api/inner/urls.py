from flask import Blueprint

from transactions_with_broker.src.api.inner.transactions import TransactionsView

ROUTES = [
    (
        '/transactions/',
        TransactionsView.as_view('transactions'),
        ['GET', 'POST']
    ),
]

inner_api = Blueprint("inner_api", __name__, url_prefix="/api/inner/v1")
for (path, view, methods) in ROUTES:
    inner_api.add_url_rule(path, view_func=view, methods=methods)
