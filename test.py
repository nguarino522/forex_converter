from unittest import TestCase
from app import app
from convert import ConvertCurrency

class RouteTests(TestCase):
    
    def setUp(self):
        """set before each test"""
        
        self.client = app.test_client()
        app.config['TESTING'] = True
        
    def test_homepage(self):
        """testing the default base route"""

        with app.test_client() as client:
            resp = client.get('/')
            self.assertEqual(resp.status_code, 200)
            
    
    def test_valid_conversion(self):
        """testing if properly convert a number"""
        
        with app.test_client() as client:
            resp = client.get("/convert?currencycodefrom=usd&currencycodeto=usd&amounttoconvert=1")
            self.assertEqual(resp.status_code, 302)
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertIn("SUCCESS: Converted currenncy", html)
            
    
    def test_invalid_currency_code(self):
        """testing if invalid currency code"""
        
        with app.test_client() as client:
            resp = client.get("/convert?currencycodefrom=usdf&currencycodeto=usd&amounttoconvert=1")
            self.assertEqual(resp.status_code, 302)
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertIn("ERROR: One or more currency codes are invalid", html)
            
    
    def test_invalid_number(self):
        """testing if invalid currency code"""
        
        with app.test_client() as client:
            resp = client.get("/convert?currencycodefrom=usd&currencycodeto=usd&amounttoconvert=fd1")
            self.assertEqual(resp.status_code, 302)
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertIn("ERROR: The number entered is invalid", html)
            
    
    def test_invalid_currency_code_and_number(self):
        """testing if invalid currency code"""
        
        with app.test_client() as client:
            resp = client.get("/convert?currencycodefrom=usdf&currencycodeto=usd&amounttoconvert=1fd")
            self.assertEqual(resp.status_code, 302)
            resp = client.get("/")
            html = resp.get_data(as_text=True)
            self.assertIn("ERROR: One or more currency codes are invalid", html)
            self.assertIn("ERROR: The number entered is invalid", html)
            
            
            

class ConvertCurrencyObjectTests(TestCase):
    
    
    def setUp(self):
        """set before each test"""
        
        self.cc = ConvertCurrency()
        
    def test_convert_currency(self):
        """testing convert currency function"""
        
        self.assertEqual(self.cc.convert_currency("USD", "USD", 1), 1)
        
    def test_valid_currency_code(self):
        """testing validate currency code function"""
        
        self.assertEqual(self.cc.check_valid_currency_code("USD","USD"), True)
        self.assertEqual(self.cc.check_valid_currency_code("USDF", "USD"), False)
        self.assertEqual(self.cc.check_valid_currency_code("USDF", "USDf"), False)
        self.assertEqual(self.cc.check_valid_currency_code("GBP", "EUR"), True)
        
    def test_check_valid_num(self):
        """testing check valid num function"""
        
        self.assertEqual(self.cc.check_convert_valid_num(5), 5.0)
        self.assertEqual(self.cc.check_convert_valid_num("afsd"), False)
        self.assertEqual(self.cc.check_convert_valid_num(5.22), 5.22)
        self.assertEqual(self.cc.check_convert_valid_num(44.24654562), 44.24654562)
        
    def test_retrieve_currency_symbol(self):
        """testing that currency symbol gets propery retrieved"""
        
        self.assertEqual(self.cc.retrieve_currency_symbol("USD"), "$")
        self.assertEqual(self.cc.retrieve_currency_symbol("usd"), None)
        self.assertEqual(self.cc.retrieve_currency_symbol("usdf"), None)