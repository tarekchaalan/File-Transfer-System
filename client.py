import socket
import os
import sys

def find_file(name, path='.'):
    """
    Search for a file with a given name within a directory and its subdirectories.

    Parameters:
    - name: The name of the file to find.
    - path: The directory path to start the search from. Defaults to the current directory.

    Returns:
    The full path to the file if found, or None if not found.
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

def send_command(connSock, command):
    """
    Send a command to the server via a socket, padding it to a fixed length.

    Parameters:
    - connSock: The socket object used for the connection.
    - command: The command string to be sent.

    Returns:
    None.
    """
    connSock.sendall(command.encode().ljust(100, b'\0'))

def receive_response(connSock):
    """
    Receive a response from the server via a socket.

    Parameters:
    - connSock: The socket object used for the connection.

    Returns:
    The decoded response string from the server.
    """
    response = connSock.recv(1024).decode().strip('\0')
    return response

def send_file(dataSock, fileName):
    """
    Send a file to the server over a socket.

    Parameters:
    - dataSock: The socket object used for the data transfer.
    - fileName: The name of the file to be sent.

    Returns:
    A boolean indicating whether the file was successfully sent or not.
    """
    if not os.path.isfile(fileName):
        print(f"File {fileName} does not exist.")
        return False

    fileSize = os.path.getsize(fileName)
    dataSock.sendall(str(fileSize).encode().ljust(10, b'\0'))

    with open(fileName, "rb") as fileObj:
        while True:
            fileData = fileObj.read(65536)
            if not fileData:
                break
            dataSock.sendall(fileData)

    print(f"Sent {fileName} of {fileSize} bytes to the server.")
    return True

def receive_file(dataSock, fileName, clientPort):
    """
    Receive a file from the server and save it to a client-specific directory.

    Parameters:
    - dataSock: The socket object used for the data transfer.
    - fileName: The name of the file to be received.
    - clientPort: The port number of the client, used to create a unique directory.

    Returns:
    None.
    """
    clientDir = f"Client_{clientPort}_Received"
    if not os.path.exists(clientDir):
        os.makedirs(clientDir)

    filePath = os.path.join(clientDir, fileName)

    with open(filePath, "wb") as fileObj:
        while True:
            fileData = dataSock.recv(65536)
            if not fileData:
                break
            fileObj.write(fileData)

    print(f"Received {fileName} and saved in '{clientDir}'.")

def main():
    """
    Main function to run the client. Handles connection to the server and user inputs.

    Parameters:
    None.

    Returns:
    None.
    """
    serverAddr = "localhost"
    if len(sys.argv) > 1:
        serverPort = int(sys.argv[1])
        print("Connecting to server port #" + str(serverPort))
    else:
        print("Error: Please provide an open port number")
        sys.exit(1)

    try:
        controlSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        controlSock.connect((serverAddr, serverPort))
        localPort = controlSock.getsockname()[1]  # Client's port number
    except socket.error as e:
        print(f"Socket error: {e}")
        return
    except Exception as e:
        print(f"Other exception: {e}")
        return

    while True:
        command = input("\nEnter command (put/get/ls/quit): ").strip()

        send_command(controlSock, command)

        if command == 'quit':
            break
        elif command.startswith('put'):
            _, fileName = command.split()
            found = find_file(fileName)
            if found:
                fileName = found
            dataSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            dataSock.connect((serverAddr, serverPort + 1))
            send_file(dataSock, fileName)
            dataSock.close()
        elif command.startswith('get'):
            _, fileName = command.split()
            response = receive_response(controlSock)
            if "Sending" in response:
                dataSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dataSock.connect((serverAddr, serverPort + 1))
                receive_file(dataSock, fileName, localPort)
                dataSock.close()
            else:
                print(response)
        elif command == 'ls':
            response = receive_response(controlSock)
            print("Files on server:", response)

        if not command.startswith(('get', 'ls')):
            response = receive_response(controlSock)

    controlSock.close()

if __name__ == "__main__":
    main()