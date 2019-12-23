import sys, re, dns.resolver, socket, smtplib
def isNumber(n, min = -1, max = sys.maxsize):
    try:
        val = int(n)
        return min <= val and val <= max
    except ValueError:
        return False


def isNumberEx(n, min=-1, max=sys.maxsize):
    if isNumber(n, min, max):
        sys.exit(0)
    sys.exit(1)

def isValidEmail (email):
    # Step 1: Check email
    # Check using Regex that an email meets minimum requirements, throw an error if not
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match == None:
        print('Bad Syntax in ' + email)
        return False

    # Step 2: Getting MX record
    # Pull domain name from email address
    domain_name = email.split('@')[1]

    # get the MX record for the domain
    records = dns.resolver.query(domain_name, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    # Step 3: ping email server
    # check if the email address exists

    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail(email)
    code, message = server.rcpt(str(email))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        print('Y')
        return True
    else:
        print('N')
        return False

def isValidEmailEx (email):
    if isValidEmail(email):
        sys.exit(0)
    sys.exit(1)

