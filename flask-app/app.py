from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def run_docker(container_name):
    try:
        result = subprocess.check_output(["docker", "run", container_name], text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}, Code: {e.returncode}"
    
@app.route('/')
def home():
    return jsonify({
        "Python": run_docker("hola-mundo-python"),
        "JavaScript": run_docker("hola-mundo-javascript"),
        "Java": run_docker("hola-mundo-java"),
        "Ruby": run_docker("hola-mundo-ruby"),
        "Go": run_docker("hola-mundo-go")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
