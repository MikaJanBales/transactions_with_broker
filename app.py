import os

from flask import Flask, render_template, request, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from transactions_with_broker.db.config import connect_string, BaseModel
from transactions_with_broker.db.models.clients import Clients
from transactions_with_broker.db.models.wallets import Wallets

app = Flask(__name__)
app.secret_key = os.urandom(24)  # проверка
app.config['SQALCHEMY_DATABASE_URI'] = connect_string
engine = create_engine(connect_string)

BaseModel.metadata.create_all(engine)
Session = sessionmaker(bind=engine, autoflush=False)
session = Session()


@app.route("/")
def index():
    clients = session.query(Clients).all()
    wallets = session.query(Wallets).all()
    clients_wallets = session.query(Clients, Wallets).join(Clients, Wallets.id == Clients.wallet_id).all()
    return render_template('index.html', title='Главная', clients=clients, wallets=wallets,
                           clients_wallets=clients_wallets)


@app.route("/create_wallet", methods=('POST', 'GET'))
def create_balance():
    if request.method == 'POST':
        try:
            wallets_form = Wallets(account=request.form['account'],
                                   cash=request.form['cash'])
            session.add(wallets_form)
            session.flush()
            clients_form = Clients(name=request.form['name'],
                                   wallet_id=wallets_form.id)
            session.add(clients_form)
            session.commit()
        except Exception as e:
            print(e)
            session.rollback()
    return render_template('create_wallet.html', title='Открыть счёт')


@app.route('/cash_transfer', methods=('POST', 'GET'))
def cash_transfer():
    if request.method == 'POST':
        try:
            sender = session.query(Wallets).filter(Wallets.account == int(request.form['sender_number'])).first()
            recipient = session.query(Wallets).filter(Wallets.account == int(request.form['recipient_number'])).first()

            if not sender:
                flash(f"Такого счёта '{request.form['sender_number']}' отправителя не существует")
                raise

            if sender.cash - int(request.form['amount']) < 0:
                flash("Не хватает средств")
                raise

            if not recipient:
                flash(f"Такого счёта '{request.form['recipient_number']}' получателя не существует")
                raise

            sender.cash -= int(request.form['amount'])
            session.add(sender)

            recipient.cash += int(request.form['amount'])
            session.add(recipient)

            session.commit()
        except Exception as e:
            print(e)
            session.rollback()

    return render_template('/cash_transfer.html', title='Пополнить счёт')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
