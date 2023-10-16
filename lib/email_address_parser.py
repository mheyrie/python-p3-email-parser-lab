# your code goes here!
import re


class EmailAddressParser:
    regex = re.compile(r'[\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b]')

    def __init__(self, mail_address):
        self.mail_address = mail_address
    
    def parse(self):
        strings = (re.split(r',|\s', self.mail_address)) 
                                                
        parses_mail = set()

        for string in strings:
            if self.regex.fullmatch(string):
                parses_mail.add(string) 
                return sorted(list(parses_mail))    
        

email_addresses = "john@doe.com, person@somewhere.org"  
parser = EmailAddressParser(email_addresses)     

parser.parse()