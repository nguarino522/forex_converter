from flask import Flask, request, render_template, redirect, flash, session, jsonify
from forex_python.converter import CurrencyRates,CurrencyCodes
from convert import ConvertCurrency


app = Flask(__name__)
app.config['SECRET_KEY'] = "24rjk24kj3"

cc = ConvertCurrency()

@app.route("/")
def default_route():
    """default route"""

    return render_template("index.html")

@app.route("/convert")
def convert_route():
    """convert route and handling"""
    
    curr_code_to = request.args.get('currencycodeto').upper()
    curr_code_from = request.args.get('currencycodefrom').upper()
    amount = float(request.args.get('amounttoconvert'))
    symbol_to = cc.retrieve_currency_symbol(curr_code_to)
    symbol_from = cc.retrieve_currency_symbol(curr_code_from)
    
    valid_curr_code_result = cc.check_valid_currency_code(curr_code_to, curr_code_from)

    if valid_curr_code_result:
        convert_result = cc.convert_currency(curr_code_from, curr_code_to, amount)
        if type(convert_result) == "<class 'str'>":
            flash(f"{convert_result}")
            return redirect("/")
        else:
            flash(f"SUCCESS: Converted {symbol_from}{amount} of {curr_code_from} to {curr_code_to}. The amount is {symbol_to}{convert_result}")
            return redirect("/")
    elif not valid_curr_code_result:
        flash("ERROR: One or more currency codes are invalid. Please enter a valid currency code.")
        return redirect("/")
    else:
        flash("ERROR: Potential unknown error has occurred.")
        return redirect("/")