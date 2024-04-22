from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.contrib.auth import get_user_model
from HangManApp.models import *
from django.utils.crypto import get_random_string
import os

game_word = ""
current_string = ""
mistake = 0

word_list = {
    'food': ['pizza', 'burger', 'sushi', 'pasta', 'salad'],
    'sport': ['basketball', 'soccer', 'tennis', 'swimming', 'cycling'],
    'color': ['red', 'blue', 'green', 'yellow', 'black']
}


@csrf_exempt
def check_letter(request):
    global game_word
    global current_string
    global mistake



    data = json.loads(request.body)
    character = data['character']
    username_of_click = data['username']

    score = Game.objects.filter(member_model__username=username_of_click).first()
    game_word = score.game_word_model
    current_string = score.current_string_model
    mistake = score.mistakes_model

    if character in game_word:
        answer_status = True
        for i in range(len(game_word)):
            if game_word[i] != ' ' and game_word[i] == character:
                current_string_list = list(current_string)
                current_string_list[i] = game_word[i]
                current_string = ''.join(current_string_list)
    else:
        answer_status = False
        mistake+= 1

    if(mistake >= 6): win_status = "lose"
    elif(not '_' in current_string): win_status = "win"
    else: win_status = "none"
    

    score.game_word_model = game_word
    score.current_string_model = current_string
    score.mistakes_model = str(mistake)
    score.save(update_fields=['game_word_model', 'current_string_model', 'mistakes_model'])

    print("*** user " + username_of_click + " clicked on " + character + " | game_word: " + game_word + ", currentString: " + current_string + ", mistakes: " + str(mistake))

    if(win_status == "lose"): answer = game_word
    else: answer = ""
    return JsonResponse({'success': True, 'current_string' : current_string, 'hang_man_image' : 'HangMan' + str(min(mistake+1, 7)) + '.png', 'answer_status' : answer_status, 'win_status': win_status, 'answer' : answer})

def main(request):
    
    global game_word
    global current_string
    global mistake
    global word_list
    
    random_category = random.choice(list(word_list.keys()))
    random_item = random.choice(word_list[random_category])

    game_word = random_item

    mistake = 0
    current_string = "_"*len(game_word)

    game_word = ' '.join(game_word.upper())
    current_string = ' '.join(current_string.upper())

    

    unique_id = str(get_random_string(length=32))
    print("*** new game started with " + game_word + " word by " + unique_id)

    member = Member(username=unique_id)
    member.save()
    new_score = Game(member_model=member, game_word_model=game_word, current_string_model = current_string, mistakes_model = mistake)
    new_score.save()

    return render(request, 'index.html', {'empty_word' : current_string, 'category' : random_category, 'username' : unique_id})

def own_web(request):
    return render(request, 'main.html')
