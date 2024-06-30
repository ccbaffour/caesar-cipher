# Caesar Cipher Tool

This Python script implements a Caesar Cipher tool that allows you to encrypt, decrypt, or bruteforce decrypt text using a specified shift value.

## Usage

Run the script `main.py` with the following command-line options:

### Options

- `-h, --help`: Show help message and exit.
- `-e string, --encrypt string`: Encrypt the given text.
- `-d string, --decrypt string`: Decrypt the given text.
- `-b string, --bruteforce string`: Attempt to bruteforce decrypt the text (all possible shifts).
- `-s SHIFT, --shift SHIFT`: Specify the shift value for encryption/decryption.

## Example

Encrypt a message:
```bash
python main.py -e "Hello" -s 3
```

Decrypt a message:
```bash
python main.py -e "Khoor" -s 3
```
Bruteforce decrypt a message:
```bash
python main.py -b "Khoor"
```

The script uses the simple Caesar Cipher algorithm where each letter in the text is shifted by the specified number of positions in the alphabet.

Feel free to customize the script or improve upon it for your needs!
