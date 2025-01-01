class ServiceReturnType:
    def __init__(self, is_err: bool, msg: str, data: any, code: int) -> None:
        self.is_err = is_err
        self.msg    = msg
        self.data   = data
        self.status = code

    def get_response(self) -> dict:
        return {
            'is_err': self.is_err,
            'msg': self.msg,
            'data': self.data
        }
    
    def get_status(self) -> int:
        return self.status