# Osoba pierwsza - twórca wiadomości
def create_message(message):
    print('\nMessage was created.')
    return message

# Osoba druga - odbiorca wiadomości
def received_message(message):
    print('\nReceived message . . . decoding:')
    print('Message is:', message)
    return message

# Osoba... trzecia? - ktoś podsłuchujący, możemy to podciągnąć pod atak Man in the middle :)
# https://pl.wikipedia.org/wiki/Atak_man_in_the_middle
def man_in_the_middle(message):
    print('\nLook what we have here . . .')
    print('Intercepted message is:', message)
    return message


# Example flow
message = 'Testowa wiadomosc do drugiej osoby\n'
createdMessage = create_message(message)
# W zwyklym flow - to leci do odbiorcy, jednak tutaj, wkrada nam się osoba trzecia:
receivedMessage = received_message(man_in_the_middle(createdMessage))
