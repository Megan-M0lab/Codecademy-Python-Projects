gamers = []

def add_gamer(gamer, gamers_list):
    if "name" and "availability" in gamer.keys():
        gamers_list.append(gamer)

def build_daily_frequency_table():
    return {"Monday" : 0, "Tuesday" : 0, "Wednesday": 0, "Thursday" : 0, "Friday" : 0, "Saturday" : 0, "Sunday" : 0}

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1

def find_best_night(availability_table):
    return max(availability_table)

def available_on_night(gamers_list, day):
    return [gamer['name'] for gamer in gamers_list if day in gamer ['availability']]

def send_email(gamers_who_can_attend, day, game):
    for player in gamers_who_can_attend:
        print(form_email.format(name=player, day_of_week=day, game=game))


kimberly = {'name' : 'Kimberly Warner', 'availability' : ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


count_availability = build_daily_frequency_table()

calculate_availability(gamers, count_availability)

game_night = find_best_night(count_availability)

print(game_night)

attending_game_night = available_on_night(gamers, game_night)

print(attending_game_night)


form_email = "Hello {name}! Our next game night will be on {day_of_week}. We will be playing {game}. Hope to see you there!"

send_email(attending_game_night, game_night, "Abruptly Goblins!")

unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]

second_night_availability = build_daily_frequency_table()

calculate_availability(unable_to_attend_best_night, second_night_availability)

second_night = find_best_night(second_night_availability)

print(second_night)