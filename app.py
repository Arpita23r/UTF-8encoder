from flask import Flask, request, render_template_string
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    encoded_str = ""
    decoded_str = ""
    if request.method == 'POST':
        data = request.form.get('data')

        if data:
            encoded = base64.b64encode(data.encode("utf-8"))
            encoded_str = encoded.decode("utf-8")
            decoded = base64.b64decode(encoded_str)
            decoded_str = decoded.decode("utf-8")

    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Base64 Encoder/Decoder</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                margin-bottom: 20px;
                color: #4a4e69;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            input[type="text"] {
                padding: 10px;
                border: 2px solid #4a4e69;
                border-radius: 5px;
                margin-bottom: 10px;
                width: 250px;
                transition: border-color 0.3s;
            }
            input[type="text"]:focus {
                border-color: #9a8c98;
                outline: none;
            }
            input[type="submit"] {
                background-color: #9a8c98;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                transition: background-color 0.3s, transform 0.2s;
            }
            input[type="submit"]:hover {
                background-color: #4a4e69;
                transform: translateY(-2px);
            }
            .result {
                margin-top: 20px;
                padding: 10px;
                border: 1px solid #4a4e69;
                border-radius: 5px;
                background-color: #ffffff;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
                width: 300px;
                text-align: center;
            }
            footer {
                margin-top: 30px;
                font-size: 14px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <h1>Base64 Encoder/Decoder</h1>
        <form method="POST">
            <label for="data">Enter the data to encode:</label><br>
            <input type="text" id="data" name="data" required>
            <input type="submit" value="Encode">
        </form>

        {% if encoded %}
            <div class="result">
                <h2>Encoded:</h2>
                <p>{{ encoded }}</p>
            </div>
        {% endif %}
        
        {% if decoded %}
            <div class="result">
                <h2>Decoded:</h2>
                <p>{{ decoded }}</p>
            </div>
        {% endif %}
        
        <footer>
            Made with ❤️ and ⚡ by Arpita
        </footer>
    </body>
    </html>
    '''
    
    return render_template_string(template, encoded=encoded_str, decoded=decoded_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
