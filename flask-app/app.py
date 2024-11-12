from flask import Flask, render_template
import subprocess
import shutil

app = Flask(__name__)

def run_docker(container_name):
    if not shutil.which("docker"):
        return "Error: Docker no está disponible en este contenedor."
    try:
        result = subprocess.check_output(["docker", "run", container_name], text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}, Code: {e.returncode}"

@app.route('/')
def home():
    results = {
        "Python": run_docker("hola-mundo-python"),
        "JavaScript": run_docker("hola-mundo-javascript"),
        "Java": run_docker("hola-mundo-java"),
        "Ruby": run_docker("hola-mundo-ruby"),
        "Go": run_docker("hola-mundo-go")
    }
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


#PS C:\Users\Adrian Nole\Documents\GitHub\Practice_task_containers_server\flask-app> docker run -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock flask-app1