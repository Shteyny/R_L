import random

import pygame as py
from fight_creatures import hero_fight


def fight_scene(screen, clock, FPS, enemies, hero):   # hero = класс героя для боя
    game = True                                        # enemies = [классы противников]

    def print_text(message, x, y, font_size, font_color=(255, 255, 255),
                   font_type=None):  # функция для отрисовки текста
        font_type = py.font.Font(font_type, font_size)
        text = font_type.render(message, True, font_color)
        screen.blit(text, (x, y))

    for i in range(len(enemies)):
        enemies[i].position(i)

    hero_hp = hero.give_health()
    hero_ab = hero.give_ability()
    hero_exp = hero.give_experience()
    hero_it = []                  # нужны шмотки для героя
    all_actions = [[hero_ab, "способности"], [hero_it, "предметы"]]
    action = all_actions
    while game:
        screen.fill((0, 0, 0))
        clock.tick(FPS)
        for i in enemies:
            i.otris()
        print_text("exp: {}".format(hero_exp), 25, 570, 30)
        print_text("hp: {}".format(hero_hp), 25, 600, 30)
        for i in range(len(action)):
            print_text("{} - {}".format(i + 1, action[i][1]), 120 + 250 * (i % 2), 570 + 30 * (i // 2), 30)
        hero.otris()
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    action = all_actions
                elif event.key == py.K_1:
                    if action == all_actions:
                        action = all_actions[0][0]
                elif event.key == py.K_2:
                    if action == all_actions:
                        action = all_actions[1][0]
        py.display.update()
