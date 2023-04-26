#Read email addresses in from file. Generate a different list for each valid
#email address (@yahoo @hotmail @gmail @hdsb etc.)
#Invalid email address are @fake @mail
#Data can be stored as it appears in the file

yahoo_list = []
hotmail_list = []
gmail_list = []
hdsb_list = []
invalid_list = []

with open('emails.txt') as file_in:
    for line in file_in:
        line = line.strip()

        if '@hotmail' in line:
            hotmail_list.append(line)
        if '@yahoo' in line:
            yahoo_list.append(line)
        if '@gmail' in line:
            gmail_list.append(line)
        if '@hdsb' in line:
            hdsb_list.append(line)
        if '@fake' in line or '@mail' in line:
            invalid_list.append(line)

print(yahoo_list)
print(gmail_list)
        

