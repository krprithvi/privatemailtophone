def process_multipart_message(message):
    rtn = ''
    if message.is_multipart():
        for m in message.get_payload():
            rtn += process_multipart_message(m)
    else:
        rtn += message.get_payload()
    return rtn
