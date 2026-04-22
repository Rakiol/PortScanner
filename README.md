# PortScanner 🔍

A simple Python port scanner built to practice core Python concepts like functions, loops, sockets, file I/O and CLI argument parsing.

## Features

- Scan a **single port** or a **range of ports**
- Displays the **service name** for open ports (e.g. Port 80 → http)
- Saves all open ports to `openPorts.txt`
- CLI-based — pass arguments directly when running the script
- `--help` flag for usage instructions
- Timeout handling for fast scanning

## Requirements

- Python 3.x
- No external libraries needed — uses only the built-in `socket` and `sys` modules

## Usage

```bash
# Scan a single port
python main.py <ip/domain> <port>

# Scan a port range
python main.py <ip/domain> <start> <end>

# Show help
python main.py --help
python main.py -h
```

## Examples

```bash
python main.py 127.0.0.1 80
python main.py scanme.nmap.org 1 1024
```

Output:
```
Scanning Port: 22
Scanning Port: 23
...
Port 80 is OPEN and Service: http
```

Open ports are saved to `openPorts.txt` in the same directory.

## Project Structure

```
PortScanner/
├── main.py          # Main scanner with scan_port() and scan_range()
└── openPorts.txt    # Output file (auto-generated)
```

## ⚠️ Legal Notice

Only scan systems you own or have explicit permission to scan. Unauthorized port scanning may be illegal in your country.

## What I learned

This project was built as a **Python learning exercise** covering:
- Functions and parameters
- Loops and conditionals
- `sys.argv` for CLI argument parsing
- `socket` module for network connections
- File I/O with `with open()`
- `try/except` error handling
- `if __name__ == "__main__"` pattern
- CLI design with flags (`--help`, `-h`)