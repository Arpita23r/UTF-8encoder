import base64

def main():
    data = input("Enter the data to encode: ")
    
    encoded = base64.b64encode(data.encode("utf-8"))
    encoded_str = encoded.decode("utf-8")
    print(f"Encoded: {encoded_str}")
    
    decoded = base64.b64decode(encoded_str)
    decoded_str = decoded.decode("utf-8")
    print(f"Decoded: {decoded_str}")

if __name__ == "__main__":
    main()