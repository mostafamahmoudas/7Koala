### README - **7Koala** - Anti-DDoS Protection

---

**7Koala** is an advanced DDoS protection system designed to safeguard your server from various types of attacks. This guide provides step-by-step instructions on how to install and use **7Koala** on your Linux server.

---

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Instructions](#installation-instructions)
3. [Setup and Configuration](#setup-and-configuration)
4. [Running the Service](#running-the-service)
5. [Web Interface](#web-interface)
6. [Usage](#usage)
7. [License](#license)

---

### System Requirements

- **Operating System**: Ubuntu 20.04 or later, Debian 10 or later
- **Python Version**: Python 3.6 or higher
- **Root Privileges**: Required for installing dependencies and configuring the firewall
- **Network Configuration**: Ensure that ports 80 (HTTP) and 443 (HTTPS) are open for the web interface

---

### Installation Instructions

Follow these steps to install **7Koala** on your server:

1. **Log into your server as root** or use `sudo` for root access:

   ```bash
   sudo su
   ```

2. **Download the installation script**:

   Download the `bash.sh` script to automate the installation:

   ```bash
   wget https://7tteam.com/7Koala/latest/bash.sh
   ```

3. **Make the script executable**:

   ```bash
   chmod +x bash.sh
   ```

4. **Run the installation script**:

   ```bash
   ./bash.sh
   ```

   This script will:
   - Update your system.
   - Install the required dependencies: Python, iptables, psutil, Scapy, and git.
   - Clone the **7Koala** repository from GitHub.
   - Set up the necessary firewall rules using **iptables**.
   - Create a `systemd` service for auto-starting the protection system.

---

### Setup and Configuration

1. **Configure Firewall (iptables)**:

   The script automatically sets up basic firewall rules to allow HTTP (80) and HTTPS (443) traffic and block potential malicious requests. If you need to customize firewall settings, modify `/etc/iptables/rules.v4`.

2. **Configure Protection Settings**:

   Open the file `/opt/7Koala/7Koala_config.py` to adjust the protection rules based on your server’s traffic needs.

   Example configuration:
   ```python
   MAX_REQUESTS_PER_SECOND = 1000  # Max requests per second allowed
   BLOCK_TIME = 60  # Time to block the IP after excessive requests (seconds)
   ```

3. **Web Interface Setup**:

   The web interface is available at `http://yourserverip:5000` by default. You can configure it to run on a different port if required by editing the configuration file in `/opt/7Koala/config.json`.

---

### Running the Service

To start **7Koala** and enable it to run on system boot, use the following commands:

1. **Enable and Start the Service**:

   ```bash
   systemctl enable 7Koala.service
   systemctl start 7Koala.service
   ```

2. **Check the Status of the Service**:

   To ensure that **7Koala** is running properly, check the service status:

   ```bash
   systemctl status 7Koala.service
   ```

---

### Web Interface

The web interface allows you to monitor the following in real-time:

- **Number of attacks blocked**
- **Server CPU usage**
- **RAM usage**
- **Blocked IP addresses**

By default, the web interface is accessible on port 5000:

```bash
http://yourserverip:5000
```

---

### Usage

- **Monitoring**: The web interface will update the statistics live, including attacks blocked and system performance metrics.
- **IP Blocking**: Suspicious IPs that exceed the request limit will be automatically blocked. You can manually unblock IPs from the web interface.
- **Log Analysis**: Review the system logs for detailed information about blocked attacks and other activities.

---

### License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

### Conclusion

With **7Koala**, you can ensure that your server is protected from DDoS attacks and that performance remains stable during high-traffic events. For any additional questions or support, feel free to contact us!

---

**Happy Protecting!** 🌐🚀
