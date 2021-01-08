import random

# Non-route functions
def code(length):
    pw_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    pw_chars = list(pw_chars)
    random.shuffle(pw_chars)
    pw = random.choices(pw_chars, k=length)
    pw = ''.join(pw)
    return pw

def strong_code(length):
    pw_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@·$%&()=+-_;,.:#'
    pw_chars = list(pw_chars)
    random.shuffle(pw_chars)
    pw = random.choices(pw_chars, k=length)
    pw = ''.join(pw)
    return pw

print(code(12))