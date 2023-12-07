# Documentation for CPSC 471 Final Project - TCP Sockets

[<svg xmlns="http://www.w3.org/2000/svg" height="50" width="50" viewBox="0 0 448 512"><path d="M448 96c0-35.3-28.7-64-64-64H64C28.7 32 0 60.7 0 96V416c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V96zM265.8 407.7c0-1.8 0-6 .1-11.6c.1-11.4 .1-28.8 .1-43.7c0-15.6-5.2-25.5-11.3-30.7c37-4.1 76-9.2 76-73.1c0-18.2-6.5-27.3-17.1-39c1.7-4.3 7.4-22-1.7-45c-13.9-4.3-45.7 17.9-45.7 17.9c-13.2-3.7-27.5-5.6-41.6-5.6s-28.4 1.9-41.6 5.6c0 0-31.8-22.2-45.7-17.9c-9.1 22.9-3.5 40.6-1.7 45c-10.6 11.7-15.6 20.8-15.6 39c0 63.6 37.3 69 74.3 73.1c-4.8 4.3-9.1 11.7-10.6 22.3c-9.5 4.3-33.8 11.7-48.3-13.9c-9.1-15.8-25.5-17.1-25.5-17.1c-16.2-.2-1.1 10.2-1.1 10.2c10.8 5 18.4 24.2 18.4 24.2c9.7 29.7 56.1 19.7 56.1 19.7c0 9 .1 21.7 .1 30.6c0 4.8 .1 8.6 .1 10c0 4.3-3 9.5-11.5 8C106 393.6 59.8 330.8 59.8 257.4c0-91.8 70.2-161.5 162-161.5s166.2 69.7 166.2 161.5c.1 73.4-44.7 136.3-110.7 158.3c-8.4 1.5-11.5-3.7-11.5-8zm-90.5-54.8c-.2-1.5 1.1-2.8 3-3.2c1.9-.2 3.7 .6 3.9 1.9c.3 1.3-1 2.6-3 3c-1.9 .4-3.7-.4-3.9-1.7zm-9.1 3.2c-2.2 .2-3.7-.9-3.7-2.4c0-1.3 1.5-2.4 3.5-2.4c1.9-.2 3.7 .9 3.7 2.4c0 1.3-1.5 2.4-3.5 2.4zm-14.3-2.2c-1.9-.4-3.2-1.9-2.8-3.2s2.4-1.9 4.1-1.5c2 .6 3.3 2.1 2.8 3.4c-.4 1.3-2.4 1.9-4.1 1.3zm-12.5-7.3c-1.5-1.3-1.9-3.2-.9-4.1c.9-1.1 2.8-.9 4.3 .6c1.3 1.3 1.8 3.3 .9 4.1c-.9 1.1-2.8 .9-4.3-.6zm-8.5-10c-1.1-1.5-1.1-3.2 0-3.9c1.1-.9 2.8-.2 3.7 1.3c1.1 1.5 1.1 3.3 0 4.1c-.9 .6-2.6 0-3.7-1.5zm-6.3-8.8c-1.1-1.3-1.3-2.8-.4-3.5c.9-.9 2.4-.4 3.5 .6c1.1 1.3 1.3 2.8 .4 3.5c-.9 .9-2.4 .4-3.5-.6zm-6-6.4c-1.3-.6-1.9-1.7-1.5-2.6c.4-.6 1.5-.9 2.8-.4c1.3 .7 1.9 1.8 1.5 2.6c-.4 .9-1.7 1.1-2.8 .4z"/></svg>](https://github.com/tarekchaalan/File-Transfer-System)

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
