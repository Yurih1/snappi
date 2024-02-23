from fastapi import HTTPException


class GenericExceptions:

    def __init__(self, status_code: int, message: str ) -> None:
        self.code = status_code
        self.message = message

    def generic_http_exception(self):
        raise HTTPException(status_code=self.code, detail=self.message)
