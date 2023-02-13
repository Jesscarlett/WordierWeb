from django.http import HttpResponse
from django.shortcuts import render
import json
import os
import random
# Create your views here.
from django.templatetags.static import static


def index(request):
    quote = quote_func()
    joke = joke_func()
    w1, m1, w2, m2, w3, m3, w4, m4, w5, m5, w6, m6, w7, m7, w8, m8, w9, m9, w10, m10 = junior_random_func()
    jq1, ja1, jq2, ja2, jq3, ja3, jq4, ja4, jq5, ja5, jq6, ja6, jq7, ja7, jq8, ja8 = joke_random_func()
    q1, q2, q3, q4, q5, q6, q7, q8 = quote_random_func()
    cq1, cq2, cq3, cq4 = conversation_random_func()
    return render(request, 'home.html', {'quote': quote,
                                         'joke': joke,
                                         'w1': w1, 'm1': m1,
                                         'w2': w2, 'm2': m2,
                                         'w3': w3, 'm3': m3,
                                         'w4': w4, 'm4': m4,
                                         'w5': w5, 'm5': m5,
                                         'jq1': jq1, 'ja1': ja1,
                                         'jq2': jq2, 'ja2': ja2,
                                         'jq3': jq3, 'ja3': ja3,
                                         'jq4': jq4, 'ja4': ja4,
                                         'q1': q1, 'q2': q2,
                                         'q3': q3, 'q4': q4,
                                         'cq1': cq1, 'cq2': cq2,
                                         'cq3': cq3, 'cq4': cq4
                                         })


def quote_func():
    with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\quotes.json") as file:
        quotes_d = json.load(file)
        i = random.randint(21879, 23145)
        k = str(i)
        quote = '"' + quotes_d[k]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[k]['A']
    return quote


def joke_func():
    with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\jokes.json") as file:
        jokes_d = json.load(file)
        m = random.randint(1000, 1716)
        n = str(m)
        joke = "Q: " + jokes_d[n]['Q'] + '\n' + '\n' + "        " + jokes_d[n]['A']
    return joke


def dict_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        word, result1, result2, result3 = show_data_meaning(user_input)
        return render(request, 'definition.html', {'result1': result1, 'result2': result2, 'result3': result3, 'word': word})

    else:
        quote = quote_func()
        joke = joke_func()
        w1, m1, w2, m2, w3, m3, w4, m4, w5, m5, w6, m6, w7, m7, w8, m8, w9, m9, w10, m10 = junior_random_func()
        jq1, ja1, jq2, ja2, jq3, ja3, jq4, ja4, jq5, ja5, jq6, ja6, jq7, ja7, jq8, ja8 = joke_random_func()
        q1, q2, q3, q4, q5, q6, q7, q8 = quote_random_func()
        cq1, cq2, cq3, cq4 = conversation_random_func()
    return render(request, 'home.html', {'quote': quote,
                                         'joke': joke,
                                         'w1': w1, 'm1': m1,
                                         'w2': w2, 'm2': m2,
                                         'w3': w3, 'm3': m3,
                                         'w4': w4, 'm4': m4,
                                         'w5': w5, 'm5': m5,
                                         'jq1': jq1, 'ja1': ja1,
                                         'jq2': jq2, 'ja2': ja2,
                                         'jq3': jq3, 'ja3': ja3,
                                         'jq4': jq4, 'ja4': ja4,
                                         'q1': q1, 'q2': q2,
                                         'q3': q3, 'q4': q4,
                                         'cq1': cq1, 'cq2': cq2,
                                         'cq3': cq3, 'cq4': cq4
                                         })


def junior_random_func():
    with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\PSBjunior.json") as file:
        junior_d = json.load(file)
        jr = random.sample(list(junior_d), 10)
        e = str(jr[0])
        f = str(jr[1])
        g = str(jr[2])
        h = str(jr[3])
        o = str(jr[4])
        p = str(jr[5])
        q = str(jr[6])
        r = str(jr[7])
        s = str(jr[8])
        t = str(jr[9])
        w1 = e.capitalize()
        m1 = junior_d[e]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w2 = f.capitalize()
        m2 = junior_d[f]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w3 = g.capitalize()
        m3 = junior_d[g]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w4 = h.capitalize()
        m4 = junior_d[h]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w5 = o.capitalize()
        m5 = junior_d[o]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w6 = p.capitalize()
        m6 = junior_d[p]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w7 = q.capitalize()
        m7 = junior_d[q]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w8 = r.capitalize()
        m8 = junior_d[r]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w9 = s.capitalize()
        m9 = junior_d[s]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        w10 = t.capitalize()
        m10 = junior_d[t]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
    return w1, m1, w2, m2, w3, m3, w4, m4, w5, m5, w6, m6, w7, m7, w8, m8, w9, m9, w10, m10


