# Quick-Stock-Checker

  A dockerized simple app to check selected stocks.  Results contains information on previous closing value, current opening value, today's high and today's low for each selected stock.
  
## **Built with:**

* [![Python](https://img.shields.io/badge/python-3.8.3-blue.svg)](https://www.python.org/downloads/release/python-383/)

## **Getting Started**

### **Clone repository**

    $ git clone https://github.com/Xuehong-pdx/Quick-Stock-Checker/.git

* Navigate to the project folder

      $ cd quick_stock
      
### **Docker**

* **Download Docker Desktop:** https://www.docker.com/get-started. There are versions available for Linux, Max, and Windows. **What is Docker?** Docker is a platform for building, running, and shipping applications. Docker packages up an application with everything it needs and allows an app to run and function the same way on any user's local machine.

* **Create a Docker ID:** https://hub.docker.com/signup

* **Login to Docker:** Enter Docker credentials when prompt.
      
      $ docker login
      
* **Build Docker Image:** 
      
      $ docker build -t quick_stock .
      
* **Run program/Docker Container:**
      
      $ docker run -it quick_stock
      
