# 🐳 **Task Work: Dockerizing the Application** 🐳

This project aims to **dockerize** an application using five different programming languages. This makes the application portable and consistent across any environment.

---

## 💻 **Programming Languages Used**

This project uses the following **5 programming languages**:

1. **🐍 Python**: Used for the main application logic, especially for data processing and database interactions.
   
2. **🚀 Go**: Employed for tasks requiring high efficiency and concurrency, ideal for fast and high-performance web services.

3. **☕ Java**: Used to build robust and scalable applications, particularly in enterprise environments.

4. **🌐 JavaScript**: Essential for frontend development, improving user interaction and making the application dynamic and responsive.

5. **💎 Ruby**: Used for developing fast backend applications and web services, known for its simplicity and ease of use in small to medium projects.

---

## 📦 **Project Overview**

### 🌟 **What Does the Project Do?**

The project provides a flexible and scalable solution for managing data, implementing features, and running applications in various environments. The application is **dockerized**, meaning the development and execution environment is contained within a container, making it easy to deploy on any system with Docker installed.

### 🛠 **Main Features:**
- **Microservices**: Each language and component of the application is isolated in containers, promoting independence and scalability.
- **Database**: Interacts with SQL databases to efficiently store and manage data.
- **User Interface**: Frontend interactions are implemented using JavaScript and Ruby.
- **Performance**: Go and Java are used to optimize performance and handle large volumes of data.

---

## 🐋 **Dockerizing the Project**

This project is fully **dockerized**, which means you can run it easily on any machine that has Docker installed, without the need for complex environment setups.

### 🚀 **Installing Docker:**
To run this project on Docker, make sure you have Docker installed. If not, you can [download Docker here](https://www.docker.com/get-started).

---

## 🔨 **Usage Instructions**

### 1. **Clone the Repository:**

To get started, clone the project repository to your local machine using Git:

```bash
git clone https://github.com/adriannole/Practice_task_containers_server.git

### 2. **Build the Docker Image:**

docker build -t trabajo_tarea .


### 3. **Run the Container:**
docker run -d -p 5000:5000 trabajo_tarea


### 4. **Verify the Container is Running:**
http://localhost:5000


