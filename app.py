from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story


app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/story')
def story():
    place=request.args.get('place')
    adjective=request.args.get('adjective')
    noun=request.args.get('noun')
    verb=request.args.get('verb')
    plural_noun=request.args.get('plural_noun')
    selected_story=request.args.get('selected_story')

    story_templates={
        'Story 1': """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
        'Story 2': '''Once upon a time in a mystical {place}, there dwelled a wise {adjective} {noun}. It delighted in {verb} {plural_noun} under the moonlight.''',
        'Story 3': '''In a distant land known as {place}, a brave {adjective} {noun} resided. Its greatest joy was to {verb} {plural_noun} and spread laughter.''',
        'Story 4':'''Far away, in the realm of {place}, a curious {adjective} {noun} existed. It spent its days {verb} {plural_noun} and discovering new horizons.''',
        'Story 5':'''Once upon a time, within the enchanted {place}, lived a kind-hearted {adjective} {noun}. Its true passion was to {verb} {plural_noun} and bring joy to all.'''
    }

    if selected_story in story_templates:
        story_template=story_templates[selected_story]
    
        story=Story(
        ["place", "noun", "verb", "adjective", "plural_noun"], story_template)

        generated_story = story.generate({
            'place': place,
            'adjective': adjective,
            'noun': noun,
            'verb': verb,
            'plural_noun': plural_noun
        })

        

        return render_template('story.html', selected_story=selected_story, generated_story=generated_story, story_template=story_template)