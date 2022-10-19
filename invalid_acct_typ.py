from mimetypes import init


class InvalidAccountTypeError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)