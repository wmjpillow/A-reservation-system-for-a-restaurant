import datetime

from app import app, db
from flask import render_template, flash, redirect, session, g

from .forms import ReservationForm, ShowReservationsOnDateForm, AddTableForm
from .controller import create_reservation
from .models import Table, Reservation


# Time Display: book table in fixed hours when the restaurant operates.
RESTAURANT_OPEN_TIME=10
RESTAURANT_CLOSE_TIME=22


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="A Reservation System For A Restaurant")

@app.route('/reservation_status', methods=['GET', 'POST'])
def reservation_status():
    form = ReservationForm()
    if form.validate_on_submit():
        if form.reservation_datetime.data < datetime.datetime.now():
            flash("You cannot book dates in the past")
            return redirect('/reservation_status')
        reservation_date = datetime.datetime.combine(form.reservation_datetime.data.date(), datetime.datetime.min.time())
        if form.reservation_datetime.data < reservation_date + datetime.timedelta(hours=RESTAURANT_OPEN_TIME) or \
        form.reservation_datetime.data > reservation_date + datetime.timedelta(hours=RESTAURANT_CLOSE_TIME):
            flash("The restaurant is closed at that hour!")
            return redirect('/reservation_status')
        reservation = create_reservation(form)
        if reservation:
            flash("Reservation created!")
            return redirect('/index')
        else:
            flash("That time is taken!  Try another time")
            return redirect('/reservation_status')
    return render_template('reservation_status.html', title="Make Reservation", form=form)

@app.route('/show_tables', methods=['GET', 'POST'])
def show_tables():
    form = AddTableForm()

    if form.validate_on_submit():
        table = Table(capacity=int(form.table_capacity.data))
        db.session.add(table)
        db.session.commit()
        flash("Table created!")
        return redirect('/show_tables')

    tables = Table.query.all()
    return render_template('show_tables.html', title="Tables", tables=tables, form=form)

@app.route('/show_reservations', methods=['GET', 'POST'])
@app.route('/show_reservations/<reservation_date>', methods=['GET', 'POST'])
def show_reservations(reservation_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")):
    form = ShowReservationsOnDateForm()
    if form.validate_on_submit():
        res_date = datetime.datetime.strftime(form.reservation_date.data, "%Y-%m-%d")
        return redirect('/show_reservations/' + res_date)
    res_date = datetime.datetime.strptime(reservation_date, "%Y-%m-%d")
    reservations = Reservation.query.filter(Reservation.reservation_time >= res_date,
                                            Reservation.reservation_time < res_date + datetime.timedelta(days=1)).all()

    return render_template('show_reservations.html', title="Reservations", reservations=reservations, form=form)

@app.route('/admin')
def admin():
    return render_template('admin.html', title="Admin")
