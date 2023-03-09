"""
init
"""

from yoyo import step

__depends__ = {'__init__'}

steps = [
    step(
        """
        CREATE TABLE wallets
            (
                id                 SERIAL PRIMARY KEY NOT NULL,
                account            INTEGER            NOT NULL,
                cash               INTEGER            NOT NULL
            );
        """
    ),
    step(
        """
        CREATE TABLE clients
            (
                id                 SERIAL PRIMARY KEY NOT NULL,
                name               VARCHAR(255)       NOT NULL,
                wallet_id          INTEGER            NOT NULL,
                FOREIGN KEY (wallet_id) REFERENCES wallets (id)
            );
        """
    ),
    step(
        """
        CREATE TABLE transactions
            (
                id                 SERIAL PRIMARY KEY NOT NULL,
                sender_id          INTEGER            NOT NULL,
                amount             INTEGER            NOT NULL,
                recipient_id       INTEGER            NOT NULL,
                is_done            BOOLEAN            NOT NULL,
                FOREIGN KEY (sender_id) REFERENCES wallets (id),
                FOREIGN KEY (recipient_id) REFERENCES wallets (id)
            );
        """
    )
]
