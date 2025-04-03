from flask import Flask, request

app = Flask(__name__)


@app.route("/hello", methods=['GET'])
def hello_world() -> str:
    firstname: str = request.args.get('firstname', 'Anonymous')
    lastname: str = request.args.get('lastname')

    return f'Hello {firstname} {lastname}!'


if __name__ == "__main__":
    app.run(debug=True)
