# your code goes here!
import re


class EmailAddressParser:
    
    def __init__(self, mail_address):
        self.mail_address = mail_address
    
    def parse(self):
        
        emails = re.split(r'[,\s]+', self.mail_address)
        emails = [email.strip() for email in emails]
        unique_email = sorted(set(emails))
        return unique_email



email_addresses = "john@doe.com, person@somewhere.org"  
parser = EmailAddressParser(email_addresses)     

parser.parse()