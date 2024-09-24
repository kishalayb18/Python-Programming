from flask import Flask, jsonify

app = Flask(__name__)

# First API that generates some data
@app.route('/api1', methods=['GET'])
def api1():
    data = {"message": "This is data from API 1"}
    return jsonify(data)

# Second API that consumes data from the first API using test_client()
@app.route('/api2', methods=['GET'])
def api2():
    # Use test_client to call API 1
    with app.test_client() as client:
        response = client.get('/api1')
        data_from_api1 = response.get_json()

    # Use the data from API 1 in API 2
    new_data = {"message": "This is API 2 using data from API 1", "api1_data": data_from_api1}
    return jsonify(new_data)

if __name__ == '__main__':
    app.run(debug=True)