def senior_random_func():
    with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\PSBsenior.json") as file:
        senior_d = json.load(file)
        sr = random.sample(list(senior_d), 10)
        x1 = str(sr[0])
        x2 = str(sr[1])
        x3 = str(sr[2])
        x4 = str(sr[3])
        x5 = str(sr[4])
        x6 = str(sr[5])
        x7 = str(sr[6])
        x8 = str(sr[7])
        x9 = str(sr[8])
        x10 = str(sr[9])
        ws1 = x1.capitalize()
        ms1 = senior_d[x1]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws2 = x2.capitalize()
        ms2 = senior_d[x2]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws3 = x3.capitalize()
        ms3 = senior_d[x3]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws4 = x4.capitalize()
        ms4 = senior_d[x4]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws5 = x5.capitalize()
        ms5 = senior_d[x5]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws6 = x6.capitalize()
        ms6 = senior_d[x6]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws7 = x7.capitalize()
        ms7 = senior_d[x7]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws8 = x8.capitalize()
        ms8 = senior_d[x8]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws9 = x9.capitalize()
        ms9 = senior_d[x9]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
        ws10 = x10.capitalize()
        ms10 = senior_d[x10]['definition'].lstrip().replace(' ', ' | ', 1) + '\n'
    return ws1, ms1, ws2, ms2, ws3, ms3, ws4, ms4, ws5, ms5, ws6, ms6, ws7, ms7, ws8, ms8, ws9, ms9, ws10, ms10


def joke_random_func():
    with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\jokes.json") as file:
        joke_d = json.load(file)
        jo = random.sample(list(joke_d), 8)
        e1 = str(jo[0])
        e2 = str(jo[1])
        e3 = str(jo[2])
        e4 = str(jo[3])
        e5 = str(jo[4])
        e6 = str(jo[5])
        e7 = str(jo[6])
        e8 = str(jo[7])
        jq1 = joke_d[e1]['Q'].lstrip()
        ja1 = joke_d[e1]['A'].lstrip() + '\n'
        jq2 = joke_d[e2]['Q'].lstrip()
        ja2 = joke_d[e2]['A'].lstrip() + '\n'
        jq3 = joke_d[e3]['Q'].lstrip()
        ja3 = joke_d[e3]['A'].lstrip() + '\n'
        jq4 = joke_d[e4]['Q'].lstrip()
        ja4 = joke_d[e4]['A'].lstrip() + '\n'
        jq5 = joke_d[e5]['Q'].lstrip()
        ja5 = joke_d[e5]['A'].lstrip() + '\n'
        jq6 = joke_d[e6]['Q'].lstrip()
        ja6 = joke_d[e6]['A'].lstrip() + '\n'
        jq7 = joke_d[e7]['Q'].lstrip()
        ja7 = joke_d[e7]['A'].lstrip() + '\n'
        jq8 = joke_d[e8]['Q'].lstrip()
        ja8 = joke_d[e8]['A'].lstrip() + '\n'
    return jq1, ja1, jq2, ja2, jq3, ja3, jq4, ja4, jq5, ja5, jq6, ja6, jq7, ja7, jq8, ja8


def quote_random_func():
    with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\quotes.json") as file:
        quotes_d = json.load(file)
        random_numbers = random.sample(range(21879, 23146), 8)
        a1 = str(random_numbers[0])
        a2 = str(random_numbers[1])
        a3 = str(random_numbers[2])
        a4 = str(random_numbers[3])
        a5 = str(random_numbers[4])
        a6 = str(random_numbers[5])
        a7 = str(random_numbers[6])
        a8 = str(random_numbers[7])
        q1 = '"' + quotes_d[a1]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[a1]['A']
        q2 = '"' + quotes_d[a2]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[a2]['A']
        q3 = '"' + quotes_d[a3]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[a3]['A']
        q4 = '"' + quotes_d[a4]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[a4]['A']
        q5 = '"' + quotes_d[a5]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[a5]['A']
        q6 = '"' + quotes_d[a6]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[a6]['A']
        q7 = '"' + quotes_d[a7]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[a7]['A']
        q8 = '"' + quotes_d[a8]['Q'] + '"' + '\n' + '\n' + '--- ' + quotes_d[a8]['A']
    return q1, q2, q3, q4, q5, q6, q7, q8


def conversation_random_func():
    with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\CQ.json") as file:
        conversation_d = json.load(file)
        con = random.sample(list(conversation_d), 5)
        c1 = str(con[0])
        c2 = str(con[1])
        c3 = str(con[2])
        c4 = str(con[3])
        cq1 = "Q: " + conversation_d[c1].lstrip() + '\n'
        cq2 = "Q: " + conversation_d[c2].lstrip() + '\n'
        cq3 = "Q: " + conversation_d[c3].lstrip() + '\n'
        cq4 = "Q: " + conversation_d[c4].lstrip() + '\n'
    return cq1, cq2, cq3, cq4


