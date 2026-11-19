
# Bella Vista Salon Appointment System

## Project Description

Bella Vista Salon is a Flask web application prototype for a salon appointment system. Customers can view salon services, review service details, and access an appointment booking page. Staff can view the appointment calendar, while administrators can review available salon services.

## Technologies Used

- Python
- Flask
- HTML
- Jinja2
- Pico CSS
- Visual Studio Code

## Project Pages

| Page | Route |
|---|---|
| Home | `/` |
| Services | `/services` |
| Service Details | `/services/1` |
| Book Appointment | `/book` |
| Staff Calendar | `/calendar` |
| My Appointments | `/appointments` |
| Services Administration | `/services-admin` |

## Installation and Setup

1. Clone or download the project.
2. Open the project folder in Visual Studio Code.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

4. Install the required packages:

   ```powershell
   pip install -r requirements.txt
   ```

5. Start the Flask application:

   ```powershell
   python -m flask --app app run --debug
   ```

6. Open the following address in your browser:

   http://127.0.0.1:5000

## Current Limitations

This is a prototype using sample appointment and service data. Appointment submissions, database storage, and service editing are not implemented yet.

## Author

Student Project - EGN 475
