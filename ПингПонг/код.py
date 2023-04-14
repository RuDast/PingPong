import pygame


pygame.init()

fps = 60

win = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Ping Pong")

obj1 = pygame.Rect(100, 0, 25, 100)
obj2 = pygame.Rect(675, 0, 25, 100)

dy1 = 0
dy2 = 0
speed_player1 = 5
speed_player2 = 5
speed_boll = 4
y1 = 0
y2 = 0

dir_x, dir_y = -1, 1
cx, cy = 400, 200

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    win.fill((35, 47, 110))
    pygame.draw.line(win, "Gray", (70, 0), (70, 400), 5)
    pygame.draw.line(win, "Gray", (730, 0), (730, 400), 5)
    pygame.draw.rect(win, 'Red', pygame.Rect.move(obj1, 0, y1 + dy1 * speed_player1))
    pygame.draw.rect(win, "Green", pygame.Rect.move(obj2, 0, y2 + dy2 * speed_player2))
    y1 += dy1 * speed_player1
    y2 += dy2 * speed_player2

    k1 = [y1 + dy1 * speed_player1, y1 + dy1 * speed_player1 + 100]
    k2 = [y2 - 10 + dy2 * speed_player1, y2 + dy2 * speed_player2 + 90]

    if cx == 0 or cx == 800:
        cx = 400
        cy = 200
    if 110 < cx < 140 and k1[0] < cy < k1[1]:
        dir_x = -dir_x
    if 690 > cx > 660 and k2[0] < cy < k2[1]:
        dir_x = -dir_x
    if cy + speed_boll * dir_y > 390:
        dir_y = -dir_y
    if cy + speed_boll * dir_y < 10:
        dir_y = -dir_y

    cx += speed_boll * dir_x
    cy += speed_boll * dir_y

    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN] and y1 + dy1 * speed_player1 <= 300:
        dy1 = 1
    elif key[pygame.K_UP] and y1 + dy1 * speed_player1 >= 0:
        dy1 = -1
    else:
        dy1 = 0

    if key[pygame.K_s] and y2 + dy2 * speed_player2 <= 300:
        dy2 = 1
    elif key[pygame.K_w] and y2 + dy2 * speed_player2 >= 0:
        dy2 = -1
    else:
        dy2 = 0

    pygame.draw.circle(win, 'Yellow', (cx + speed_boll * dir_x, cy + speed_boll * dir_y), 10)

    clock.tick(fps)
    pygame.display.update()

pygame.quit()
