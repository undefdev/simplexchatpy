# SimpleX Chat Protocol Library (Sketch)

This library provides a preliminary Python implementation of the [SimpleX Chat Protocol](https://github.com/simplex-chat/simplex-chat/blob/stable/docs/protocol/simplex-chat.md), designed for experimentation and learning. The goal is to offer developers an easy-to-read and interactive framework to understand the protocol's mechanics.

## Project Goal

The primary purpose of this library is to:
- Provide a clear and concise representation of the SimpleX Chat Protocol.
- Allow developers to experiment with the protocol's functionalities in a python.
- Serve as an educational tool for those interested in the SimpleX Chat Protocol.

## Current Status

The library is currently in its early stages and serves as a sketch of the protocol's core functionalities. It is not intended to be a secure or production-ready implementation.

## Features

- Encode and decode messages based on the SimpleX Chat Protocol.
- Manage user profiles, including setting, updating, and deleting profiles.
- Utility functions for encoding, decoding, and validating messages.
- Mock message and profile stores for simulation and experimentation.

## Getting Started

To experiment with the library, you can clone the repository and import the relevant modules in your Python environment. Here's a basic example:

```python
from chat import SimplexChat
from models import MessageContent, MessageContainer

# Initialize the chat instance
chat = SimplexChat()

# Set a profile
chat.set_profile(display_name="Bob", full_name="Robert Paulson")

# Create a message content
message_content = MessageContent(type="text", content="My name is Bob.")

# Create a message container with the message content
message_container = MessageContainer(content=message_content)

# Send the message
chat.send_message(message_container)

# Receive a message
received_message = chat.receive_message()
print(received_message)
```

Please note that this is a mock implementation and doesn't send/receive messages over a network.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

