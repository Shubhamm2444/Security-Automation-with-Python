import subprocess

def scan_server(server_ip):
  """
  This function scans a server using the specified vulnerability scanner.

  Args:
      server_ip (str): The IP address of the server to be scanned.

  Returns:
      None
  """
  # Replace 'vuln_scanner' with the actual command for your vulnerability scanner
  command = f"vuln_scanner {server_ip}"
  try:
    # Execute the vulnerability scanner command
    subprocess.run(command.split(), check=True)
    print(f"Vulnerability scan completed for server {server_ip}")
  except subprocess.CalledProcessError as e:
    print(f"Error scanning server {server_ip}: {e}")

# List of servers to scan
server_list = ["10.0.0.1", "10.0.0.2"]

# Loop through the server list and call the scan_server function
for server in server_list:
  scan_server(server)

print("Vulnerability scanning of all servers completed!")

** Explanation of the Code:
1:We define a function scan_server that takes the server IP address as input.
2:Inside the function, we construct the command string using f-strings and the placeholder vuln_scanner.
3:We use subprocess.run to execute the vulnerability scanner command for the specified server.
4:The check=True argument in subprocess.run raises an exception if the command fails, allowing us to handle potential errors.
5:Inside the loop, we call the scan_server function for each server in the list.
6:After scanning all servers, the script prints a completion message.