def show_data_meaning(user_input):
    # perform some function using the user_input
    try:
        search_word = user_input
        if search_word == '':
            search_word = 'hello'
            x = 'h'
        else:
            x = search_word[0].upper()

        with open(os.path.dirname(os.path.dirname(__file__)) + f"\\static\\D{x}.json") as file:
            word_dict = json.load(file)
        word = search_word.upper()
        if word in word_dict:
            first_meaning = word_dict.get(word)
            full_meaning = first_meaning.get('MEANINGS')
            first_n_pair = list(full_meaning.items())[:3]
            m = str(first_n_pair)
            word_meaning = m.translate(str.maketrans({'{': None, '}': None, "[": None,
                                                      "]": None, "'": None, "'": None, "(": None,
                                                      ")": None}))
            num_list = ["1,", "2,", "3,", "4,", "5,"]
            for char in num_list:
                word_meaning = word_meaning.replace(char, "")
            word_meaning = word_meaning.replace(", ,", ",")
            synonyms = first_meaning.get('SYNONYMS')
            word_synonym = str(synonyms).translate(str.maketrans({'{': None,
                                                                  '}': None,
                                                                  "[": None,
                                                                  "]": None,
                                                                  "'": None,
                                                                  "'": None,
                                                                  "(": None,
                                                                  ")": None}))

        with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\PSBjunior.json") as file:
            example1_dict = json.load(file)

        with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\PSBsenior.json") as file:
            example2_dict = json.load(file)

        with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\sentencepos.json") as file:
            example3_dict = json.load(file)

        k = word.lower()
        if k in example1_dict.keys():
            sentence_list = example1_dict[k]['definition'].split(": ", 1)
            sentence = sentence_list[-1]
            sen = 'SENTENCE: ' + sentence
        elif k in example2_dict.keys():
            sentence_list = example2_dict[k]['definition'].split(": ", 1)
            sentence = sentence_list[-1]
            sen = 'SENTENCE: ' + sentence
        elif k in example3_dict.keys():
            sentence = example3_dict[k]['sentence']
            sen = 'SENTENCE: ' + sentence
        else:
            sen = ""
        result1 = ' MEANINGS: ' + word_meaning + ' ...'
        result2 = ' SYNONYMS: ' + word_synonym + '.'
        result3 = ' ' + sen
        return search_word.capitalize(), result1, result2, result3
    except UnboundLocalError or AttributeError:
        result1 = 'Word is not found, please check your spelling.'
        result2 = ""
        result3 = ""
        return search_word.capitalize(), result1, result2, result3


def junior_senior_words(request):
    w1, m1, w2, m2, w3, m3, w4, m4, w5, m5, w6, m6, w7, m7, w8, m8, w9, m9, w10, m10 = junior_random_func()
    ws1, ms1, ws2, ms2, ws3, ms3, ws4, ms4, ws5, ms5, ws6, ms6, ws7, ms7, ws8, ms8, ws9, ms9, ws10, ms10 = \
        senior_random_func()
    return render(request, 'pswords.html', {
        'w1': w1, 'm1': m1, 'w2': w2, 'm2': m2,  'w3': w3, 'm3': m3, 'w4': w4, 'm4': m4, 'w5': w5, 'm5': m5,
        'w6': w6, 'm6': m6, 'w7': w7, 'm7': m7, 'w8': w8, 'm8': m8, 'w9': w9, 'm9': m9, 'w10': w10, 'm10': m10,
        'ws1': ws1, 'ms1': ms1,
        'ws2': ws2, 'ms2': ms2,
        'ws3': ws3, 'ms3': ms3,
        'ws4': ws4, 'ms4': ms4,
        'ws5': ws5, 'ms5': ms5,
        'ws6': ws6, 'ms6': ms6,
        'ws7': ws7, 'ms7': ms7,
        'ws8': ws8, 'ms8': ms8,
        'ws9': ws9, 'ms9': ms9,
        'ws10': ws10, 'ms10': ms10})


def senior_words(request):
    w1, m1, w2, m2, w3, m3, w4, m4, w5, m5, w6, m6, w7, m7, w8, m8, w9, m9, w10, m10 = junior_random_func()
    ws1, ms1, ws2, ms2, ws3, ms3, ws4, ms4, ws5, ms5, ws6, ms6, ws7, ms7, ws8, ms8, ws9, ms9, ws10, ms10 = \
        senior_random_func()
    return render(request, 'seniorwords.html', {
        'w1': w1, 'm1': m1, 'w2': w2, 'm2': m2,  'w3': w3, 'm3': m3, 'w4': w4, 'm4': m4, 'w5': w5, 'm5': m5,
        'w6': w6, 'm6': m6, 'w7': w7, 'm7': m7, 'w8': w8, 'm8': m8, 'w9': w9, 'm9': m9, 'w10': w10, 'm10': m10,
        'ws1': ws1, 'ms1': ms1,
        'ws2': ws2, 'ms2': ms2,
        'ws3': ws3, 'ms3': ms3,
        'ws4': ws4, 'ms4': ms4,
        'ws5': ws5, 'ms5': ms5,
        'ws6': ws6, 'ms6': ms6,
        'ws7': ws7, 'ms7': ms7,
        'ws8': ws8, 'ms8': ms8,
        'ws9': ws9, 'ms9': ms9,
        'ws10': ws10, 'ms10': ms10})


