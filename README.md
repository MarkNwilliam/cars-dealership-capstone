# Best Cars Dealership - Full Stack Application Development Capstone

## Project Name
**Best Cars Dealership** — A responsive full-stack web application for a national
car dealership with branches across the United States. Users can browse dealerships,
view and submit reviews, filter dealerships by state, and analyze review sentiment.

## Description
This project is the capstone for the **Full Stack Software Developer Professional
Certificate**. It combines a Django back end with a React front end, a Node.js/Express
dealership and reviews microservice backed by MongoDB, a Flask-based sentiment analyzer,
and a SQLite database for car makes and models.

## Key Features
- Browse all dealerships and filter them by state
- View dealership details and customer reviews with sentiment analysis
- Register, log in, and log out
- Submit reviews for any dealership
- Admin interface to manage car makes and models
- Responsive UI built with React, Bootstrap, and custom CSS

## Technologies Used
- **Backend:** Python, Django, REST APIs
- **Frontend:** React, HTML5, CSS3, Bootstrap
- **Microservices:** Node.js, Express, Flask
- **Databases:** MongoDB, SQLite
- **DevOps:** Docker, Kubernetes, GitHub Actions (CI/CD), IBM Cloud Code Engine

## Repository Structure
```
server/
├── database/          # Node.js/Express dealership & reviews microservice (MongoDB)
├── djangoapp/         # Django app (models, views, proxy services, microservices)
├── djangoproj/        # Django project configuration
└── frontend/          # React application and static pages
```

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- MongoDB

### Run the services
1. Start the dealerships & reviews service:
   ```bash
   cd server/database
   npm install
   node app.js
   ```
2. Start the sentiment analyzer:
   ```bash
   cd server/djangoapp/microservices
   pip install -r requirements.txt
   python app.py
   ```
3. Run the Django server:
   ```bash
   cd server
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
4. Build the React frontend:
   ```bash
   cd server/frontend
   npm install
   npm run build
   ```

## Deployment
The application can be containerized with Docker and deployed on Kubernetes or
IBM Cloud Code Engine. A CI/CD pipeline is configured with GitHub Actions.

## License
Copyright IBM Corp. All Rights Reserved.
