import argparse
from secrets import choice
import string

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='A small script to generate you a password.')
    parser.add_argument('length', type=int, help='The length of your password')
    
    parser.add_argument('-c', '--capital', action='store_true', help='Allow usage of capital characters')
    parser.add_argument('-s', '--special', action='store_true', help='Allow usage of special characters')
    parser.add_argument('-n', '--numeric', action='store_true', help='Allow usage of numeric characters')

    parser.add_argument('-C', '--count', type=int, default=1, help='Ability to generate more than one password at a time!')
    parser.add_argument('-S', '--save', type=str, help='file name to save the file in!')

    args = parser.parse_args()

    return args

def get_chars (capital: bool, special: bool, numeric: bool) -> str:
    result = string.ascii_lowercase + string.ascii_uppercase*capital + string.punctuation*special + string.digits*numeric

    return result

def generate (length: int, space: str) -> str:
    if length > 0:
        return ''.join([choice(space) for _ in range(length)])
    else:
        raise Exception(f'{length} needs to be greater than 0')

def main() -> None:
    args = get_args()
    space = get_chars(args.capital, args.special, args.numeric)

    passwords = '\n'.join([generate(args.length, space) for _ in range(args.count)])

    if args.save:
        with open(args.save, 'w+') as file:
            file.write(passwords)
    else:
        print(passwords)

if __name__ == '__main__':
    main()