def jokes_quotes(request):
    jq1, ja1, jq2, ja2, jq3, ja3, jq4, ja4, jq5, ja5, jq6, ja6, jq7, ja7, jq8, ja8 = joke_random_func()
    q1, q2, q3, q4, q5, q6, q7, q8 = quote_random_func()
    if request.method == 'POST':
        key_word = request.POST.get('key_word')
        quote1, quote2, quote3, quote4, quote5 = show_quotes(key_word)
        return render(request, 'jokes_quotes.html', {'jq1': jq1, 'ja1': ja1,
                                                   'jq2': jq2, 'ja2': ja2,
                                                   'jq3': jq3, 'ja3': ja3,
                                                   'jq4': jq4, 'ja4': ja4,
                                                   'jq5': jq5, 'ja5': ja5,
                                                   'jq6': jq6, 'ja6': ja6,
                                                   'jq7': jq7, 'ja7': ja7,
                                                   'jq8': jq8, 'ja8': ja8,
                                                   'q1': q1, 'q2': q2,
                                                   'q3': q3, 'q4': q4,
                                                   'q5': q5, 'q6': q6,
                                                   'q7': q7, 'q8': q8,
                                                   'quote1': quote1, 'quote2': quote2,
                                                   'quote3': quote3, 'quote4': quote4,
                                                   'quote5': quote5
                                                 })
    else:
        quote1 = ""
        quote2 = ""
        quote3 = ""
        quote4 = ""
        quote5 = ""
        return render(request, 'jokes_quotes.html', {'jq1': jq1, 'ja1': ja1,
                                                     'jq2': jq2, 'ja2': ja2,
                                                     'jq3': jq3, 'ja3': ja3,
                                                     'jq4': jq4, 'ja4': ja4,
                                                     'jq5': jq5, 'ja5': ja5,
                                                     'jq6': jq6, 'ja6': ja6,
                                                     'jq7': jq7, 'ja7': ja7,
                                                     'jq8': jq8, 'ja8': ja8,
                                                     'q1': q1, 'q2': q2,
                                                     'q3': q3, 'q4': q4,
                                                     'q5': q5, 'q6': q6,
                                                     'q7': q7, 'q8': q8,
                                                     'quote1': quote1, 'quote2': quote2,
                                                     'quote3': quote3, 'quote4': quote4,
                                                     'quote5': quote5
                                                   })


def show_quotes(key_word):
    quotes_list = []
    try:
        quote_word = key_word
        if quote_word == '':
            quote_word = 'success'
        else:
            lower_word = quote_word.lower()
        with open(os.path.dirname(os.path.dirname(__file__)) + "\\static\\quotes.json") as quote_file:
            quotes_dict = json.load(quote_file)
            i = random.randint(2, 23144)
            n = 0
            for x in range(i, 23145):
                if lower_word in quotes_dict[str(x)]['Q'].lower():
                    quotes_list.append(quotes_dict[str(x)]['Q'] + '  --- ' + quotes_dict[str(x)]['A'])
                    n += 1
                    if n > 4:
                        break
                    else:
                        pass
                else:
                    pass
            for y in range(1, i):
                if n > 4:
                    break
                else:
                    if lower_word in quotes_dict[str(y)]['Q'].lower():
                        quotes_list.append(quotes_dict[str(y)]['Q'] + ' --- ' + quotes_dict[str(x)]['A'])
                        n += 1
                    else:
                        pass
        try:
            quote1 = quotes_list[0]
        except IndexError:
            quote1 = 'Quotes related to this word are not found. Please try another word.'
        try:
            quote2 = quotes_list[1]
        except IndexError:
            quote2 = ""
        try:
            quote3 = quotes_list[2]
        except IndexError:
            quote3 = ""
        try:
            quote4 = quotes_list[3]
        except IndexError:
            quote4 = ""
        try:
            quote5 = quotes_list[4]
        except IndexError:
            quote5 = ""
    except UnboundLocalError or AttributeError:
        quote1 = 'Quotes related to this word are not found. Please try another word.'
        quote2, quote3, quote4, quote5 = ""
    return quote1, quote2, quote3, quote4, quote5

