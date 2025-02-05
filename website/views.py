from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Mood_Tracker
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    search_query = request.args.get('search', '')

    if request.method == 'POST':
        title = request.form.get('title')
        trigger = request.form.get('trigger')
        preferred_approach = request.form.get('preferred_approach')
        better_approach = request.form.get('better_approach')
        resolution = request.form.get('Resolution')
        satisfaction_rate = request.form.get('Satisfaction_rate')

        if not title or not trigger or not satisfaction_rate:
            flash('Title, Trigger, and Satisfaction Rate are required.', 'error')
        else:
            new_entry = Mood_Tracker(
                user_id=current_user.id,
                title=title,
                trigger=trigger,
                preferred_approach=preferred_approach,
                better_approach=better_approach,
                Resolution=resolution,
                Satisfaction_rate=int(satisfaction_rate)
            )
            db.session.add(new_entry)
            db.session.commit()
            flash('Mood entry added successfully!', 'success')
            return redirect(url_for('views.home'))

    if search_query:
        entries = Mood_Tracker.query.filter(Mood_Tracker.title.ilike(f'%{search_query}%'), Mood_Tracker.user_id == current_user.id).all()
    else:
        entries = Mood_Tracker.query.filter_by(user_id=current_user.id).order_by(Mood_Tracker.date.desc()).limit(5).all()
    
    return render_template("home.html", user=current_user, entries=entries, search_query=search_query)

@views.route('/delete/<int:entry_id>', methods=['POST'])
@login_required
def delete_entry(entry_id):
    entry = Mood_Tracker.query.get(entry_id)
    if entry and entry.user_id == current_user.id:
        db.session.delete(entry)
        db.session.commit()
        flash('Entry deleted successfully!', 'success')
    else:
        flash('Unauthorized action.', 'error')
    return redirect(url_for('views.home'))
