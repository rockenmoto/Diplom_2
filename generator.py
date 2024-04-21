import random
import string


class Generator:
    @staticmethod
    def generate_rdm_str(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string
