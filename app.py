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
    amount = request.args.get('amounttoconvert')
         
    check_valid_num = cc.check_convert_valid_num(amount)   
    valid_curr_code_result = cc.check_valid_currency_code(curr_code_to, curr_code_from)
    
    if valid_curr_code_result and check_valid_num:
        convert_result = cc.convert_currency(curr_code_from, curr_code_to, check_valid_num)
        if isinstance(convert_result, str):
            flash(f"{convert_result}")
            return redirect("/")
        else:
            flash(f"SUCCESS: Converted currenncy from {curr_code_from} to {curr_code_to}. The amount is {cc.retrieve_currency_symbol(curr_code_to)}{convert_result}")
            return redirect("/")
        
    if not valid_curr_code_result and check_valid_num:
        flash("ERROR: One or more currency codes are invalid. Please enter a valid currency code.")
        return redirect("/")
    
    
    if valid_curr_code_result and not check_valid_num:
        flash("ERROR: The number entered is invalid. Please enter a valid number.")
        return redirect("/")
    
    if not valid_curr_code_result and not check_valid_num:
        flash("ERROR: The number entered is invalid. Please enter a valid number.")
        flash("ERROR: One or more currency codes are invalid. Please enter a valid currency code.")
        return redirect("/")
