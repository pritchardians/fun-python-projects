from flask import Flask, render_template, request, redirect
import random
import logging
import folium
from funs import where_on_earth as woe

app = Flask(__name__)
logger = logging.getLogger('werkzeug')
loc_lat = 0
loc_long = 0

project_list = ['Nonsense Sentences', 'Proverbs', 'Geeky Stuff', 'Sign Up Form']
topic_list = ['Comprehensions']
sentence_structure = 'art adj noun adv verb art adj noun'
proverb_structure = ['a stitch in time saves nine', 'look before you leap']
nouns = ['man', 'dog', 'human', 'vampire', 'bat', 'thief', 'monster', 'fish', 'bird', 'traffic warden', 'twin',
         'choirmaster',
         'flea', 'ghost', 'talking tree', 'Pirate', 'uncle', 'pest', 'zombie', 'walrus', 'whale', 'fowl', 'seagull',
         'cop', 'child', 'circus master', 'clown', 'eagle', 'mentor']
adjectives = ['angry', 'big', 'small', 'hairy', 'hard', 'gray', 'cool', 'skinny', 'upset', 'unintelligible',
              'fictional',
              'cold', 'swashbuckling', 'Scottish', 'haggard', 'overworked', 'contaminated', 'scarred', 'terrified',
              'clammy', 'sweating', 'laughing', 'confused', 'handsome', 'rugged', 'posh', 'filthy', 'troublesome']
verbs = ['ponders', 'eats', 'jumps over', 'overtakes', 'trips', 'rips', 'swims behind', 'treats', 'paints', 'cons',
         'jumps', 'pecks', 'follows', 'ignores', 'woos', 'undervalues', 'trips up', 'mistakenly chooses',
         'pulls', 'torments', 'delights', 'loves', 'dislikes', 'runs away from', 'is ambivalent towards', 'ignores',
         'fights', 'flees', 'creeps up on']
adverbs = ['quickly', 'easily', 'grumpily', 'massively', 'politely', 'scandalously', 'scarily', 'daintily', 'slowly',
           'greedily', 'lovingly', 'nervously', 'stealthily']
pronouns = ['he', 'she', 'they', 'it', 'me']
prepositions = ['by', 'with', 'about', 'until', 'through']
conjunctions = ['and', ' but', ' or', ' while', ' because']
interjections = ['oh', ' wow', ' oops', 'huh', 'well I never']
articles = ['the', 'a', 'his', 'her', 'the', 'a', 'the', 'a']
connectors = ['meanwhile', 'but', 'while', 'however', 'but over there', 'until', 'before']
punctuation = ['!', '.', '...']
bef = 'before you0'
vowels = ['a', 'e', 'i', 'o', 'u']


def create_sentence(type):
    last_article = ''
    if type == 'connecting':
        sentence = random.choice(connectors) + ' '
    else:
        sentence = ''
    for fig_of_speech in sentence_structure.split():
        if fig_of_speech == 'noun':
            sentence += random.choice(nouns)
        if fig_of_speech == 'adj':
            adj = random.choice(adjectives)
            if adj[0] in vowels and last_article == 'a':
                sentence = sentence[:-1] + 'n '
            sentence += adj
        if fig_of_speech == 'verb':
            sentence += random.choice(verbs)
        if fig_of_speech == 'adv':
            sentence += random.choice(adverbs)
        if fig_of_speech == 'pro':
            sentence += random.choice(pronouns)
        if fig_of_speech == 'prep':
            sentence += random.choice(prepositions)
        if fig_of_speech == 'conj':
            sentence += random.choice(conjunctions)
        if fig_of_speech == 'inter':
            sentence += random.choice(interjections)
            sentence += ','
        if fig_of_speech == 'art':
            last_article = random.choice(articles)
            sentence += last_article
        sentence += ' '
    return punctuate(sentence)


def punctuate(sentence):
    sentence = sentence[:-1]
    return (sentence + random.choice(punctuation)).capitalize()


@app.route('/')
def home():
    return render_template('index.html', project_list=project_list)


@app.route('/nonsense')
def nonsense():
    return render_template('nonsense.html', first=create_sentence('first'),
                           second=create_sentence('connecting'))


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/geekout')
def geekout():
    return render_template('geekout.html', topic_list=topic_list)


@app.route('/thankyou')
def thankyou():
    username = request.args.get('username')
    logger.info("In thankyou route. Username is:")
    logger.info(username)
    if username == '':
        username = 'Guest'
    return render_template('thankyou.html', username=username)


@app.route('/where-on-earth')
def where_on_earth():
    location_details = woe.choose_location()
    global loc_lat
    global loc_long
    global loc_title
    (loc_lat, loc_long, loc_title, loc_description, loc_clues) = location_details
    (loc_clue_1, loc_clue_2, loc_clue_3) = loc_clues
    return render_template('where-on-earth.html',
                           description=loc_description,
                           title=loc_title,
                           clue_1=loc_clue_1,
                           clue_2=loc_clue_2,
                           clue_3=loc_clue_3
                           )


@app.route('/map')
def map():
    start_coords = (0, 0)
    fg_base = folium.FeatureGroup(name='Where On Earth?')
    fg_borders = folium.FeatureGroup(name='Borders')
    fg_base.add_child(
        folium.Marker(location=[loc_lat, loc_long], popup='<strong>You found me!</strong> <br> <br>' + loc_title
                      + '</br></br> Press the \'back\' button to return',
                      icon=folium.Icon(color='cadetblue')))
    for _ in range(0, 3):
        fg_base.add_child(folium.Marker(location=[random.randint(-90, 90), random.randint(-180, 180)],
                                        popup='<strong>Try again.</strong>',
                                        icon=folium.Icon(color='cadetblue')))

    where_on_earth_map = folium.Map(width=1000, height=650, location=start_coords, zoom_start=2,
                                    tiles='Stamen Terrain')
    where_on_earth_map.add_child(fg_base)
    where_on_earth_map.add_child(fg_borders)
    where_on_earth_map.add_child(folium.LayerControl())
    where_on_earth_map.save('templates/map.html')
    return render_template('map.html')
    # return where_on_earth_map._repr_html_()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True, port=random.randint(4000, 5000))
