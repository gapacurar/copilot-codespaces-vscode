import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from BankAccount import BankAccount
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Create some sample accounts
accounts = {
    "123456": BankAccount("123456", "John Doe", 1000.0),
    "654321": BankAccount("654321", "Jane Doe", 500.0)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accounts', methods=['GET'])
def get_accounts():
    return jsonify({acc_num: str(acc) for acc_num, acc in accounts.items()})

@app.route('/accounts/<account_number>', methods=['GET'])
def get_account(account_number):
    account = accounts.get(account_number)
    if account:
        return jsonify(str(account))
    return jsonify({"error": "Account not found"}), 404

@app.route('/accounts/<account_number>/deposit', methods=['POST'])
def deposit(account_number):
    account = accounts.get(account_number)
    if account:
        amount = request.json.get('amount')
        if account.deposit(amount):
            return jsonify({"message": "Deposit successful", "balance": account.get_balance()})
        return jsonify({"error": "Invalid amount"}), 400
    return jsonify({"error": "Account not found"}), 404

@app.route('/accounts/<account_number>/withdraw', methods=['POST'])
def withdraw(account_number):
    account = accounts.get(account_number)
    if account:
        amount = request.json.get('amount')
        if account.withdraw(amount):
            return jsonify({"message": "Withdrawal successful", "balance": account.get_balance()})
        return jsonify({"error": "Invalid amount or insufficient funds"}), 400
    return jsonify({"error": "Account not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)