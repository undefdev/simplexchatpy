class SimplexChatError(Exception):
    """Base exception class for SimpleX Chat Protocol errors."""
    pass

class EncodingError(SimplexChatError):
    """Raised when there's an error encoding a message."""
    pass

class DecodingError(SimplexChatError):
    """Raised when there's an error decoding a message."""
    pass
