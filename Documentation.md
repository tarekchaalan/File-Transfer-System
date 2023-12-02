# Documentation for CPSC 471 Final Project - TCP Sockets

## Team Members

|     | Name            | Email                              |
| --- | --------------- | ---------------------------------- |
| 1   | Tarek Chaalan   | tchaalan23@csu.fullerton.edu       |
| 2   | Liti Foloifo    | lfoloifo@csu.fullerton.edu         |
| 3   | Chloe Truong    | chloent@csu.fullerton.edu          |
| 4   | Kelly Kuoch     | ykuoc00001@csu.fullerton.edu       |
| 5   | Michelle Nguyen | michellenguyen12@csu.fullerton.edu |

## Overview

Develop a TCP Sockets program which uses Python to implement (simplified) FTP server and FTP client. The client shall connect to the server and support uploading and downloading of files to/from server.

## Project Structure

```
.
└── File_Transfer_System/
    ├── README.md
    ├── Documentation.md
    ├── client.py
    ├── server.py
    └── Example_Files/
        ├── MSWord.docx
        ├── document.pdf
        ├── image.jpg
        └── text.txt
```

After client sent files to server using `put` command, files are stored in folder

```
.
└── File_Transfer_System/
    └── Server_Files/
```

After client received files from server using `get` command, files are stored in folder

```
.
└── File_Transfer_System/
    └── Client_<client-port-number>_Received/
```

## Code Documentation

### [Client.py](https://github.com/tarekchaalan/File-Transfer-System/blob/main/client.py)

1.  ```
    def find_file(name, path='.'):

    Search for a file with a given name within a specified directory and its subdirectories.

    Parameters:
    - name: The name of the file to find.
    - path: The directory path to start the search from. Defaults to the current directory.

    Returns:
    The full path to the file if found, or None if not found.
    ```

2.  ```
    def send_command(connSock, command):

    Send a command to the server via a socket, padding the command to a fixed length.

    Parameters:
    - connSock: The socket object used for the connection.
    - command: The command string to be sent.

    Returns:
    None.
    ```

3.  ```
    def receive_response(connSock):

    Receive a response from the server via a socket.

    Parameters:
    - connSock: The socket object used for the connection.

    Returns:
    The decoded response string from the server.
    ```

4.  ```
    def send_file(dataSock, fileName):

    Send a file to the server over a socket.

    Parameters:
    - dataSock: The socket object used for the data transfer.
    - fileName: The name of the file to be sent.

    Returns:
    A boolean indicating whether the file was successfully sent or not.
    ```

5.  ```
    def receive_file(dataSock, fileName, clientPort):

    Receive a file from the server and save it to a client-specific directory.

    Parameters:
    - dataSock: The socket object used for the data transfer.
    - fileName: The name of the file to be received.
    - clientPort: The port number of the client, used to create a unique directory.

    Returns:
    None.
    ```

6.  ```
    def main():

    Main function to run the client. Handles connection to the server and user inputs.

    Parameters:
    None.

    Returns:
    None.
    ```

### [Server.py](https://github.com/tarekchaalan/File-Transfer-System/blob/main/server.py)

1.  ```
    def recv_all(sock, numBytes):

    Receive a specific number of bytes from a socket.

    Parameters:
    - sock: The socket object to receive data from.
    - numBytes: The exact number of bytes to receive.

    Returns:
    A bytes object containing the received data.
    ```

2.  ```
    def send_file(dataSock, filePath):

    Send a file over a socket.

    Parameters:
    - dataSock: The socket object used for the data transfer.
    - filePath: The full path of the file to be sent.

    Returns:
    None.
    ```

3.  ```
    def handle_client(controlSock, addr):

    Handle commands from a connected client.

    Parameters:
    - controlSock: The control socket connected to the client.
    - addr: The address tuple of the client.

    Returns:
    None.
    ```

4.  ```
    def main():

    Main function to start the server and accept client connections.

    Parameters:
    None.

    Returns:
    None.
    ```


## Protocol Diagram

![Protocol Diagram](https://i.imgur.com/R6DfL1W.png)


## Testing
**1. Test the Server**

- **Run Server**

        Example: "python server.py 1234"

        Expected Outcome: The server starts and waits for connections

**2. Test the Client**

- **Run Client**

        Example: "python client.py 1234"

        Expected Outcome: The client is connecting to the server and the user is prompted to enter a command

**3. Test FTP Commands**

- **put Command**

        Allows the user to insert a file into the server
        Example: "put MSWord.docx"

        Expected Outcome: The client sends the file to the server. If the file you are putting in is invalid, it will say "file <input> does not exist."

- **get Command**

        Allows the user to receive a file from the server
        Example: "get MSWord.docx"

        Expected Outcome: The client receives the file from the server. If the file you are getting is invalid, it will say "File not found."

- **ls Command**

        Allows the user to view all files frmo the server
        Example: "ls"

        Expected Outcome: The client displays a list of files from the server, if there are no files on the server, it will display "NONE"

- **quit Command**

        Allows the user to close the connection from client to server
        Example: "quit"

        Expected Outcome: The client disconnects from the server