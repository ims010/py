import smtplib

from string import Template

from email.mine.multipart import MIMEMultipart
from email.mime.text import MIMEtext

MY_ADDRESS = 'my_address@example.com'
PASSWORD = 'mypassword'


def get_contact(filename):
    name = []
    emails = []
    with open(filename. mode='r', encoding='utf-8') as contact_file:
        for a_contact in contacts_file:
            name.append(a_contact.spilt()[0])
            email.append(a_contact.spilt()[1])
        return name, emails

    def read_template(filename):
        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file_read()
        return Template(template_file_content)

    def main():
        names, emails = get_contacts('mycontact.txt')
        message
