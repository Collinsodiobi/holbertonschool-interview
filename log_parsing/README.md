# Log Parsing

This project contains a Python script that reads log entries from standard input and computes metrics.

## Requirements

* Ubuntu 14.04 LTS
* Python 3.4.3
* PEP 8 style

## Files

* `0-stats.py` - Reads stdin line by line, computes the total file size, and counts occurrences of specific HTTP status codes.

## Usage

```bash
./0-generator.py | ./0-stats.py
```

The script prints:

* Total file size processed
* Number of occurrences of each valid status code

Statistics are displayed every 10 lines and when the program is interrupted.
