from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

# function to fetch hostname and ip
def fetch_details():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@app.route("/")
def hello_flask():
    return "<p>Hello Flask</p>"

@app.route("/health")
def health():  
    return jsonify(
        status = "UP"
    )

# rendering dynamic template
@app.route("/details")
def details():
    hostname, ip = fetch_details()
    return render_template('index.html', HOST_NAME = hostname, HOST_IP = ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)