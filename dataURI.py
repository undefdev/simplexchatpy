import re
import base64
from dataclasses import dataclass

@dataclass(frozen=True)
class DataURI:
    value: str

    def __post_init__(self):
        if not self.is_valid_data_uri(self.value):
            raise ValueError(f"'{self.value}' is not a valid data URI format for a base64 encoded image.")

    @staticmethod
    def is_valid_data_uri(data_uri: str) -> bool:
        pattern = r'^data:image\/[a-zA-Z+]+;base64,[a-zA-Z0-9+/=]+$'
        if match := re.match(pattern, data_uri):
            try:
                base64_data = data_uri.split(",")[1]
                base64.b64decode(base64_data)
                return True
            except Exception:
                return False
        return False
