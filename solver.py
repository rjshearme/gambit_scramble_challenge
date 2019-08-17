class Solver:
    @staticmethod
    def scramble(ascii_codes, *args):
        number_args = len(args)
        for index, code in enumerate(ascii_codes):
            arg_key = args[index % number_args]
            ascii_codes[index] = code + arg_key
        return ascii_codes

    @staticmethod
    def unscramble(ascii_codes, *args):
        number_args = len(args)
        for index, code in enumerate(ascii_codes):
            arg_key = args[index % number_args]
            new_code = code - arg_key
            new_code = new_code if new_code >= 0 else new_code + 256
            ascii_codes[index] = new_code
        return ascii_codes

    @staticmethod
    def chars_to_codes(chars: str) -> list:
        return [ord(char) for char in chars]

    @staticmethod
    def codes_to_chars(codes: list) -> str:
        return ''.join([chr(code) for code in codes])
