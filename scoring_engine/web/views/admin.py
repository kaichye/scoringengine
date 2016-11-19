from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required
from operator import itemgetter
from scoring_engine.models.user import User
from scoring_engine.models.team import Team


mod = Blueprint('admin', __name__)


@mod.route('/admin')
@mod.route('/admin/status')
@login_required
def status():
    if current_user.is_white_team:
        return render_template('admin/status.html')
    else:
        return redirect(url_for('auth.unauthorized'))


@mod.route('/admin/manage')
@login_required
def manage():
    if current_user.is_white_team:
        users = User.query.with_entities(User.id, User.username).all()
        teams = Team.query.with_entities(Team.id, Team.name).all()
        return render_template('admin/manage.html', users=sorted(users, key=itemgetter(0)), teams=teams)
    else:
        return redirect(url_for('auth.unauthorized'))


@mod.route('/admin/stats')
@login_required
def stats():
    if current_user.is_white_team:
        return render_template('admin/stats.html')
    else:
        return redirect(url_for('auth.unauthorized'))


@mod.route('/admin/services')
@login_required
def services():
    if current_user.is_white_team:
        blue_teams = Team.query.filter(Team.color == 'Blue').all()
        return render_template('admin/services.html', blue_teams=blue_teams)
    else:
        return redirect(url_for('auth.unauthorized'))
