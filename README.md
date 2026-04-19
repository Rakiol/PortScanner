# PortScanner 🔍

A simple Python port scanner built to practice core Python concepts like functions, loops, sockets, and file I/O.

## Features

- Scan a **single port** or a **range of ports**
- Saves all open ports to `openPorts.txt`
- Interactive CLI — enter target IP/domain and port range at runtime
- Timeout handling for fast scanning

## Requirements

- Python 3.x
- No external libraries needed — uses only the built-in `socket` module

## Usage

```bash
python main.py
```

You will be prompted to:
1. Enter an IP address or domain (e.g. `127.0.0.1` or `scanme.nmap.org`)
2. Choose between single port scan (`1`) or range scan (`2`)
3. Enter the port number or range

## Example

```
Please write IP or Domain
> scanme.nmap.org
Please write 1 = Single Port or 2 = Range
> 2
Write Start Range
> 1
Write End Range
> 100

Port 22 is OPEN
Port 80 is OPEN
...
Finished
```

Open ports are saved to `openPorts.txt` in the same directory.

## Project Structure

```
PortScanner/
├── main.py          # Main scanner with scan_port() and scan_range()
├── connect.py       # Socket connection experiments
├── echo-client.py   # Echo client example
├── echo-server.py   # Echo server example
└── openPorts.txt    # Output file (auto-generated)
```

## ⚠️ Legal Notice

Only scan systems you own or have explicit permission to scan. Unauthorized port scanning may be illegal in your country.

## Purpose

This project was built as a **Python learning exercise** covering:
- `socket` module
- Functions and return values
- Loops and conditionals
- File I/O with `open()`
- User input handling
- `if __name__ == "__main__"` pattern
