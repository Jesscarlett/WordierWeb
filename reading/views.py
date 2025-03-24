from django.http import HttpResponse
from django.shortcuts import render
import json
import os
import random


def read(request):
    return render(request, 'read.html')


def alice_one(request):
    return render(request, 'alice_one.html')


def alice_two(request):
    return render(request, 'alice_two.html')


def alice_three(request):
    return render(request, 'alice_three.html')


def alice_four(request):
    return render(request, 'alice_four.html')

def alice_five(request):
    return render(request, 'alice_five.html')


def alice_six(request):
    return render(request, 'alice_six.html')

def alice_seven(request):
    return render(request, 'alice_seven.html')

def alice_eight(request):
    return render(request, 'alice_eight.html')

def alice_nine(request):
    return render(request, 'alice_nine.html')

def alice_ten(request):
    return render(request, 'alice_ten.html')

def alice_eleven(request):
    return render(request, 'alice_eleven.html')

def alice_twelve(request):
    return render(request, 'alice_twelve.html')

def glass_one(request):
    return render(request, 'glass_one.html')

def glass_two(request):
    return render(request, 'glass_two.html')

def glass_three(request):
    return render(request, 'glass_three.html')

def glass_four(request):
    return render(request, 'glass_four.html')

def glass_five(request):
    return render(request, 'glass_five.html')

def glass_six(request):
    return render(request, 'glass_six.html')

def glass_seven(request):
    return render(request, 'glass_seven.html')

def glass_eight(request):
    return render(request, 'glass_eight.html')

def glass_nine(request):
    return render(request, 'glass_nine.html')

def glass_ten(request):
    return render(request, 'glass_ten.html')

def glass_eleven(request):
    return render(request, 'glass_eleven.html')

def treasure_one(request):
    return render(request, 'treasure_one.html')

def treasure_two(request):
    return render(request, 'treasure_two.html')

def treasure_three(request):
    return render(request, 'treasure_three.html')

def treasure_four(request):
    return render(request, 'treasure_four.html')

def treasure_five(request):
    return render(request, 'treasure_five.html')

def treasure_six(request):
    return render(request, 'treasure_six.html')

def peter_one(request):
    return render(request, 'peter_one.html')

def peter_two(request):
    return render(request, 'peter_two.html')

def peter_three(request):
    return render(request, 'peter_three.html')

def peter_four(request):
    return render(request, 'peter_four.html')

def peter_five(request):
    return render(request, 'peter_five.html')

def peter_six(request):
    return render(request, 'peter_six.html')

def black_one(request):
    return render(request, 'black_one.html')

def black_two(request):
    return render(request, 'black_two.html')

def black_three(request):
    return render(request, 'black_three.html')

def black_four(request):
    return render(request, 'black_four.html')

def black_five(request):
    return render(request, 'black_five.html')

def black_six(request):
    return render(request, 'black_six.html')

def black_seven(request):
    return render(request, 'black_seven.html')

def black_eight(request):
    return render(request, 'black_eight.html')

def black_nine(request):
    return render(request, 'black_nine.html')

def black_ten(request):
    return render(request, 'black_ten.html')

def fairy_one(request):
    return render(request, 'fairy_one.html')


def fairy_two(request):
    return render(request, 'fairy_two.html')


def fairy_three(request):
    return render(request, 'fairy_three.html')


def fairy_four(request):
    return render(request, 'fairy_four.html')


def fairy_five(request):
    return render(request, 'fairy_five.html')


def fairy_six(request):
    return render(request, 'fairy_six.html')


def fairy_seven(request):
    return render(request, 'fairy_seven.html')


def fairy_eight(request):
    return render(request, 'fairy_eight.html')


def book(request):
    return render(request, 'book.html')


def atomic_habits(request):
    return render(request, 'atomic_habits.html')

def the_power_of_now(request):
    return render(request, 'the_power_of_now.html')

def think_and_grow_rich(request):
    return render(request, 'think_and_grow_rich.html')

def the_7_habits_of_highly_effective_people(request):
    return render(request, 'the_7_habits_of_highly_effective_people.html')

def how_to_win_friends_and_influence_people(request):
    return render(request, 'how_to_win_friends_and_influence_people.html')

def you_are_a_badass(request):
    return render(request, 'you_are_a_badass.html')

def the_four_agreements(request):
    return render(request, 'the_four_agreements.html')

def daring_greatly(request):
    return render(request, 'daring_greatly.html')

def mans_search_for_meaning(request):
    return render(request, 'mans_search_for_meaning.html')

