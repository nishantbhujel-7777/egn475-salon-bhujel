# Bella Vista Salon – User Stories and Acceptance Criteria

**Project:** Bella Vista Salon Appointment Booking System  
**Platform:** Flask Web Application  
**Location:** Coral Gables, Florida  
**Assignment:** EGN475 – Week 2 Assignment 1

## 1. Introduction

Bella Vista Salon is a web-based appointment booking application designed to make it easier for clients to explore salon services and schedule appointments. The application will also help salon staff manage appointments and maintain accurate service information.

This backlog contains user stories for two main personas: salon clients and salon staff members. Each story includes two Given/When/Then acceptance criteria and a priority level. The stories will guide the development and testing of the Flask prototype.

## 2. User Personas

### Persona 1: Salon Client

A salon client is a person who wants to explore available salon services, view appointment availability, book appointments, and manage existing reservations. The client needs a simple and convenient booking experience.

### Persona 2: Salon Staff Member

A salon staff member is responsible for managing customer appointments, updating appointment statuses, and maintaining salon service information. Staff members need an organized system to reduce manual work and prevent scheduling mistakes.

## 3. User Stories and Acceptance Criteria

### US-01: View Available Salon Services

**Priority: MUST HAVE**

**User Story:**

As a salon client, I want to view the available salon services so that I can choose a service that meets my needs.

**Acceptance Criteria:**

1. Given that the salon has available services, when I open the services page, then the system displays the service names, descriptions, and prices.

2. Given that no salon services are currently available, when I open the services page, then the system displays a message explaining that no services are currently available.

### US-02: View Available Appointment Times

**Priority: MUST HAVE**

**User Story:**

As a salon client, I want to view available appointment times for a selected date so that I can choose a convenient time.

**Acceptance Criteria:**

1. Given that appointment times are available on a selected date, when I select that date, then the system displays the available appointment times.

2. Given that a particular appointment time is already booked, when I view the available times for that date, then the booked time is not displayed as available.

### US-03: Book a Salon Appointment

**Priority: MUST HAVE**

**User Story:**

As a salon client, I want to book an appointment for a selected service and time so that I can receive salon services at my preferred time.

**Acceptance Criteria:**

1. Given that I have selected a valid service, date, and available time, when I submit the booking form, then the system creates the appointment and displays a booking confirmation.

2. Given that I have not selected a required service or appointment time, when I submit the booking form, then the system displays a validation message and does not create the appointment.

### US-04: View My Appointments

**Priority: MUST HAVE**

**User Story:**

As a salon client, I want to view my scheduled appointments so that I can keep track of my upcoming salon visits.

**Acceptance Criteria:**

1. Given that I have existing appointments, when I open the My Appointments page, then the system displays my appointment dates, times, services, and statuses.

2. Given that I do not have any appointments, when I open the My Appointments page, then the system displays a message indicating that no appointments have been scheduled.

### US-05: Cancel an Appointment

**Priority: SHOULD HAVE**

**User Story:**

As a salon client, I want to cancel an upcoming appointment so that I can manage changes in my schedule.

**Acceptance Criteria:**

1. Given that I have an upcoming appointment, when I select the cancel option and confirm my decision, then the system updates the appointment status to canceled.

2. Given that an appointment has already been completed or canceled, when I attempt to cancel it again, then the system prevents the action and displays an appropriate message.

### US-06: View the Staff Appointment Calendar

**Priority: MUST HAVE**

**User Story:**

As a salon staff member, I want to view the salon appointment calendar so that I can monitor scheduled client visits.

**Acceptance Criteria:**

1. Given that appointments have been scheduled, when I open the staff calendar, then the system displays the appointments with their dates, times, services, and statuses.

2. Given that no appointments are scheduled for a selected date, when I view that date on the calendar, then the system displays an empty schedule message.

### US-07: Update Appointment Status

**Priority: MUST HAVE**

**User Story:**

As a salon staff member, I want to update an appointment's status so that I can keep appointment records accurate.

**Acceptance Criteria:**

1. Given that an appointment exists, when an authorized staff member changes its status to confirmed or completed, then the system saves and displays the updated status.

2. Given that a regular client attempts to access the staff appointment management function, when the client tries to update an appointment status, then the system denies access and displays an authorization message.

### US-08: Manage Salon Services

**Priority: SHOULD HAVE**

**User Story:**

As a salon staff member, I want to add or update salon service information so that clients can see accurate service details and prices.

**Acceptance Criteria:**

1. Given that an authorized staff member enters a valid service name, description, and price, when they save the service, then the system adds or updates the service information.

2. Given that a staff member submits a service without a required name or valid price, when they save the service, then the system displays a validation error and does not save the invalid information.

### US-09: View Appointment Confirmation

**Priority: COULD HAVE**

**User Story:**

