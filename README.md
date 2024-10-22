
# Flask Base64 Encoder/Decoder

This is a simple Flask web application that encodes and decodes data using Base64. It provides an easy-to-use interface for users to enter data, encode it to Base64, and decode it back to its original form.

## Features

- Input data to be encoded in Base64.
- Display the encoded result.
- Decode the Base64 string back to its original form.
- Beautiful and responsive UI with CSS styling.
- Made with ❤️ and ⚡ by Arpita.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Gunicorn (for deployment)

## Requirements

- Python 3.7 or higher
- Flask
- Gunicorn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sgindeed/CropRecommend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CropRecommend
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application Locally

To run the application locally, use the following command:

```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Deployment

To deploy the application on Render:

1. Push your code to a GitHub repository.
2. Create a new web service on Render.
3. Set the build command:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the start command:

   ```bash
   gunicorn app:app
   ```

5. Configure any necessary environment variables.
6. Click on "Deploy" to launch your application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [Gunicorn](https://gunicorn.org/) - The WSGI HTTP server used for deployment.
  
