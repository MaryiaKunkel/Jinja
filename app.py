from flask import Flask, render_template, request
from stories import Story

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/story_1')
def story_1():
    place=request.args.get('place')
    adjective=request.args.get('adjective')
    noun=request.args.get('noun')
    verb=request.args.get('verb')
    plural_noun=request.args.get('plural_noun')

    story=Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    )

    generated_story = story.generate({
        'place': place,
        'adjective': adjective,
        'noun': noun,
        'verb': verb,
        'plural_noun': plural_noun
    })

    return render_template('story_1.html', generated_story=generated_story)

@app.route('/story_2')
def story_2():
    place=request.args.get('place')
    adjective=request.args.get('adjective')
    noun=request.args.get('noun')
    verb=request.args.get('verb')
    plural_noun=request.args.get('plural_noun')

    story=Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """In a land far away, a {adjective} {noun} lived in a {place}. It had a unique talent for {verb} {plural_noun} every day."""
    )

    generated_story = story.generate({
        'place': place,
        'adjective': adjective,
        'noun': noun,
        'verb': verb,
        'plural_noun': plural_noun
    })

    return render_template('story_2.html', generated_story=generated_story)

@app.route('/story_3')
def story_3():
    place=request.args.get('place')
    adjective=request.args.get('adjective')
    noun=request.args.get('noun')
    verb=request.args.get('verb')
    plural_noun=request.args.get('plural_noun')

    story=Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Long ago, in a magical {place}, there existed a {adjective} {noun}. It was known for its ability to {verb} {plural_noun} with grace."""
    )

    generated_story = story.generate({
        'place': place,
        'adjective': adjective,
        'noun': noun,
        'verb': verb,
        'plural_noun': plural_noun
    })

    return render_template('story_3.html', generated_story=generated_story)

@app.route('/story_4')
def story_4():
    place=request.args.get('place')
    adjective=request.args.get('adjective')
    noun=request.args.get('noun')
    verb=request.args.get('verb')
    plural_noun=request.args.get('plural_noun')

    story=Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in an enchanted {place}, a {adjective} {noun} dwelled. Its favorite pastime was to {verb} {plural_noun} under the moonlight."""
    )

    generated_story = story.generate({
        'place': place,
        'adjective': adjective,
        'noun': noun,
        'verb': verb,
        'plural_noun': plural_noun
    })

    return render_template('story_4.html', generated_story=generated_story)

@app.route('/story_5')
def story_5():
    place=request.args.get('place')
    adjective=request.args.get('adjective')
    noun=request.args.get('noun')
    verb=request.args.get('verb')
    plural_noun=request.args.get('plural_noun')

    story=Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """In a realm of {place}, a {adjective} {noun} resided. It was famous for its talent to {verb} {plural_noun} in harmony with nature."""
    )

    generated_story = story.generate({
        'place': place,
        'adjective': adjective,
        'noun': noun,
        'verb': verb,
        'plural_noun': plural_noun
    })

    return render_template('story_5.html', generated_story=generated_story)
