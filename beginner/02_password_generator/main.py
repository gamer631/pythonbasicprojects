"""Generate a password using the secrets module."""
import secrets, string

def main():
    try: size=int(input('Password length (8+): '))
    except ValueError: print('Use a whole number.'); return
    if size<8: print('Length must be at least 8.'); return
    alphabet=string.ascii_letters+string.digits+'!@#$%^&*_-+'
    print('Password:', ''.join(secrets.choice(alphabet) for _ in range(size)))
if __name__=='__main__': main()
