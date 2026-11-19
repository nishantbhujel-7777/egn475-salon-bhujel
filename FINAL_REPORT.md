# EGN 475 – Week 3 – Assignment 3.1
## Build Every Screen as a Flask Page

**Project:** Bella Vista Salon Appointment System  
**Student:** Nishant Bhujel
**Course:** EGN 475  
**Date:** November 19, 2026

## 1. Project Overview

For this assignment, I developed a Flask web application prototype for Bella Vista Salon, a salon appointment system. The application allows customers to view salon services, review service details, and access an appointment booking page. Staff can view scheduled appointments, and administrators can review the available salon services.

## 2. Technologies Used

- Python
- Flask
- HTML
- Jinja2
- Pico CSS
- Visual Studio Code
- Git and GitHub

## 3. Application Pages and Routes

The application contains the following pages:

| Page | Flask Route | Description |
|---|---|---|
| Home | `/` | Introduces Bella Vista Salon |
| Services | `/services` | Displays available salon services |
| Service Details | `/services/<service_id>` | Displays details about an individual service |
| Book Appointment | `/book` | Provides an appointment booking form |
| Staff Calendar | `/calendar` | Displays scheduled appointments |
| My Appointments | `/appointments` | Displays appointment history |
| Services Administration | `/services-admin` | Displays salon service information for administrators |

## 4. Flask and Jinja Implementation

I used Flask to create the application routes and render the HTML templates. I used Jinja template inheritance to share a common navigation bar and page layout through `base.html`.

I also used Jinja loops to display salon services and appointment records. Conditional statements display different messages depending on whether records are available.

The service detail route uses an integer URL parameter to identify a service. If a service does not exist, the application returns a 404 error.

## 5. Testing

I tested the application in a web browser using the Flask development server.

The following pages were tested:

1. Home page
2. Services page
3. Service details page
4. Book appointment page
5. Staff calendar page
6. My appointments page
7. Services administration page
8. Invalid service URL to test the 404 response

Screenshots of the tested pages are included with this submission.

## 6. Current Limitations

The application currently uses sample data. Appointment booking does not save information to a database. Administrative service changes are not implemented. These features can be added in future development.

## 7. Conclusion

This assignment helped me understand how to build a Flask application using routes, templates, and Jinja. I learned how to organize a project, reuse a common page layout, display dynamic sample data, and test application routes.

The completed project provides a working prototype of the Bella Vista Salon appointment system.
