from typing import Any
from pydantic import BaseModel
from flask import jsonify, make_response


class Response(BaseModel):
    data: Any
    status_code: int = 200
    message: str = None

    def to_json(self):
        return {
            "data": self.data,
            "status_code": self.status_code,
            "message": self.message
        }

    def to_response(self):
        response = make_response(self.to_json())
        response.status_code = self.status_code
        return response
