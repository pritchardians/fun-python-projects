import random

sentence_structure = 'art adj noun adv verb art adj noun'
nouns = ['man', 'dog', 'human', 'vampire', 'bat', 'thief', 'monster', 'fish', 'bird', 'traffic warden', 'twin',
         'choirmaster', 'stalker', 'daredevil',
         'flea', 'ghost', 'talking tree', 'Pirate', 'uncle', 'pest', 'zombie', 'walrus', 'whale', 'fowl', 'seagull',
         'cop', 'child', 'circus master', 'clown', 'eagle', 'mentor']
adjectives = ['angry', 'big', 'small', 'hairy', 'hard', 'gray', 'cool', 'skinny', 'upset', 'unintelligible',
              'fictional', 'stubbled', 'pale', 'stumbling', 'old',
              'cold', 'swashbuckling', 'Scottish', 'haggard', 'overworked', 'contaminated', 'scarred', 'terrified',
              'clammy', 'sweating', 'laughing', 'confused', 'handsome', 'rugged', 'posh', 'filthy', 'troublesome']
verbs = ['ponders', 'eats', 'jumps over', 'overtakes', 'trips', 'rips', 'swims behind', 'treats', 'paints', 'cons',
         'pecks', 'follows', 'ignores', 'woos', 'undervalues', 'trips up', 'mistakenly chooses',
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


print(create_sentence(' '))
print(create_sentence('connecting'))
