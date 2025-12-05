from yagmail import SMTP
from config import ADMIN_EMAIL_PASSWORD


email = SMTP(user="1998ivankaa@gmail.com", password="rngh vhsz nvjs stpd")
email.send(
    to="08gz1rhkbr@spymail.one",
    subject="Test email from Python",
    contents="Hello Python!"
)
