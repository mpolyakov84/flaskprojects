from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm, DelForm


puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():

        new_puppy = Puppy(form.name.data)
        db.session.add(new_puppy)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add.html', form=form)

@puppies_blueprint.route('/delete', methods = ['GET', 'POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        del_puppy = Puppy.query.get(form.id.data)
        db.session.delete(del_puppy)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    return render_template('delete.html', form=form)

@puppies_blueprint.route('/list')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)