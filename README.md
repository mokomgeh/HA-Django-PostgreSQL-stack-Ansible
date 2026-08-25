# HA-Django-PostgreSQL-stack-Ansible
This is a 4-node, highly available web stack built and automated with Ansible on RockyLinux 9. It's a hands-on project (my first after my RHCE certification) applying my RHCSA / RHCE material to a real world multi-tier architecture.
The nodes are:
- 1 Load balancer (HAProxy)
- 2 Webservers (Django application + Nginx and Gunicorn)
- 1 PostgreSQL database

# Why I am building this project
I want to prove to myself that I can apply the skills I learned while studying for my certification to build a real-life working project. I also want some technical visibility to companies and hiring managers  

# Project Architecture
<img width="252" height="422" alt="Project structure" src="https://github.com/user-attachments/assets/8c63d22b-18d1-4235-bdcf-b6ab54d16244" />

# Stack
1. OS                    -      RockyLinux 9 
2. Provisioning          -      Ansible (Automation)
3. Load Balancer         -      HAProxy (Web traffic distribution)
4. App Server            -      Django (Web app backend)
5. Web Server            -      Nginx (Reverse proxy)
6. Database              -      PostgreSQL (Database Storage)
7. Security              -      SELinux & Firewalld (Mandatory Access control)

# Project Tasks
1. VM provisioning and ansible base configuration (ansible.cfg file, inventories and ssh connection)
2. ansible node general configurations
3. database node configuration (Posgresql installation and configuration.)
4. webserver nodes configuration (django and nginx setup and configuration)
5. load balancer configuration (configure HAProxy)
6. testing