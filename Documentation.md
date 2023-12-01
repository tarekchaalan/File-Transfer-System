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

1. Add comments within the code ([server.py](https://github.com/tarekchaalan/File-Transfer-System/blob/main/server.py) and [client.py](https://github.com/tarekchaalan/File-Transfer-System/blob/main/client.py)) to explain complex sections.

2. Provide information about functions, classes, and modules. Include information on parameters, return values, and any exceptions raised.

---

## [Server.py](https://github.com/tarekchaalan/File-Transfer-System/blob/main/server.py)

`recv_all(sock, numBytes)`: Receives a specific number of bytes from a socket.
`send_file(dataSock, filePath)`: Sends a file over a socket.
`handle_client(controlSock, addr)`: Manages commands from a connected client.

## [Client.py](https://github.com/tarekchaalan/File-Transfer-System/blob/main/client.py)

`find_file(name, path)`: Searches for a file within a directory and its subdirectories.
`send_command(connSock, command)`: Sends a command to the server via a socket.
`receive_response(connSock)`: Receives a response from the server via a socket.

---

## Protocol Diagram

![Protocol Diagram](https://i.imgur.com/R6DfL1W.png)

## Installation Instruction

Instructions on how to install and set up the project.

## Testing

Explain how to run tests and provide examples of expected outcomes.
