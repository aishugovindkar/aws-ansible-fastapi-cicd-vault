# AWS FastAPI Deployment with Ansible, CI/CD & HashiCorp Vault

![CI/CD](https://github.com/aishugovindkar/aws-ansible-fastapi-cicd-vault/actions/workflows/deploy.yaml/badge.svg?branch=main)


This project demonstrates an end-to-end DevOps pipeline where a containerized **FastAPI** application is automatically deployed to an **AWS EC2** instance using **GitHub Actions** (CI/CD), **Ansible** for provisioning, and **HashiCorp Vault** for secret management.

---

## 🚀 Tech Stack Used

| Tool              | Purpose                                   |
|-------------------|-------------------------------------------|
| **AWS EC2**        | Host the backend application              |
| **FastAPI**        | Lightweight Python web framework          |
| **Docker**         | Containerize the application              |
| **Ansible**        | Provision EC2, install Docker, deploy app |
| **GitHub Actions** | CI/CD pipeline on push to `main`          |
| **Vault**          | Secure secrets retrieval inside container |
| **CloudWatch**     | Monitor EC2 instance metrics              |

---

## 📦 Project Flow

1. ✅ **Push to GitHub** → triggers GitHub Actions
2. 📁 **App folder is copied** to AWS EC2 via SSH
3. ⚙️ **Ansible** builds Docker image & runs the container
4. 🔐 **FastAPI container** securely pulls a secret from **Vault**
5. 📊 **CloudWatch** monitors EC2 CPU/memory metrics

---

## 📁 Project Structure

```

aws-ansible-fastapi-cicd-vault/
├── app/                      # FastAPI source code + Dockerfile
├── ansible/
│   ├── inventory.ini         # Ansible inventory with localhost
│   ├── playbook.yml          # Provisioning + deployment steps
│   └── vault\_token.txt       # Vault token (used locally)
├── .github/workflows/
│   └── deploy.yaml           # CI/CD GitHub Actions workflow
├── .gitignore
└── README.md

```

---

## 🔐 Vault Integration

- Installed Vault on EC2
- Stored and accessed a secret inside Vault
- Shared the EC2 network namespace with Docker container
- App securely fetched the secret using Python `hvac` client

---

## 🧪 How to Test

1. Open your app in the browser:
```

http\://\<YOUR\_EC2\_PUBLIC\_IP>:5000

```
2. On pushing to `main`, your app is rebuilt and redeployed live!

---

## 📸 Screenshots

_Add here if you captured any screenshots — monitoring, workflow success, or logs._

---

## 🙋‍♀️ Author

**Aishwarya Govindkar**  
DevOps Engineer | Cloud Enthusiast | Python Automation  
[GitHub Profile](https://github.com/aishugovindkar)

---

## 🌟 What I Learned

- ✅ How to automate EC2 deployments using Ansible
- ✅ Built a production-style CI/CD pipeline with GitHub Actions
- ✅ Used Vault securely inside containers
- ✅ Solved real-world deployment issues with Docker, SSH & Git

---

## ✅ Future Improvements

- Add NGINX reverse proxy for secure HTTPS
- Use GitHub Actions Matrix builds
- Set up dynamic DNS / domain mapping
- Add monitoring dashboard with Prometheus + Grafana


