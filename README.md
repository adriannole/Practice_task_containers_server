@@ -1,22 +1,22 @@
# 🐳 **Task Work: Dockerizing "Hello World" in Multiple Programming Languages** 🐳
# 🐳 **Task Work: Dockerizing the Application** 🐳

This project demonstrates how to program a simple "Hello World" application in five different programming languages. The goal is to render the output of each "Hello World" program in a single **HTML page**, showcasing the versatility of different languages. All of this is **dockerized**, making it easy to deploy and run the application across various environments.
This project aims to **dockerize** an application using five different programming languages. This makes the application portable and consistent across any environment.

---

## 💻 **Programming Languages Used**

This project includes "Hello World" programs in the following **5 programming languages**:
This project uses the following **5 programming languages**:

1. **🐍 Python**: Used for demonstrating a basic Python script that prints "Hello World" to the console.
1. **🐍 Python**: Used for the main application logic, especially for data processing and database interactions.
   
2. **🚀 Go**: A simple Go program is included to print "Hello World" on the web page, highlighting Go’s efficiency.
2. **🚀 Go**: Employed for tasks requiring high efficiency and concurrency, ideal for fast and high-performance web services.

3. **☕ Java**: A Java program is created that prints "Hello World" when run within a Docker container.
3. **☕ Java**: Used to build robust and scalable applications, particularly in enterprise environments.

4. **🌐 JavaScript**: The JavaScript version dynamically renders "Hello World" in the browser, using basic DOM manipulation.
4. **🌐 JavaScript**: Essential for frontend development, improving user interaction and making the application dynamic and responsive.

5. **💎 Ruby**: A Ruby script is used to print "Hello World" to the terminal, showcasing its simplicity.
5. **💎 Ruby**: Used for developing fast backend applications and web services, known for its simplicity and ease of use in small to medium projects.

---


@@ -24,76 +24,44 @@ This project includes "Hello World" programs in the following **5 programming la

### 🌟 **What Does the Project Do?**

The main purpose of this project is to demonstrate how "Hello World" can be implemented in different programming languages and how to render their outputs in a single HTML page. The project is **dockerized**, meaning all the programming environments and the HTML page are contained within Docker containers, allowing you to run them easily on any system.
The project provides a flexible and scalable solution for managing data, implementing features, and running applications in various environments. The application is **dockerized**, meaning the development and execution environment is contained within a container, making it easy to deploy on any system with Docker installed.

### 🛠 **Main Features:**

- **Multi-language Demonstration**: Showcases "Hello World" programs in Python, Go, Java, JavaScript, and Ruby.
- **Web Rendering**: All outputs are rendered in a single HTML page.
- **Dockerized Application**: The entire application is containerized, allowing easy deployment and scalability.
- **Microservices**: Each language and component of the application is isolated in containers, promoting independence and scalability.
- **Database**: Interacts with SQL databases to efficiently store and manage data.
- **User Interface**: Frontend interactions are implemented using JavaScript and Ruby.
- **Performance**: Go and Java are used to optimize performance and handle large volumes of data.

---

## 🐋 **Dockerizing the Project**

This project is fully **dockerized**, which means you can run it easily on any machine that has Docker installed without the need for complex environment setups.
This project is fully **dockerized**, which means you can run it easily on any machine that has Docker installed, without the need for complex environment setups.

### 🚀 **Installing Docker:**

To run this project on Docker, ensure that Docker is installed on your machine. If it isn't, you can [download Docker here](https://www.docker.com/get-started).
To run this project on Docker, make sure you have Docker installed. If not, you can [download Docker here](https://www.docker.com/get-started).

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

To get started, clone the project repository to your local machine using Git:

## Alternativa: Descargar Todas las Imágenes de una Sola Vez

git clone https://github.com/adriannole/Practice_task_containers_server.git

docker pull adrixer/trabajo_tarea
### 2. **Build the Docker Image:**

## Paso 3: Ejecutar el Contenedor Flask
docker run -p 5000:5000 adrixer/trabajo_tarea:flask
docker build -t trabajo_tarea .

## Paso 4: Acceder a la Aplicación 

http://127.0.0.1:5000/ 
### 3. **Run the Container:**
docker run -d -p 5000:5000 trabajo_tarea


## Lógica del Código 
### 4. **Verify the Container is Running:**
http://localhost:5000

def home():
    results = {
        "Lenguaje en Python": run_docker("adrixer/trabajo_tarea:python"),
        "Lenguaje en JavaScript": run_docker("adrixer/trabajo_tarea:javascript"),
        "Lenguaje en Java": run_docker("adrixer/trabajo_tarea:java"),
        "Lenguaje en Ruby": run_docker("adrixer/trabajo_tarea:ruby"),
        "Lenguaje en Go": run_docker("adrixer/trabajo_tarea:go")
     }
    return render_template('index.html', results=results)

