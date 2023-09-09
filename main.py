import imaplib
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

username =  os.getenv("EMAIL")
password =  os.getenv("PASSWORD")
host = "imap.mail.me.com" # iCloud IMAP server
port = 993 # default IMAP SSL port

M = imaplib.IMAP4_SSL(host, port)
M.login(username, password)

# Functions

def retrieve_date(from_date):
    now = datetime.now()
    date = now - timedelta(days=from_date)
    date_str = date.strftime("%d-%b-%Y")
    return date_str

def search_mails(from_sender, date):
    M.select()
    # Search for mails from a specific sender and since a specific date
    res, data = M.search("UTF-8", f'SINCE "{date}"', f'FROM "{from_sender}"')
    if res != "OK":
        print("Error searching mails.")
        return 0
    return data

def fetch_email(id):
    # Fetch the email body (RFC822) for the given ID
    res, data = M.fetch(id, "(UID BODY[TEXT])")
    if res == 'OK':
        return response_part
    return None


if __name__ == "__main__":

    fromSender = "Amazon"
    data = search_mails(fromSender, retrieve_date(7))
    data_list = data[0].split()
    # Get the most recent email id
    raw_email = fetch_email(data_list[-1])
    print(raw_email[1])
    M.close()
    M.logout()