def the_miracle_morning(request):
    return render(request, 'the_miracle_morning.html')

def deep_work(request):
    return render(request, 'deep_work.html')

def grit(request):
    return render(request, 'grit.html')

def the_subtle_art_of_not_giving_a_fck(request):
    return render(request, 'the_subtle_art_of_not_giving_a_fck.html')

def cant_hurt_me(request):
    return render(request, 'cant_hurt_me.html')

def mindset(request):
    return render(request, 'mindset.html')

def ikigai(request):
    return render(request, 'ikigai.html')

def make_your_bed(request):
    return render(request, 'make_your_bed.html')

def the_alchemist(request):
    return render(request, 'the_alchemist.html')

def the_untethered_soul(request):
    return render(request, 'the_untethered_soul.html')

def big_magic(request):
    return render(request, 'big_magic.html')

def essentialism(request):
    return render(request, 'essentialism.html')

def the_slight_edge(request):
    return render(request, 'the_slight_edge.html')

def no_excuses(request):
    return render(request, 'no_excuses.html')

def the_4_hour_workweek(request):
    return render(request, 'the_4_hour_workweek.html')

def as_a_man_thinketh(request):
    return render(request, 'as_a_man_thinketh.html')

def the_success_principles(request):
    return render(request, 'the_success_principles.html')

def start_with_why(request):
    return render(request, 'start_with_why.html')

def who_moved_my_cheese(request):
    return render(request, 'who_moved_my_cheese.html')

def the_war_of_art(request):
    return render(request, 'the_war_of_art.html')

def tools_of_titans(request):
    return render(request, 'tools_of_titans.html')

def good_to_great(request):
    return render(request, 'good_to_great.html')

def the_lean_startup(request):
    return render(request, 'the_lean_startup.html')

def blue_ocean_strategy(request):
    return render(request, 'blue_ocean_strategy.html')

def leaders_eat_last(request):
    return render(request, 'leaders_eat_last.html')

def principles_life_and_work(request):
    return render(request, 'principles_life_and_work.html')

def the_hard_thing_about_hard_things(request):
    return render(request, 'the_hard_thing_about_hard_things.html')

def measure_what_matters(request):
    return render(request, 'measure_what_matters.html')

def dare_to_lead(request):
    return render(request, 'dare_to_lead.html')

def the_innovators_dilemma(request):
    return render(request, 'the_innovators_dilemma.html')

def start_something_that_matters(request):
    return render(request, 'start_something_that_matters.html')

def extreme_ownership(request):
    return render(request, 'extreme_ownership.html')

def e_myth_revisited(request):
    return render(request, 'e_myth_revisited.html')

def the_art_of_war(request):
    return render(request, 'the_art_of_war.html')

def crushing_it(request):
    return render(request, 'crushing_it.html')

def delivering_happiness(request):
    return render(request, 'delivering_happiness.html')

def the_infinite_game(request):
    return render(request, 'the_infinite_game.html')

def built_to_last(request):
    return render(request, 'built_to_last.html')

def zero_to_one(request):
    return render(request, 'zero_to_one.html')

def the_100_startup(request):
    return render(request, 'the_100_startup.html')

def rich_dad_poor_dad(request):
    return render(request, 'rich_dad_poor_dad.html')

def profit_first(request):
    return render(request, 'profit_first.html')

def the_personal_mba(request):
    return render(request, 'the_personal_mba.html')

def what_got_you_here_wont_get_you_there(request):
    return render(request, 'what_got_you_here_wont_get_you_there.html')

def the_goal(request):
    return render(request, 'the_goal.html')

def disrupt_you(request):
    return render(request, 'disrupt_you.html')

def rework(request):
    return render(request, 'rework.html')

def made_to_stick(request):
    return render(request, 'made_to_stick.html')

def purple_cow(request):
    return render(request, 'purple_cow.html')

def linchpin(request):
    return render(request, 'linchpin.html')

def tribes(request):
    return render(request, 'tribes.html')


def thinking_fast_and_slow(request):
    return render(request, 'thinking_fast_and_slow.html')

def the_paradox_of_choice(request):
    return render(request, 'the_paradox_of_choice.html')

def influence_psychology_of_persuasion(request):
    return render(request, 'influence_psychology_of_persuasion.html')

def blink(request):
    return render(request, 'blink.html')

def the_tipping_point(request):
    return render(request, 'the_tipping_point.html')

def outliers(request):
    return render(request, 'outliers.html')

def david_and_goliath(request):
    return render(request, 'david_and_goliath.html')

