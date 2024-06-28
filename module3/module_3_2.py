def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    recipient_ok = False        # флаг корректности адреса получаетля
    sender_ok = False           # флаг корректности адреса отправителя

    # проверка корректности адреса получателя
    recipient_dot = recipient.rfind('.')
    if recipient[recipient_dot:] in ['.com', '.ru', '.net'] and '@' in recipient:
        recipient_ok = True

    # проверка корректности адреса отправителя
    sender_dot = sender.rfind('.')
    if sender[sender_dot:] in ['.com', '.ru', '.net'] and '@' in sender:
        sender_ok = True

    if not (recipient_ok and sender_ok):    # если хотя один из адресов некорректен
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient + '.')
    elif sender == recipient:               # если адреса отправителя и получателя совпадают
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com': # если адрес отправителя остался по умолчанию
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient + '.')
    else:                                   # адрес отправителя отличается от адреса по умолчанию
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient + '.')


send_email('Привет, что завтра делаешь?', 'sanya@yandex.ru')
send_email('Привет, что завтра делаешь?', 'sanya@yandex.by')
send_email('Привет, хорошее настроение', 'sanya@yandex.ru', sender='vovka@mail.ru')
send_email('Привет, хорошее настроение', 'vovka@mail.ru', sender='vovka@mail.ru')