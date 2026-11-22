
import os
import db

from flask import (
    Flask,
    render_template,
    abort,
    request,
    redirect,
    url_for
)

app = Flask(__name__)

# -----------------------------------
# DATABASE CONFIGURATION
# -----------------------------------

app.config["DATABASE"] = os.path.join(
    app.instance_path, "salon.sqlite"
)

os.makedirs(app.instance_path, exist_ok=True)

db.init_app(app)


# -----------------------------------
# SAMPLE SALON SERVICES
# Used by existing Week 3 pages
# -----------------------------------

SAMPLE_SERVICES = [
    {
        "id": 1,
        "name": "Women's Haircut",
        "category": "Hair",
        "price_cents": 4500,
        "duration": 45,
        "description": "Professional haircut and styling."
    },
    {
        "id": 2,
        "name": "Men's Haircut",
        "category": "Hair",
        "price_cents": 2500,
        "duration": 30,
        "description": "Classic men's haircut and grooming."
    },
    {
        "id": 3,
        "name": "Hair Coloring",
        "category": "Hair",
        "price_cents": 8500,
        "duration": 120,
        "description": "Professional hair coloring service."
    },
    {
        "id": 4,
        "name": "Manicure",
        "category": "Nails",
        "price_cents": 3000,
        "duration": 40,
        "description": "Nail shaping and polish."
    },
    {
        "id": 5,
        "name": "Pedicure",
        "category": "Nails",
        "price_cents": 4000,
        "duration": 50,
        "description": "Relaxing foot and nail treatment."
    },
    {
        "id": 6,
        "name": "Facial Treatment",
        "category": "Skincare",
        "price_cents": 6000,
        "duration": 60,
        "description": "Refreshing facial skincare treatment."
    }
]


# -----------------------------------
# STAFF CALENDAR SAMPLE DATA
# -----------------------------------

SAMPLE_CALENDAR = [
    {
        "id": 1,
        "client": "Emma Johnson",
        "service": "Women's Haircut",
        "date": "2026-11-20",
        "time": "10:00 AM",
        "staff": "Maria",
        "status": "Confirmed"
    },
    {
        "id": 2,
        "client": "Sophia Williams",
        "service": "Manicure",
        "date": "2026-11-20",
        "time": "11:30 AM",
        "staff": "Jessica",
        "status": "Pending"
    },
    {
        "id": 3,
        "client": "Olivia Brown",
        "service": "Hair Coloring",
        "date": "2026-11-20",
        "time": "02:00 PM",
        "staff": "Maria",
        "status": "Confirmed"
    }
]


# -----------------------------------
# CUSTOMER APPOINTMENT HISTORY
# -----------------------------------

SAMPLE_APPOINTMENTS = [
    {
        "id": 1,
        "service": "Women's Haircut",
        "date": "2026-11-15",
        "time": "10:00 AM",
        "staff": "Maria",
        "status": "Completed"
    },
    {
        "id": 2,
        "service": "Manicure",
        "date": "2026-11-18",
        "time": "01:00 PM",
        "staff": "Jessica",
        "status": "Confirmed"
    },
    {
        "id": 3,
        "service": "Facial Treatment",
        "date": "2026-11-22",
        "time": "03:00 PM",
        "staff": "Maria",
        "status": "Pending"
    }
]


# -----------------------------------
# HOME PAGE
# -----------------------------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        services=SAMPLE_SERVICES
    )


# -----------------------------------
# SERVICES LIST PAGE
# READ FROM SQLITE DATABASE
# -----------------------------------

@app.route("/services")
def services():

    services = db.get_db().execute(
        """
        SELECT id, name, duration_minutes, price_cents
        FROM services
        WHERE active = 1
        ORDER BY name
        """
    ).fetchall()

    return render_template(
        "services.html",
        services=services
    )


# -----------------------------------
# SERVICE DETAIL PAGE
# READ ONE SERVICE FROM DATABASE
# -----------------------------------

@app.route("/services/<int:service_id>")
def service_detail(service_id):

    service = db.get_db().execute(
        """
        SELECT id, name, duration_minutes, price_cents
        FROM services
        WHERE id = ? AND active = 1
        """,
        (service_id,)
    ).fetchone()

    if service is None:
        abort(404)

    return render_template(
        "service-detail.html",
        service=service
    )


# -----------------------------------
# BOOK APPOINTMENT PAGE
# Existing Week 3 functionality
# -----------------------------------

@app.route("/book")
def book():
    return render_template(
        "book.html",
        services=SAMPLE_SERVICES
    )


# -----------------------------------
# STAFF CALENDAR PAGE
# -----------------------------------

@app.route("/calendar")
def calendar():
    return render_template(
        "calendar.html",
        appointments=SAMPLE_CALENDAR
    )


# -----------------------------------
# CUSTOMER APPOINTMENTS PAGE
# -----------------------------------

@app.route("/appointments")
def appointments():
    return render_template(
        "appointments.html",
        appointments=SAMPLE_APPOINTMENTS
    )


# -----------------------------------
# SERVICES ADMIN PAGE
# -----------------------------------

@app.route("/services-admin")
def services_admin():
    return render_template(
        "services-admin.html",
        services=SAMPLE_SERVICES
    )


# -----------------------------------
# ADD NEW SERVICE
# GET = DISPLAY FORM
# POST = SAVE TO DATABASE
# -----------------------------------

@app.route("/admin/services/new", methods=["GET", "POST"])
def new_service():

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        duration = request.form.get("duration_minutes", "").strip()

        price = request.form.get("price", "").strip()

        # Refuse empty service names
        if not name:
            return render_template(
                "new-service.html",
                error="Service name cannot be empty."
            )

        # Convert dollars into cents
        price_cents = round(float(price) * 100)

        # Insert new service into SQLite
        database = db.get_db()

        database.execute(
            """
            INSERT INTO services
            (name, duration_minutes, price_cents, active)
            VALUES (?, ?, ?, ?)
            """,
            (name, int(duration), price_cents, 1)
        )

        # Save changes
        database.commit()

        # Redirect to services list
        return redirect(url_for("services"))

    return render_template("new-service.html")


# -----------------------------------
# RUN FLASK APPLICATION
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)