def predictably_irrational(request):
    return render(request, 'predictably_irrational.html')

def drive(request):
    return render(request, 'drive.html')

def the_social_animal(request):
    return render(request, 'the_social_animal.html')

def nudge(request):
    return render(request, 'nudge.html')

def the_art_of_choosing(request):
    return render(request, 'the_art_of_choosing.html')

def scarcity(request):
    return render(request, 'scarcity.html')

def mistakes_were_made(request):
    return render(request, 'mistakes_were_made.html')

def the_happiness_hypothesis(request):
    return render(request, 'the_happiness_hypothesis.html')

def switch(request):
    return render(request, 'switch.html')

def sway(request):
    return render(request, 'sway.html')

def mindwise(request):
    return render(request, 'mindwise.html')

def born_to_be_good(request):
    return render(request, 'born_to_be_good.html')

def emotional_intelligence_2_0(request):
    return render(request, 'emotional_intelligence_2_0.html')

def sapiens(request):
    return render(request, 'sapiens.html')

def homo_deus(request):
    return render(request, 'homo_deus.html')

def a_brief_history_of_time(request):
    return render(request, 'a_brief_history_of_time.html')

def the_selfish_gene(request):
    return render(request, 'the_selfish_gene.html')

def the_immortal_life_of_henrietta_lacks(request):
    return render(request, 'the_immortal_life_of_henrietta_lacks.html')

def the_gene(request):
    return render(request, 'the_gene.html')

def the_emperor_of_all_maladies(request):
    return render(request, 'the_emperor_of_all_maladies.html')

def astrophysics_for_people_in_a_hurry(request):
    return render(request, 'astrophysics_for_people_in_a_hurry.html')

def cosmos(request):
    return render(request, 'cosmos.html')

def the_greatest_show_on_earth(request):
    return render(request, 'the_greatest_show_on_earth.html')

def the_sixth_extinction(request):
    return render(request, 'the_sixth_extinction.html')

def why_evolution_is_true(request):
    return render(request, 'why_evolution_is_true.html')

def the_hidden_life_of_trees(request):
    return render(request, 'the_hidden_life_of_trees.html')

def entangled_life(request):
    return render(request, 'entangled_life.html')

def what_if(request):
    return render(request, 'what_if.html')

def the_body(request):
    return render(request, 'the_body.html')

def a_short_history_of_nearly_everything(request):
    return render(request, 'a_short_history_of_nearly_everything.html')

def life_on_the_edge(request):
    return render(request, 'life_on_the_edge.html')

def the_order_of_time(request):
    return render(request, 'the_order_of_time.html')

def reality_is_not_what_it_seems(request):
    return render(request, 'reality_is_not_what_it_seems.html')

def the_elegant_universe(request):
    return render(request, 'the_elegant_universe.html')

def the_fabric_of_the_cosmos(request):
    return render(request, 'the_fabric_of_the_cosmos.html')

def until_the_end_of_time(request):
    return render(request, 'until_the_end_of_time.html')

def being_mortal(request):
    return render(request, 'being_mortal.html')

def complications(request):
    return render(request, 'complications.html')

def better(request):
    return render(request, 'better.html')

def the_checklist_manifesto(request):
    return render(request, 'the_checklist_manifesto.html')

def silent_spring(request):
    return render(request, 'silent_spring.html')

def guns_germs_and_steel(request):
    return render(request, 'guns_germs_and_steel.html')

def collapse(request):
    return render(request, 'collapse.html')

def the_uninhabitable_earth(request):
    return render(request, 'the_uninhabitable_earth.html')

def braiding_sweetgrass(request):
    return render(request, 'braiding_sweetgrass.html')

def we_are_the_weather(request):
    return render(request, 'we_are_the_weather.html')

def on_the_origin_of_species(request):
    return render(request, 'on_the_origin_of_species.html')

def the_disordered_cosmos(request):
    return render(request, 'the_disordered_cosmos.html')

def lifes_edge(request):
    return render(request, 'lifes_edge.html')

def the_tangled_tree(request):
    return render(request, 'the_tangled_tree.html')

def i_contain_multitudes(request):
    return render(request, 'i_contain_multitudes.html')

def an_immense_world(request):
    return render(request, 'an_immense_world.html')

def the_infinite_machine(request):
    return render(request, 'the_infinite_machine.html')

def when_breath_becomes_air(request):
    return render(request, 'when_breath_becomes_air.html')

def do_no_harm(request):
    return render(request, 'do_no_harm.html')

def why_we_get_sick(request):
    return render(request, 'why_we_get_sick.html')

