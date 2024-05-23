# Base64 Encoding and Decoding

This script demonstrates how to encode and decode data using Base64 in Python. Base64 is commonly used to encode binary data as ASCII characters, making it easier to transmit and store.

## Features

- **Encoding**: Converts a string into its Base64 encoded form.
- **Decoding**: Converts a Base64 encoded string back to its original form.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository or download the script.**

2. **Run the script**:

    ```sh
    python script_name.py
    ```

3. **Follow the on-screen prompt to enter the data you want to encode.** The script will display the Base64 encoded result, and then decode it back to the original string to verify the process.

## Example

Here's an example interaction with the script:

```sh
Enter the data to encode: Hello, World!
Encoded: SGVsbG8sIFdvcmxkIQ==
Decoded: Hello, World!


- **Import base64**: Imports the base64 module which contains methods for encoding and decoding.
- **main() function**:
  - Prompts the user to enter data.
  - Encodes the input data using Base64.
  - Prints the encoded string.
  - Decodes the encoded string back to the original data.
  - Prints the decoded string to verify it matches the original input.
- **Script execution check**: Ensures the `main()` function runs when the script is executed directly.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.

---

Happy encoding and decoding!
