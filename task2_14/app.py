from flask import Flask

app = Flask(__name__)

# Это позволит использовать и HTTP, и HTTPS
if __name__ == '__main__':
    app.run(debug=True, ssl_context=('server.crt', 'server.key'))