def the_omnivores_dilemma(request):
    return render(request, 'the_omnivores_dilemma.html')

def in_defense_of_food(request):
    return render(request, 'in_defense_of_food.html')

def cooked(request):
    return render(request, 'cooked.html')

def this_is_your_mind_on_plants(request):
    return render(request, 'this_is_your_mind_on_plants.html')

def how_to_change_your_mind(request):
    return render(request, 'how_to_change_your_mind.html')

def inconvenient_truth(request):
    return render(request, 'inconvenient_truth.html')

def the_climate_book(request):
    return render(request, 'the_climate_book.html')

def a_peoples_history_of_the_united_states(request):
    return render(request, 'a_peoples_history_of_the_united_states.html')

def the_silk_roads(request):
    return render(request, 'the_silk_roads.html')

def the_wright_brothers(request):
    return render(request, 'the_wright_brothers.html')

def team_of_rivals(request):
    return render(request, 'team_of_rivals.html')

def alexander_hamilton(request):
    return render(request, 'alexander_hamilton.html')

def the_lessons_of_history(request):
    return render(request, 'the_lessons_of_history.html')

def historical_1776(request):
    return render(request, '1776.html')

def the_warmth_of_other_suns(request):
    return render(request, 'the_warmth_of_other_suns.html')

def caste(request):
    return render(request, 'caste.html')

def the_dawn_of_everything(request):
    return render(request, 'the_dawn_of_everything.html')

def the_splendid_and_the_vile(request):
    return render(request, 'the_splendid_and_the_vile.html')

def dead_wake(request):
    return render(request, 'dead_wake.html')

def in_the_garden_of_beasts(request):
    return render(request, 'in_the_garden_of_beasts.html')

def devil_in_the_white_city(request):
    return render(request, 'devil_in_the_white_city.html')

def the_diary_of_a_young_girl(request):
    return render(request, 'the_diary_of_a_young_girl.html')

def night(request):
    return render(request, 'night.html')

def the_rise_and_fall_of_the_third_reich(request):
    return render(request, 'the_rise_and_fall_of_the_third_reich.html')

def the_great_influenza(request):
    return render(request, 'the_great_influenza.html')

def a_distant_mirror(request):
    return render(request, 'a_distant_mirror.html')

def the_guns_of_august(request):
    return render(request, 'the_guns_of_august.html')

def stalingrad(request):
    return render(request, 'stalingrad.html')

def berlin_the_downfall(request):
    return render(request, 'berlin_the_downfall.html')

def the_second_world_war(request):
    return render(request, 'the_second_world_war.html')

def the_first_world_war(request):
    return render(request, 'the_first_world_war.html')

def a_world_undone(request):
    return render(request, 'a_world_undone.html')

def the_history_of_the_ancient_world(request):
    return render(request, 'the_history_of_the_ancient_world.html')

def the_making_of_the_atomic_bomb(request):
    return render(request, 'the_making_of_the_atomic_bomb.html')

def the_pioneers(request):
    return render(request, 'the_pioneers.html')

def the_path_between_the_seas(request):
    return render(request, 'the_path_between_the_seas.html')

def over_the_edge_of_the_world(request):
    return render(request, 'over_the_edge_of_the_world.html')

def the_immortal_irishman(request):
    return render(request, 'the_immortal_irishman.html')

def killers_of_the_flower_moon(request):
    return render(request, 'killers_of_the_flower_moon.html')

def empire_of_pain(request):
    return render(request, 'empire_of_pain.html')

def say_nothing(request):
    return render(request, 'say_nothing.html')

def the_code_breaker(request):
    return render(request, 'the_code_breaker.html')

def einstein_his_life_and_universe(request):
    return render(request, 'einstein_his_life_and_universe.html')

def leonardo_da_vinci(request):
    return render(request, 'leonardo_da_vinci.html')

def steve_jobs(request):
    return render(request, 'steve_jobs.html')

def benjamin_franklin(request):
    return render(request, 'benjamin_franklin.html')

def the_innovators(request):
    return render(request, 'the_innovators.html')

def born_a_crime(request):
    return render(request, 'born_a_crime.html')

def long_walk_to_freedom(request):
    return render(request, 'long_walk_to_freedom.html')

def the_book_thief(request):
    return render(request, 'the_book_thief.html')

def band_of_brothers(request):
    return render(request, 'band_of_brothers.html')

def undaunted_courage(request):
    return render(request, 'undaunted_courage.html')

def no_ordinary_time(request):
    return render(request, 'no_ordinary_time.html')