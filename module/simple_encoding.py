import random


# Osoba pierwsza - twórca wiadomości
# Tym razem posiada ona klucz - Losowy ciąg znaków który przekaże odbiorcy
def generate_key(key_length):
    key = ''
    for i in range(0, key_length):
        key = key + str(chr(random.randint(33, 126)))
    return key


# Funkcje pomocnicze zamieniąjace z i na bajty/stringi/integery
# --------------------------------------------------------------
def string_to_byte(message):
    return [format(ord(x), 'b') for x in message]


def byte_to_int(byte):
    if len(byte) < 8:
        actual_length = len(byte)
        for i in range(0, 8 - actual_length):
            byte = '0' + byte
    byte = byte[::-1]
    byte_number = 0
    int_value = 0
    for x in byte:
        int_value = int_value + (pow(2, byte_number) * int(x))
        byte_number = byte_number + 1
    return int_value


def int_to_ascii(val):
    return str(chr(val))


def create_message(message):
    print('\nMessage was created.')
    return message


# --------------------------------------------------------------


# Osoba druga - odbiorca wiadomości
def received_message(message):
    print('\nReceived message . . . decoding:')
    print('Message is:', message)
    return message


# Osoba trzecia - ktoś podsłuchujący, możemy to podciągnąć pod atak Man in the middle
# https://pl.wikipedia.org/wiki/Atak_man_in_the_middle
def man_in_the_middle(message):
    print('\nLook what we have here . . .')
    print('Intercepted message is:', message)
    return message


# Example flow
# TODO

# Tymczasowe testy:

key = generate_key(128)
print('wygenerowany klucz:', key)

print('klucz w postaci bajtów:', string_to_byte(key))
actual_key = ''
for x in string_to_byte(key):
    actual_key = actual_key + int_to_ascii(byte_to_int(x))
print('klucz odtworzony z bajtów do postaci początkowej:', actual_key)
