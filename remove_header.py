def remove_header (email):
    subject_idx = email.find("Subject")
    email = email[subject_idx:]
    subject = email[:email.find("\n")+1]
    email.strip(subject)
    message_id_x = email.find("Date:")
    email = email[message_id_x:]

    return subject + email[email.find("\n")+1:]
