from flask import Flask, request, jsonify
import requests

app=Flask(__name__)

@app.route("/validate_status", methods=["GET"])
def validate_status():
    url=request.args.get('url')

    if not url:
        return "missing parameters"
    
    try:
        response=requests.get(url)
        status_code=response.status_code
        return jsonify({"url":url,"status code":status_code})
    except Exception as e:
        return "response not receive" + str(e)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)