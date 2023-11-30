### README for CPSC 471 Final Project

#### Team Members

|     | Name            | Email                              |
| --- | --------------- | ---------------------------------- |
| 1   | Tarek Chaalan   | tchaalan23@csu.fullerton.edu       |
| 2   | Liti Foloifo    | lfoloifo@csu.fullerton.edu         |
| 3   | Chloe Truong    | chloent@csu.fullerton.edu          |
| 4   | Kelly Kuoch     | ykuoc00001@csu.fullerton.edu       |
| 5   | Michelle Nguyen | michellenguyen12@csu.fullerton.edu |

#### Programming Language

- **Python**
- Version: Python 3.11.1

#### How to Execute the Program

1. **Server Execution**:

   - Navigate to the main file directory.
   - Run the server script using Python.
     - Command on Windows: `python server.py <portnumber>`
     - Command on Mac/Linux: `python3 server.py <portnumber>`
     - `<portnumber>` is the specified port at which ftp server accepts connection requests
     - For example: `python server.py 1234`

2. **Client Execution**:

   - Navigate to the main file directory.
   - Run the client script using Python on a separate terminal.
     - Command on Windows: `python client.py <portnumber>`
     - Command on Mac/Linux: `python3 client.py <portnumber>`
     - `<portnumber>` is the specified port at which ftp server accepts connection requests
     - For example: `python client.py 1234`
   - Once running, use the commands:
     - `put [filename]` -> client puts a file onto the server
     - `get [filename]` -> client retrieves a file from the server
     - `ls` -> client requests to see the list of files on the Server
     - `quit` -> client closes socket, disconnects from server

### Example Usage

![1 Server, 2 Clients](https://i.imgur.com/wHl1U2T.png)

#### Special Notes About the Submission

- **Two-Socket Architecture**: The application uses a control socket for commands and a separate data socket for file transfers.
- **Error Handling**: Error handling is implemented.
- **File Search Feature**: In the `put` command, the client's application searches for the file in the current directory and its subdirectories.
- **Client-Specific Directory**: Files received from the server are stored in a unique directory based on the client's port number.
- **Testing**: The application has been tested for basic functionality.
- **Designing the Protocol**: Please see the attached diagram "protocoldiagram.png".

#### Contact

For any queries or issues, please contact any of the team members listed above.

---
