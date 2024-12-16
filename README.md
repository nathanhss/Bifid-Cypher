# Bifid-Cypher

Bifid Cypher Implementation Using Python

## Example of usage

Create plaintext file:

```bash
    touch plaintext.txt
    echo "Hello World" > plaintext.txt
```

Create a key of your preferred:

```bash
    touch key.key
    echo "My key" > key.key
```

Calling bifid-encrypt.py:

```bash
    python3 bifid-encrypt.py plaintext.txt key.key
```

It's will return another file called `encrypted_text.txt`

Calling bifid-decrypt.py:

```bash
    python3 bifid-decrypt.py encrypted_text.txt key.key
```

It's will return another file called `output.txt`

Note: the output text doesn't have any spacing like the original message, so you need to interpret it yourself
