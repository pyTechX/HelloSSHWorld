import random


# Tym razem posiadamy klucz - Losowy ciąg znaków który przekaże odbiorcy
def generate_key(key_length):
    key = ''
    for i in range(0, key_length):
        key = key + str(chr(random.randint(33, 126)))
    return key


# Funkcje pomocnicze zamieniąjace z i na bajty/stringi/integery
# --------------------------------------------------------------
def string_to_byte(string):
    bytes = [int_to_bin(ord(x)) for x in string]
    byte_array = []
    for byte in bytes:
        if len(byte) < 8:
            actual_length = len(byte)
            for i in range(0, 8 - actual_length):
                byte = '0' + byte
        byte_array.append(byte)
    return byte_array


def int_to_bin(int):
    flag = True
    bin_str = ''
    while flag:
        remainder = int % 2
        quotient = int // 2
        if quotient == 0:
            flag = False
        bin_str += str(remainder)
        int = quotient
    bin_str = bin_str[::-1]
    return bin_str


def byte_to_int(byte):
    byte = byte[::-1]
    byte_number = 0
    int_value = 0
    for x in byte:
        int_value = int_value + (pow(2, byte_number) * int(x))
        byte_number = byte_number + 1
    return int_value


def int_to_ascii(val):
    return str(chr(val))


# --------------------------------------------------------------

# Operacje bitowe - baza kryptografii
# ------------------------------------------------------------

def bit_negate(bit):
    return '1' if bit == '0' else '0'


def bit_and(byte_bit, key_bit):
    return '1' if byte_bit == '1' and key_bit == '1' else '0'


def bit_or(byte_bit, key_bit):
    return '1' if byte_bit == '1' or key_bit == '1' else '0'


def bit_xor(byte_bit, key_bit):
    return '1' if (byte_bit == '1' and key_bit == '0') or (byte_bit == '0' and key_bit == '1') else '0'


def encode_message_with_bitwise_xor(message, key):
    encoded = []
    message_as_byte_array = string_to_byte(message)
    key_as_byte_array = string_to_byte(key)
    for i in range(0, len(message_as_byte_array)):
        byte_from_message = message_as_byte_array[i]
        byte_from_key = key_as_byte_array[i % 128]
        new_byte = ''
        for j in range(0, 8):
            new_byte = new_byte + bit_xor(byte_from_message[j], byte_from_key[j])
        encoded.append(new_byte)
    return encoded


def decode_message_with_bitwise_xor(message, key):
    decoded_message_as_byte_array = encode_message_with_bitwise_xor(message, key)
    return byte_array_to_string(decoded_message_as_byte_array)


def byte_array_to_string(byte_array):
    actual_message = ''
    for x in byte_array:
        actual_message = actual_message + int_to_ascii(byte_to_int(x))
    return actual_message


# ------------------------------------------------------------

# Osoba pierwsza - twórca wiadomości
def create_message(message, key):
    print('\nUtworzono wiadomość.')
    return encode_message_with_bitwise_xor(message, key)


# Osoba druga - odbiorca wiadomości
def received_message(message, key):
    print('\nWiadomość otrzymana. Dekodowanie . . .')
    message = decode_message_with_bitwise_xor(message, key)
    print('Wiadomość brzmi:', message)
    return message


# Osoba trzecia - ktoś podsłuchujący, możemy to podciągnąć pod atak Man in the middle
# https://pl.wikipedia.org/wiki/Atak_man_in_the_middle
def man_in_the_middle(message):
    print('\nHmm co my tu mamy . . .')
    print('Wiadomość to tablica bajtów - łatwizna, tylko podmienie bajty na ASCII i ... voila!')
    print('Przechwycona wiadomość to:', message)
    print('\nHę...???')
    return message


# Example flow


# Tworzymy wiadomość
message = 'Pewna wiadomosc testowa Kamilu'

# Generujemy klucz
key = generate_key(128)
print('wygenerowany klucz:', key)

# Szyfrujemy wiadomość za pomocą klucza:
cyphered_message = byte_array_to_string(create_message(message, key))

# Nawet mimo ataku - MITM nikt nie odczyta naszej wiadomości... o ile nie zdobędzie klucza
cyphered_message = man_in_the_middle(cyphered_message)

# Odczytujemy wiadomość
received_message(cyphered_message, key)
