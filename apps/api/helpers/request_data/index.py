from validator import Validator

class LoginValidator(Validator):
    username = 'required|max_length:50'
    password = 'required'

    
class RegisterValidator(Validator):
    username = 'required|max_length:50'
    email = 'required|email'
    password = 'required'
