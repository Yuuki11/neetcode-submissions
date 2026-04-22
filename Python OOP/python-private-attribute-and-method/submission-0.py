class PasswordManager:
    def __init__(self, password: str):
        self.__password = password
        
    
    def verify_password(self, input_password: str) -> bool:
        return input_password == self.__password

# Do not modify the code below this line
ps_1 = PasswordManager("blue")
print(ps_1.verify_password("blue"))
print(ps_1.verify_password("pink"))

