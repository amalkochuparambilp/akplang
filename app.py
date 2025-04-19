from flask import Flask, request, jsonify, render_template
import io
import contextlib

app = Flask(__name__)

def akp_malang(code):
    code = code.replace("enkil","if")
    code = code.replace("allel","else")
    code = code.replace("parayo","print")
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        try:
            exec(code)
        except Exception as e:
            return str(e)
        return output.getvalue()
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=['POST'])
def run():
    data = request.get_json()
    code = data.get("code","")
    output = akp_malang(code)
    return jsonify({"output":output})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1000)