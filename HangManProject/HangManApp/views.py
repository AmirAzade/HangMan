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
        "sports" : ["football","baseball","breakdancing","cheerleading","figureskating","highkick",
                    "paragliding","parkour","stunt","trampoling","freerunnig","aerobatics","airracing",
                    "gliding","parachuting","skysurfing","skydiving","creeking","canoeing","waterpolo",
                    "waboba","backstroke","breaststroke","bifins","freediving","aquathlon","scubadiving",
                    "spearfishing","cliffdiving","archery","gungdo","softball","cricket","elle","kickball",
                    "matball","stickball","basketball","fastnet","beachsoccer","fieldgame","rugby","handball",
                    "hockey","rinkball","lacrosse","polo","badminton","fistball","tennis","skateboarding",
                    "snowboarding","snowkiting","surfing","rockclimbing","iceclimbing","hiking","bmx",
                    "cyclepolo","dirtjumping","unicycling","aikido","jujutsu","judo","sumo","wrestling",
                    "boxing","karate","wingchun","ninjutsu","taichi","frisbee","discgolf","calisthenics",
                    "poledance","ribbon","thumbling","kitesurfing","airsoft","paintball","darts","formulaone",
                    "hillclimbing","motocross","rally","ballet","bowling","lasertag","powerlifting","icefishing",
                    "hunting","bullriding","roping","poker","checkers","chess","sudoku","dominoes","shogi","eightball",
                    "tenball","onepocket","bankpool","killer","foosball","beachgolf","parkgolf","volleyball"
                    ]
 ,"foods&fruits" : ["Apple", "Banana", "Cherry", "Date", "Egg", "Fig", "Grape", "Honeydew", "Icecream", "Jackfruit",
                    "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Papaya", "Quince", "Raspberry", "Strawberry", "Tangerine",
                    "Ube", "Vanilla", "Watermelon", "Xigua", "Yam", "Zucchini",
                    "Almond", "Bread", "Cake", "Donut", "Eggplant", "Fish", "Garlic", "Ham", "Iceberglettuce", "Jelly",
                    "Kale", "Lamb", "Mushroom", "Noodles", "Oliveoil", "Pasta", "Quinoa", "Rice", "Sausage", "Tofu",
                    "Udonnoodles", "Vegetableoil", "Walnut", "Xanthangum", "Yogurt", "Zucchininoodles",
                    "Amaranth", "Bacon", "Cantaloupe", "Dill", "Eggplant", "Fetacheese", "Garlicbread", "Hamburger", "Icecreamsandwich", "Jalapeno",
                    "Kohlrabi", "Lentils", "Mozzarella cheese", "Nutella", "Olive", "Pancakes", "Quinoasalad", "Ricottacheese", "Salsa", "Tacos",
                    "Udon soup", "Vegetablebroth", "Watermelon", "Xerxes", "Yogurt", "Zucchinibread",
                    "Apricot", "Bakedbeans", "Caviar", "Doritos", "Eggsalad", "Fishfillet", "Garlicchips", "Hamsandwich", "Icepop", "Jambalaya",
                    "Kiwifruit", "Lambchops", "Mixedgreens", "Nachos", "Oliveoil", "Pastasalad", "Quinoa", "Ricecake", "Sausagepizza", "Tacosalad",
                    "Udonnoodlesoup", "Vegetablestirfry", "Watermelon", "Xanthangum",
                    "Arugula", "Bakedpotato", "Candy", "Doughnut", "Eggplantparmesan", "Fishfillet", "Garlicbutter", "Hamhock", "Ice cream cake", "Jambalaya",
                    "Kalesalad", "Lambstew", "Mixedberries", "Noodlesoup", "Pastasauce", "Quinoasalad", "Ricepudding", "Sausageroll", "Tacosalad",
                    "Udonnoodlesoup", "Vegetablesoup","Apricot", "Bakedbeans", "Caviar", "Doritos", "Eggsalad", "Fishfillet", "Garlicchips", "Hamsandwich", "Icepop", "Jambalaya",
                    "Kiwifruit", "Lambchops", "Mixedgreens", "Nachos", "Pastasalad", "Quinoa", "Ricecake", "Sausagepizza", "Tacosalad",
                    ]
 ,    "countries": [
                    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua",
                    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
                    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
                    "Benin", "Bhutan", "Bolivia", "Bosnia", "Botswana", "Brazil",
                    "Brunei", "Bulgaria", "BurkinaFaso", "Burundi", "CaboVerde", "Cambodia",
                    "Cameroon", "Canada", "Chad", "Chile", "China",
                    "Colombia", "Comoros", "Congo", "CostaRica", "Croatia", "Cuba", "Cyprus",
                    "CzechRepublic", "Denmark", "Djibouti", "Dominica", "Dominica",
                    "EastTimor", "Ecuador", "Egypt", "ElSalvador", "EquatorialGuinea", "Eritrea",
                    "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
                    "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
                    "Guinea", "GuineaBissau", "Guyana", "Haiti", "Honduras", "Hungary",
                    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
                    "Italy", "IvoryCoast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
                    "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
                    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
                    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                    "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
                    "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia",
                    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger",
                    "Nigeria", "NorthKorea", "NorthMacedonia", "Norway", "Oman", "Pakistan",
                    "Palau", "Panama", "PapuaNewGuinea", "Paraguay", "Peru", "Philippines",
                    "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
                    "SaintLucia", "Samoa", "SanMarino",
                    "SaudiArabia", "Senegal", "Serbia", "Seychelles",
                    "SierraLeone", "Singapore", "Slovakia", "Slovenia", "SolomonIslands", "Somalia",
                    "SouthAfrica", "SouthKorea", "SouthSudan", "Spain", "SriLanka", "Sudan",
                    "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania",
                    "Thailand", "Togo", "Tonga", "Tunisia", "Turkey",
                    "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "UnitedArabEmirates", "UnitedKingdom",
                    "UnitedStates", "Uruguay", "Uzbekistan", "Vanuatu", "VaticanCity", "Venezuela",
                    "Vietnam", "Yemen", "Zambia", "Zimbabwe"
                    ]
  ,    "films" :   [
                    "Alien", "Aladdin", "Antman", "Avatar", "BackToFuture", "Batman",
                    "BeautyAndBeast", "Blade", "Bourne", "Brave", "CaptainAmerica",
                    "Cars", "Cinderella", "Cloverfield", "Coco", "Deadpool", "DieHard",
                    "DoctorStrange", "Dunkirk", "FantasticBeasts", "FindingDory",
                    "Frozen", "Gladiator", "Godzilla", "Gravity", "Guardians",
                    "HarryPotter", "Hercules", "HomeAlone", "HotelTransylvania",
                    "Inception", "Incredibles", "IronMan", "Jaws", "JurassicPark",
                    "KillBill", "KungFuPanda", "LegoMovie", "Logan", "Madagascar",
                    "Maleficent", "ManOfSteel", "MaryPoppins", "Matrix", "Megamind",
                    "Minions", "MissionImpossible", "Moana", "MrPeabody", "Mulan",
                    "Nemo", "OzTheGreat", "PacificRim", "Pan", "Penguins", "Pirates",
                    "PitchPerfect", "Pixels", "Predator", "PrinceOfPersia", "Ratatouille",
                    "Rio", "RogueOne", "ScoobyDoo", "Shawshank", "SnowWhite", "SpiderMan",
                    "Spy", "StarTrek", "StarWars", "SuicideSquad", "Tangled", "Tarzan",
                    "TempleBall", "TheHobbit", "TheHungerGames", "TheIncredibleHulk",
                    "TheLionKing", "TheLordOfTheRings", "TheMummy", "TheRock", "Thor",
                    "ToyStory", "Transformers", "Up", "Venom", "WALLE", "WonderWoman",
                    "XMen", "Zootopia"
                    ] 
  ,  "videogames" : [
                    "Yoshi","Wildermyth","Wildermyth","WatchDogs","Wandersong","Valorant","Unworthy",
                    "Unworthy","UntitledGoose","UntilDawn","Unrailed!","Unrailed!","Unlucky","Undertale","Truberbrook","Townscaper",
                    "TowerFall","TheVanishing","TheSwapper","ThePedestrian","TheMessenger","TheGardens","Terraria","Tale",
                    "SuperSmash","SuperMeat","SuperCrush","StreetFighter","Stardew","SpiderMan","Spelunky","Sonic","Soma","Skellboy","ShovelKnight",
                    "SheDreams","Sentinels","Rust","Rocket","Roblox","Residentevil","RedDead","Recompile","Rainbow","PumpkinJack","PUBG","Pokemon","Pode",
                    "Paratopic","Oxenfree","Overwatch","Overcooked","Ori","Nidhogg","MonsterHunter","Minecraft","MegaMan","MassEffect","MarioKart","Luigi","LostEmber",
                    "LittleNightmares","Lisa","LifeisStrange","Liberated","Lacuna","Kirby","Katamari","Inside","HyperLight","Hotline","HollowKnight","Hitman","HerStory",
                    "Haven","Halo","Hades","Guacamelee","GTAV","GrowHome","Gris","Gonner","GoingUnder","GangBeasts","FrogDetective","FranBow","Fortnite",
                    "Forager","Firewatch","FinalFantasy","FelixtheReaper","FarCry","FallGuys","Everspace","Ethereal","EpicChef","EldestSouls","EarthNight","EagleIsland",
                    "Dota2","Donkey","Dishonored","DeusEx","Destiny","DeadCells","DarkSouls","Cyberpunk","Cuphead","CSGO","Crash","Borderlands","Black Ops","BioShock","Apex",
                    "AmongUs","AShortHike"," Katana"," Ark",
]                              
}


@csrf_exempt
def check_letter(request):
    global game_word
    global current_string
    global mistake



    data = json.loads(request.body)
    character = data['character']
    username_of_click = data['username']

    game = Game.objects.filter(member_model__username=username_of_click).first()
    game_word = game.game_word_model
    current_string = game.current_string_model
    mistake = game.mistakes_model

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
    

    game.game_word_model = game_word
    game.current_string_model = current_string
    game.mistakes_model = str(mistake)
    game.save(update_fields=['game_word_model', 'current_string_model', 'mistakes_model'])

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
    new_game = Game(member_model=member, game_word_model=game_word, current_string_model = current_string, mistakes_model = mistake)
    new_game.save()

    return render(request, 'index.html', {'current_string' : current_string, 'category' : random_category, 'username' : unique_id})
