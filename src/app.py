from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

def fetchDetails():
    hostname = request.host.split(':')[0]  # Get the hostname from the request
    ip_address = request.remote_addr  # Get the client's IP address from the request
    return str(hostname), str(ip_address)

@app.route("/")
def hello_world():
    return "<h1>Hello, Vinay Reddy You made that your application Run in Docker Container Cheers! !</h1>" 

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)