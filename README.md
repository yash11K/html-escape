# XML Formatter Plus 🎨

A Python package that formats and beautifies XML strings with HTML entity handling, complete with logging and emoji support! ✨

## Features 🌟

- HTML entity decoding and encoding
- XML beautification and formatting
- Java-style escape sequence handling
- Detailed logging with emojis
- Command-line interface
- Supports both direct input and file processing

## Installation 📦

You can install the package directly from GitHub using pip:

```bash
pip install git+https://github.com/YashKabra/decoder-package.git
```

## Usage 💻

### Command Line Interface

```bash
# Basic usage
xml-formatter "your_xml_string_here"

# With verbose logging
xml-formatter -v "your_xml_string_here"

# Interactive mode (if no input string provided)
xml-formatter
```

### Python API

```python
from xml_formatter import format_input

# Format your XML string
escaped_output, formatted_output = format_input("<your>xml string</your>")
print(formatted_output)
```

## Output 📝

The formatter provides two types of output:
2. Formatted Output: Beautified XML with proper indentation

## License 📄

MIT License 