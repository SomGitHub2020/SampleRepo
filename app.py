from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    if request.method == 'GET':
        return jsonify({'Status': "Successfully Connected"})


if __name__ == '__main__':
    app.run()