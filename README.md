# Python Arsenal 
This repository contains a collection of Python scripts for various security-related tasks.

## Scripts
1. **restricted_sqli_exploit.py**
    - Restricted SQL injection exploitation script with a binary search optimization.
    - Exploit restricted SQL injection vulnerabilities using a binary search algorithm to optimize query efficiency.
    - **Dependencies**: Requires `requests`.
      
2. **sqli_exploit.py**
    - SQL injection exploitation script.
    - Exploit SQL injection vulnerabilities to extract password hashes from a vulnerable web application.
    - **Dependencies**: Requires `requests`.
  
3. **web_login_bruteforce.py**
   - Web login form bruteforcing script.
   - Bruteforce login forms on web applications using a list of usernames and passwords.
   - **Dependencies**: Requires `requests`.

4. **sha256_password_crack.py**
   - SHA256 password cracking script.
   - Crack SHA256 hashes using a provided wordlist.
   - **Dependencies**: Requires `pwntools`.
   - ```bash
     python3 sha256_password_crack.py <sha256sum>
     ```
5. **port_scanner.py**
   - This script is a simple port scanner that scans a range of ports on a specified IP address.
   - **Dependencies**: Requires `sys`, `socket`, and `datetime`.
   - ```bash
     python3 port_scanner.py <ip>
     ```

6. **ssh_brute_force.py**
   - SSH connection brute-forcing script.
   - Provide a list of common passwords and attempt to brute-force SSH connections on a specified host.
   - **Dependencies**: Requires `paramiko` and `pwntools`.


7. **bise_result_scraper.py**
   - This script is designed to automate the process of taking screenshots of result pages for students on the BISE Faisalabad website.
   - **Dependencies**: Requires `requests`, `os`, and `selenium`.

8. **decorators_demo.py**
   - This script demonstrates the usage of Python decorators to log the execution time of functions.
   - **Dependencies**: Requires `datetime` and `time`.

9. **generators_demo.py**
   - This script showcases the use of Python generators to create iterators and demonstrates the concept with examples.

10. **client_socket.py**
   - This script demonstrates how to create a basic TCP client socket in Python.
   - **Dependencies**: Requires `socket`.
  

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/mubahilll/python-arsenal.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd security-tools
   ```
3. Run the desired script:
   ```bash
   python script_name.py
   ```

## License
This repository is licensed under the [MIT License](LICENSE).
