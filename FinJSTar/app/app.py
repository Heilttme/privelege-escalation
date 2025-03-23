import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_code = request.form.get("code", "")
        if user_code:
            try:
                safe_code = f'console.log(eval({user_code}))'
                output = subprocess.check_output(
                    ["node", "-e", safe_code],
                    stderr=subprocess.STDOUT,
                    text=True
                )
                result = output.strip()
            except subprocess.CalledProcessError as e:
                result = f'Ошибка выполнения: {e.output}'
    return render_template("index.html", result=str(result))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