As a salon client, I want to receive a confirmation message after booking an appointment so that I know my reservation was successfully recorded.

**Acceptance Criteria:**

1. Given that I submit a valid appointment booking, when the system successfully saves the appointment, then it displays a confirmation message containing the appointment details.

2. Given that the appointment cannot be saved because of a system error, when I submit the booking form, then the system displays an error message instead of showing a false confirmation.

### US-10: Search for Salon Services

**Priority: COULD HAVE**

**User Story:**

As a salon client, I want to search for a salon service by name so that I can quickly find the service I need.

**Acceptance Criteria:**

1. Given that salon services are available, when I enter a matching service name in the search field, then the system displays the matching services.

2. Given that I enter a service name that does not match any available service, when I submit the search, then the system displays a message indicating that no matching services were found.

## 4. Priority Summary

| Priority | Stories | Total |
|---|---|---:|
| Must Have | US-01, US-02, US-03, US-04, US-06, US-07 | 6 |
| Should Have | US-05, US-08 | 2 |
| Could Have | US-09, US-10 | 2 |

The six must-have stories define the core prototype. They provide the essential functionality for viewing services, checking availability, booking appointments, viewing bookings, and managing appointments through staff access.

The should-have stories improve appointment management and service administration. The could-have stories provide additional convenience and can be implemented if time permits.

## 5. INVEST Review

The INVEST principles help evaluate whether user stories are suitable for Agile development.

- **Independent:** Each story represents a distinct piece of functionality.
- **Negotiable:** The implementation details can be discussed and adjusted during development.
- **Valuable:** Each story provides a benefit to salon clients or staff.
- **Estimable:** Each story is small enough to estimate development effort.
- **Small:** Each story focuses on one primary goal.
- **Testable:** Each story has two acceptance criteria that can be verified.

The backlog was organized to keep each story focused on one user goal. The acceptance criteria also include validation errors, unavailable appointment times, empty results, and unauthorized access.

## 6. Questions and Answers

### Question 1: Which story did you split into smaller stories, and why?

I split the appointment management functionality into separate user stories. Initially, viewing appointments, canceling appointments, and updating appointment statuses could have been included in one large story.

However, these activities have different purposes and require different actions and testing. I separated them into viewing appointments (US-04), canceling appointments (US-05), viewing the staff calendar (US-06), and updating appointment statuses (US-07).

This makes the stories easier to develop, estimate, and test individually. It also allows the prototype to be developed incrementally.

### Question 2: Which story was hardest to write acceptance criteria for? What made it hard?

The appointment booking story (US-03) was the hardest to write acceptance criteria for because several conditions must be satisfied before an appointment can be successfully created.

The system must check that the client selected a valid service, date, and available appointment time. It must also prevent incomplete submissions and avoid creating duplicate bookings for the same appointment time.

Writing these acceptance criteria required considering both successful bookings and possible errors. I wanted the criteria to be specific enough that I could test them during Flask development.

## 7. AI Log – GitHub Copilot Review

### Review Prompt

I used the following prompt in GitHub Copilot Chat:

> Here are my user stories for a Flask prototype. Check each one against INVEST and tell me which are too big, vague or not testable. Do not rewrite them; list problems only.

### Copilot Review Results

**Important:** Insert the actual feedback returned by your GitHub Copilot Chat here. The following table is a decision log template, not a claim that Copilot has already produced these comments.

| Copilot feedback / flagged story | Decision | Explanation |
|---|---|---|
| US-03: Appointment booking may involve several conditions and validation steps. | Accepted if flagged | I kept the story focused on booking one appointment and made its acceptance criteria specific to required fields and availability. |
| US-05: Appointment cancellation should clarify which appointments can be canceled. | Accepted if flagged | I specified that only upcoming appointments can be canceled and included protection against repeated cancellation. |
| US-07: Staff appointment management needs role-based access. | Accepted if flagged | I added an authorization condition to prevent regular clients from changing appointment statuses. |
| US-09: Confirmation should distinguish successful bookings from failed bookings. | Accepted if flagged | I included separate success and error conditions so that the system does not display a false confirmation. |

### Review Decision

I reviewed the Copilot suggestions instead of automatically accepting every recommendation. I agreed with feedback that made stories more specific, independent, and testable. I would reject suggestions that introduced unnecessary features or expanded the project beyond the original Bella Vista Salon requirements.

The final backlog remains focused on the essential appointment booking and staff management functions.

## 8. Conclusion

The Bella Vista Salon user story backlog provides a foundation for developing the Flask prototype. It identifies the needs of both salon clients and staff members and defines measurable acceptance criteria for each feature.

The must-have stories will guide the initial development phase, while the should-have and could-have stories provide opportunities for future improvements. The INVEST principles and GitHub Copilot review help ensure that the stories are clear, manageable, and testable.

