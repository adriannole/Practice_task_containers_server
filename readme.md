# 🐳 **Task Work: Dockerizing "Hello World" in Multiple Programming Languages** 🐳

This project demonstrates how to program a simple "Hello World" application in five different programming languages. The goal is to render the output of each "Hello World" program in a single **HTML page**, showcasing the versatility of different languages. All of this is **dockerized**, making it easy to deploy and run the application across various environments.

---

## 💻 **Programming Languages Used**

This project includes "Hello World" programs in the following **5 programming languages**:

1. **🐍 Python**: Used for demonstrating a basic Python script that prints "Hello World" to the console.
   
2. **🚀 Go**: A simple Go program is included to print "Hello World" on the web page, highlighting Go’s efficiency.

3. **☕ Java**: A Java program is created that prints "Hello World" when run within a Docker container.

4. **🌐 JavaScript**: The JavaScript version dynamically renders "Hello World" in the browser, using basic DOM manipulation.

5. **💎 Ruby**: A Ruby script is used to print "Hello World" to the terminal, showcasing its simplicity.

---

## 📦 **Project Overview**

### 🌟 **What Does the Project Do?**

The main purpose of this project is to demonstrate how "Hello World" can be implemented in different programming languages and how to render their outputs in a single HTML page. The project is **dockerized**, meaning all the programming environments and the HTML page are contained within Docker containers, allowing you to run them easily on any system.

### 🛠 **Main Features:**

- **Multi-language Demonstration**: Showcases "Hello World" programs in Python, Go, Java, JavaScript, and Ruby.
- **Web Rendering**: All outputs are rendered in a single HTML page.
- **Dockerized Application**: The entire application is containerized, allowing easy deployment and scalability.

---

## 🐋 **Dockerizing the Project**

This project is fully **dockerized**, which means you can run it easily on any machine that has Docker installed without the need for complex environment setups.

### 🚀 **Installing Docker:**

To run this project on Docker, ensure that Docker is installed on your machine. If it isn't, you can [download Docker here](https://www.docker.com/get-started).

---

## 🔨 **Usage Instructions**


# Instrucciones para Ejecutar el Proyecto Docker

Este proyecto utiliza Docker para ejecutar contenedores de diferentes lenguajes de programación. A continuación, te proporcionamos los pasos detallados para ponerlo en funcionamiento.

## Paso 1: Accede al Docker Hub

Accede al siguiente enlace para ver todos los tags disponibles de la imagen Docker:

[https://hub.docker.com/r/adrixer/trabajo_tarea](https://hub.docker.com/r/adrixer/trabajo_tarea)

Aquí podrás ver todos los tags disponibles para cada lenguaje de programación.

## Paso 2: Descargar las Imágenes Docker


Es necesario descargar cada tag para que los contenedores funcionen correctamente. Abre Docker Desktop y usa la terminal para ejecutar los siguientes comandos en el orden indicado:


docker pull adrixer/trabajo_tarea:javascript
docker pull adrixer/trabajo_tarea:python
docker pull adrixer/trabajo_tarea:ruby
docker pull adrixer/trabajo_tarea:java
docker pull adrixer/trabajo_tarea:go
docker pull adrixer/trabajo_tarea:flask


## Alternativa: Descargar Todas las Imágenes de una Sola Vez

docker pull adrixer/trabajo_tarea

## Paso 3: Ejecutar el Contenedor Flask
docker run -p 5000:5000 adrixer/trabajo_tarea:flask

## Paso 4: Acceder a la Aplicación 

http://127.0.0.1:5000/ 


## Lógica del Código 

def home():
    results = {
        "Lenguaje en Python": run_docker("adrixer/trabajo_tarea:python"),
        "Lenguaje en JavaScript": run_docker("adrixer/trabajo_tarea:javascript"),
        "Lenguaje en Java": run_docker("adrixer/trabajo_tarea:java"),
        "Lenguaje en Ruby": run_docker("adrixer/trabajo_tarea:ruby"),
        "Lenguaje en Go": run_docker("adrixer/trabajo_tarea:go")
    }
    return render_template('index.html', results=results)

