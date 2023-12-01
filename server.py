import socket
import threading
import os
import sys

def recv_all(sock, numBytes):
    """
    Receive a specific number of bytes from a socket.

    Parameters:
    - sock: The socket object to receive data from.
    - numBytes: The exact number of bytes to receive.

    Returns:
    A bytes object containing the received data.
    """
    recvBuff = b""
    while len(recvBuff) < numBytes:
        tmpBuff = sock.recv(numBytes)
        if not tmpBuff:
            break
        recvBuff += tmpBuff
    return recvBuff

def send_file(dataSock, filePath):
    """
    Send a file over a socket.

    Parameters:
    - dataSock: The socket object used for the data transfer.
    - filePath: The full path of the file to be sent.

    Returns:
    None.
    """
    with open(filePath, "rb") as fileObj:
        while True:
            fileData = fileObj.read(65536)
            if not fileData:
                break
            dataSock.sendall(fileData)

def handle_client(controlSock, addr):
    """
    Handle commands from a connected client.

    Parameters:
    - controlSock: The control socket connected to the client.
    - addr: The address tuple of the client.

    Returns:
    None.
    """
    clientIP, clientPort = addr
    try:
        while True:
            commandBuff = recv_all(controlSock, 100)
            command = commandBuff.decode().strip('\0')
            if not command:
                break

            if command == 'quit':
                controlSock.sendall("Quitting".encode().ljust(100, b'\0'))
                break
            elif command.startswith('put'):
                _, fileName = command.split()
                baseFileName = os.path.basename(fileName)

                if not os.path.exists("Server_Files"):
                    os.makedirs("Server_Files")

                dataSock, _ = welcomeDataSock.accept()
                fileSizeBuff = recv_all(dataSock, 10)
                fileSizeStr = fileSizeBuff.decode().strip('\0').strip()
                if fileSizeStr.isdigit():
                    fileSize = int(fileSizeStr)
                else:
                    print("Invalid file size received.")
                    dataSock.close()
                    continue

                receivedSize = 0
                with open(f"Server_Files/{baseFileName}", "wb") as f:
                    while receivedSize < fileSize:
                        fileData = dataSock.recv(min(65536, fileSize - receivedSize))
                        if not fileData:
                            break
                        f.write(fileData)
                        receivedSize += len(fileData)

                dataSock.close()
                controlSock.sendall("File received".encode().ljust(100, b'\0'))
                print(f"Received {baseFileName} from Client {clientPort}")
            elif command.startswith('get'):
                _, fileName = command.split()
                filePath = os.path.join("Server_Files", fileName)

                if os.path.isfile(filePath):
                    controlSock.sendall("File found. Sending...".encode().ljust(100, b'\0'))
                    print(f"Sending {fileName} to Client {clientPort}")

                    dataSock, _ = welcomeDataSock.accept()
                    send_file(dataSock, filePath)
                    dataSock.close()
                else:
                    controlSock.sendall("File not found".encode().ljust(100, b'\0'))
            elif command == 'ls':
                if not os.path.exists("Server_Files"):
                    os.makedirs("Server_Files")

                files = os.listdir("Server_Files")
                if files:
                    fileList = ', '.join(files)
                else:
                    fileList = 'NONE'

                controlSock.sendall(fileList.encode().ljust(100, b'\0'))
                print(f"Showing Client {clientPort} the server files")

    except Exception as e:
        print(f"\nError: {e}")
    finally:
        controlSock.close()
        print(f"\nConnection closed with {addr}.\n")

def main():
    """
    Main function to start the server and accept client connections.

    Parameters:
    None.

    Returns:
    None.
    """
    global welcomeDataSock
    if len(sys.argv) > 1:
        listenPort = int(sys.argv[1])
        print("Opening port #" + str(listenPort))
    else:
        print("Error: Please provide an open port number")
        sys.exit(1)
    dataPort = listenPort + 1

    try:
        welcomeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        welcomeSock.bind(('', listenPort))
        welcomeSock.listen(5)

        welcomeDataSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        welcomeDataSock.bind(('', dataPort))
        welcomeDataSock.listen(5)

        print("\nServer started. Waiting for connections...")

        while True:
            try:
                controlSock, addr = welcomeSock.accept()
                print(f"Connected to Client: {addr}\n")
                clientThread = threading.Thread(target=handle_client, args=(controlSock, addr))
                clientThread.start()
            except socket.timeout:
                pass

    except KeyboardInterrupt:
        print("\nServer is shutting down...")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Other exception: {e}")
    finally:
        welcomeSock.close()
        welcomeDataSock.close()

if __name__ == "__main__":
    main()