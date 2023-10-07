import json
from models import MessageContent, MessageContainer, Profile
from exceptions import EncodingError, DecodingError

class SimplexEncoder(json.JSONEncoder):
    def default(self, obj):
        # If the object is an instance of any of our data classes, return its dictionary representation
        if isinstance(obj, (Profile, MessageContent, MessageContainer)):
            return obj.__dict__
        # Otherwise, let the base class handle the object
        return super().default(obj)

def encode_message(message_obj):
    """Encode a message for transmission using the SimpleX Chat Protocol."""
    if message_obj is None:
        raise EncodingError("Message object is None.")

    try:
        return json.dumps(message_obj, cls=SimplexEncoder)
    except Exception as e:
        raise EncodingError(f"Error encoding message: {e}")

def decode_message(encoded_message):
    """Decode a received message using the SimpleX Chat Protocol."""
    try:
        message_dict = json.loads(encoded_message)

        if "content" not in message_dict:
            raise DecodingError("The 'content' key is missing from the encoded message.")

        content_data = message_dict["content"]
        if not isinstance(content_data, dict):
            raise DecodingError("The 'content' key should contain a dictionary.")

        content = MessageContent(**content_data)
        return MessageContainer(content=content,
                                file=message_dict.get("file"),
                                quote=message_dict.get("quote"),
                                forward=message_dict.get("forward", False))
    except Exception as e:
        raise DecodingError(f"Error decoding message: {e}")
