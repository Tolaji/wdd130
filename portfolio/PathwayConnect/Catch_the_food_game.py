
import random
import pygame
import cv2

#Initialize Pygame
pygame.init()

# Set up game window
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Food")

# Load images
player_img = pygame.image.load("player.png").convert_alpha()
food_img = pygame.image.load("food.png").convert_alpha()
game_over_img = pygame.image.load("game_over.png").convert_alpha()

# Set up player character
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10
player_speed = 5

# Set up falling food
food_rect = food_img.get_rect()
food_rect.centerx = WIDTH // 2
food_rect.top = 0
food_speed = 2

# Initialize motion detection
cap = cv2.VideoCapture(0)
_, frame = cap.read()
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
prev_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

# Set up game state
score = 0
lives = 3
game_over = False

# Set up font
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Update player position based on user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += player_speed

        # Update player position based on motion detection
        _, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
        frame_diff = cv2.absdiff(prev_frame, gray_frame)
        _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_contour)
            player_rect.centerx = x + w // 2

        prev_frame = gray_frame

        # Update falling food position
        food_rect.y += food_speed
        if food_rect.top > HEIGHT:
            food_rect.top = 0
            food_rect.centerx = pygame.randint(0, WIDTH)

        # Check for collisions with food
        if player_rect.colliderect(food_rect):
            score += 1
            food_rect.top = 0
            food_rect.centerx = pygame.randint(0, WIDTH)

        # Check for game over
        if food_rect.bottom > HEIGHT:
            lives -= 1
            food_rect.top = 0
            food_rect.centerx = pygame.randint(0, WIDTH)
            if lives == 0:
                game_over = True

    # Draw game objects
    win.fill((255, 255, 255))
    win.blit(player_img, player_rect)
    win.blit(food_img, food_rect)
    score_text = font.render("Score: " + str(score), True)
