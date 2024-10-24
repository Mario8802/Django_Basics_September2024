import socket  # Import socket module for basic networking
import ssl     # Import ssl module to wrap the socket for HTTPS
import subprocess  # Import subprocess to interact with system commands

# Step 1: Create a basic TCP socket
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Wrap the socket with SSL to handle encrypted HTTPS communication
wrapped_sock = ssl.wrap_socket(my_sock)

# Step 3: Connect to the target server (www.softuni.bg) on port 443 (HTTPS port)
wrapped_sock.connect(('www.softuni.bg', 443))

# Step 4: Create an HTTP GET request.
# The GET line should only include the path ("/"), not the full URL.
# The Host header specifies the domain to request from.
cmd = "GET / HTTP/1.1\r\nHost: www.softuni.bg\r\n\r\n".encode()

# Step 5: Send the HTTP request to the server through the SSL-wrapped socket
wrapped_sock.send(cmd)

# Step 6: Initialize a list to store data chunks
html_data = []

# Step 7: Receive the server's response in chunks of 1024 bytes
# A loop is used to read the data until no more is received (indicated by an empty response)
while True:
    data = wrapped_sock.recv(1024)  # Read up to 1024 bytes at a time
    if len(data) < 1:  # If no data is received, break the loop
        break
    html_data.append(data.decode())

# Step 8: Close the SSL-wrapped socket to end the connection
wrapped_sock.close()

# Step 9: Combine all chunks into a single string
html_content = ''.join(html_data)

# Step 10: Use subprocess to open 'less' and view the output (you can use 'grep', 'wc', or 'tee' similarly)
process = subprocess.Popen(['less'], stdin=subprocess.PIPE)
process.communicate(input=html_content.encode())  # Pass the HTML content to 'less'
