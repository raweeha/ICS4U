
yahoo_list = []
gmail_list = []
hotmail_list = []
hdsb_list = []
invalid_email_list = []

with open('emails.txt') as f:
    for line in f:
        line = line.strip()
        if "@yahoo" in line:
            yahoo_list.append(line)
        elif "@gmail" in line:
            gmail_list.append(line)
        elif "@hotmail" in line:
            hotmail_list.append(line)
        elif "@hdsb" in line:
            hdsb_list.append(line)
        else:
            invalid_email_list.append(line)

print ("Yahoo List:", yahoo_list)
print ("Gmail List:", gmail_list)
print ("Hotmail List:", hotmail_list)
print ("HDSB List:", hdsb_list)
print ("Invalid List:", invalid_email_list)


