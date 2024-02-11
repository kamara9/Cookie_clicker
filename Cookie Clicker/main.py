import time

import pygame
import math
from Cookie import *
from Clicker import *
from variables import *
from clickers import CLICKERS_LIST

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

cookie = Cookie(screen, cookie_color, cookie_position, cookie_size)

# cursor = Clicker(screen, cookie_color, item_position, item_size, 15, 1, 10)

COOKIE_EVENT = pygame.USEREVENT
pygame.time.set_timer(COOKIE_EVENT, 1000)
timeout = 1

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
song = pygame.mixer.Sound('stop.mp3')

item_count = 1
for clicker in CLICKERS_LIST:
    pos = [item_position[0], item_position[1] + item_size[1] * item_count]
    obj = Clicker(screen, item_color, pos, item_size, clicker.get("price"),
                  clicker.get("clicks_per_second"), clicker.get("count"), clicker.get("name"))
    clicker_list.append(obj)
    item_count+=1


def cps_sum(click_list):
    sum = 0
    for clicker in click_list:
        sum += clicker.count * clicker.clicks_per_second
    return sum

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cookie.is_hovered(mouse):
                cookies += cookies_per_click
            for clicker in clicker_list:
                if clicker.is_hovered(mouse):
                    if clicker.enough_money(cookies):
                        cookies = clicker.buy_clicker(cookies)
                        song.play()
                        time.sleep(song.get_length())

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("White")
    color = (255, 255, 255)
    # RENDER YOUR GAME HERE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        # paddle_right.move_paddle(0, speed)
        pass

    # pick a font you have and set its size
    myfont = pygame.font.SysFont("Arial", 30)
    myfont2 = pygame.font.SysFont("Arial", 12)
    # apply it to text on a label
    label1 = myfont.render("Cookies: " + str(math.trunc(cookies)), 1, (0, 0, 0))
    cps_label = myfont2.render("Cookies per second: " + str(clicks_per_second), 1, (0, 0, 0))
    # put the label object on the screen at point x=100, y=100
    screen.blit(label1, (500, 10))
    screen.blit(cps_label, (100, 10))

    if cookie.is_hovered(mouse):
        cookie.draw_cookie(cookie_light, cookie_position, cookie_size)
    else:
        cookie.draw_cookie(cookie_color, cookie_position, cookie_size)
    # cursor = Clicker(screen, cookie_color, item_position, item_size, 15, 1, 10)

    item_count = 1
    for item in clicker_list:
        pos = [item_position[0], item_position[1]+item_size[1]*item_count]
        if item.is_hovered(mouse):
            item.draw_clicker(item_light, pos, item_size, item.name)
        else:
            item.draw_clicker(item_color, pos, item_size, item.name)
        item_count += 1

    clicks_per_second = cps_sum(clicker_list)
    cookies += clicks_per_second

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
