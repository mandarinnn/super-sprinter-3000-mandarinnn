from flask import Flask, render_template, request, redirect, url_for

from super_sprinter_3000.connectdatabase import ConnectDatabase
from super_sprinter_3000.models.Status import Status
from super_sprinter_3000.models.Story import Story

app = Flask(__name__)


def init_db():
    ConnectDatabase.db.connect()
    ConnectDatabase.db.drop_tables([Story, Status], safe=True)
    ConnectDatabase.db.create_tables([Story, Status], safe=True)

    stats = ['Planning', 'To Do', 'In Progress', 'Review', 'Done']
    for stat in stats:
        Status.create(name=stat)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.route('/story', methods=['GET', 'POST'])
def create_story():
    if request.method == 'POST':
        status = Status.get(Status.id == request.form['status'])
        Story.create(
            title=request.form['title'],
            story=request.form['story'],
            criteria=request.form['criteria'],
            business_value=request.form['business_value'],
            estimation=request.form['estimation'],
            status=status)
        return redirect(url_for('list_stories'))
    statuses = Status.select()
    return render_template('form.html', statuses=statuses, story=[])


@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
def update_stories(story_id):
    story = Story.get(Story.id == story_id)
    if request.method == 'GET':
        statuses = Status.select()
        return render_template('form.html', story=story, statuses=statuses)
    elif request.method == 'POST':
        story.title = request.form['title']
        story.story = request.form['story']
        story.criteria = request.form['criteria']
        story.business_value = request.form['business_value']
        story.estimation = request.form['estimation']
        story.status = request.form['status']
        story.save()
        return redirect(url_for('list_stories'))


@app.route('/')
@app.route('/list', strict_slashes=False, methods=['GET', 'POST'])
def list_stories():
    if request.method == 'POST':
        Story.delete().where(Story.id == request.form['story_id']).execute()
    stories = Story.select()
    return render_template('list.html', stories=stories)
