class EmailUser:
    _email = None
    _cpf = None
    _emailChat = None

    @classmethod
    def set_email(cls, email):
        email = email.strip('\"')
        cls._email = email

    @classmethod
    def get_email(cls):
        return cls._email
      
    @classmethod
    def set_emailChat(cls, email):
        cls._emailChat = email

    @classmethod
    def get_emailChat(cls):
        return cls._emailChat
    

    @classmethod
    def set_cpf(cls, cpf):
        cls._cpf = cpf

    @classmethod
    def get_cpf(cls):
        return cls._cpf