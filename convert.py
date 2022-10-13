from forex_python.converter import CurrencyRates,CurrencyCodes

class ConvertCurrency():

    def __init__(self):
        self.c = CurrencyRates()
        self.cc = CurrencyCodes()

    def convert_currency(self, curr_from, curr_to, curr_amount):
        """
        takes in 2 valid current codes and number (currency) 
        and converts from on to the other
        """
        try:
            result = self.c.convert(curr_from, curr_to, curr_amount)
        except:
            result = "ERROR: An exception occurred currency rate was most likely not available."

        return result

    
    def check_valid_currency_code(self, curr_from, curr_to):
        """
        confirm if currency codes valid or not
        as well as the number is valid
        """

        result1 = self.cc.get_currency_name(curr_from)
        result2 = self.cc.get_currency_name(curr_to)

        if result1 and result2:
            return True
        else:
            return False
            
    
    def retrieve_currency_symbol(self, curr_code):
        """simply grabs specified currency code's symbol"""

        symbol = self.cc.get_symbol(curr_code)

        return symbol
    
    def check_convert_valid_num(self, amount):
        """to attempt to convert and verify a valid number was entered"""
        
        try:
            float_num = float(amount)
            return float_num
        except:
            return False
