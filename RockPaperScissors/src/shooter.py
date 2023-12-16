import pygame
import random

# Constants
WIDTH, HEIGHT = 900,600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 45

PAPER = "./images/paper.jpg"
ROCK = "./images/rock.png"
SCISSOR = "./images/scissors.jpg"

MAX_PAPERS = 35
MAX_SCISSORS = 35
MAX_ROCKS = 35

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
VEL = 5
Objects = []

# Initializing pygame
pygame.init()
pygame.font.init()

# Display setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Good Luck')

# Fonts and text setup
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
font2 = pygame.font.SysFont('chalkduster.ttf', 40)
text1 = font1.render('Kill Them All', True, (0, 255, 0))
text2 = font2.render('KILL THEM ALL', True, (0, 255, 0))
textRect1 = text1.get_rect(center=(250, 250))
textRect2 = text2.get_rect(center=(250, 300))


class Paper:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        self.beatsRock = True
        self.beatsScissors = False
        self.direction = "up"
        self.x = x
        self.y = y
        self.speed = VEL

    def move(self):

        if (self.direction == "up") and (self.y - self.speed > 10):
            self.y -= self.speed
            self.rect.y -= self.speed
        elif (self.direction == "down") and (self.y + self.speed < HEIGHT-10):
            self.y += self.speed
            self.rect.y += self.speed
        elif (self.direction == "left") and (self.x - self.speed > 10):
            self.x -= self.speed
            self.rect.x -= self.speed
        elif (self.direction == "right") and (self.x + self.speed < WIDTH-10):
            self.x += self.speed
            self.rect.x += self.speed

        if self.x > WIDTH:
            self.x = WIDTH - PLAYER_WIDTH
        elif self.x < 0:
            self.x = 0 + PLAYER_WIDTH
        elif self.y > HEIGHT:
            self.y = HEIGHT - PLAYER_HEIGHT
        elif self.y < 0:
            self.y = 0 + PLAYER_HEIGHT
    
            

        if random.randint(1, 5) == 1:
            self.direction = random.choice(["up", "down", "left", "right"])

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))

class Rock:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        self.beatsScissors = True
        self.beatsPaper = False
        self.direction = "down"
        self.x = x
        self.y = y
        self.speed = VEL

    def move(self):
        if (self.direction == "up") and (self.y - self.speed > 10):
            self.y -= self.speed
            self.rect.y -= self.speed
        elif (self.direction == "down") and (self.y + self.speed < HEIGHT-10):
            self.y += self.speed
            self.rect.y += self.speed
        elif (self.direction == "left") and (self.x - self.speed > 10):
            self.x -= self.speed
            self.rect.x -= self.speed
        elif (self.direction == "right") and (self.x + self.speed < WIDTH-10):
            self.x += self.speed
            self.rect.x += self.speed

        if random.randint(1, 5) == 1:
            self.direction = random.choice(["up", "down", "left", "right"])

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))

class Scissor:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(pygame.image.load(image_path), (width, height))
        self.beatsPaper = True
        self.beatsRock = False
        self.direction = "left"
        self.x = x
        self.y = y
        
        self.speed = VEL

    def move(self):
        if (self.direction == "up") and (self.y - self.speed > 10):
            self.y -= self.speed
            self.rect.y -= self.speed
        elif (self.direction == "down") and (self.y + self.speed < HEIGHT-20):
            self.y += self.speed
            self.rect.y += self.speed
        elif (self.direction == "left") and (self.x - self.speed > 10):
            self.x -= self.speed
            self.rect.x -= self.speed
        elif (self.direction == "right") and (self.x + self.speed < WIDTH-20):
            self.x += self.speed
            self.rect.x += self.speed

        if random.randint(1, 5) == 1:
            self.direction = random.choice(["up", "down", "left", "right"])

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


def handle_collisions(papers, rocks, scissors):
    for paper in papers:
        for rock in rocks:
            if pygame.Rect.colliderect(paper.rect, (rock.rect)):
                print("Paper killed rock")
                if rock in rocks:
                    rocks.remove(rock)
                if len(papers) < MAX_PAPERS:
                    papers.append(Paper(paper.x + 10, paper.y - 5, PLAYER_WIDTH, PLAYER_HEIGHT, PAPER))
        for scissor in scissors:
            if pygame.Rect.colliderect(paper.rect, scissor.rect):
                print("SCISSOR killed paper")
                if paper in papers:
                    papers.remove(paper)
                if len(scissors) < MAX_SCISSORS:
                    scissors.append(Scissor(scissor.x + 10, scissor.y -5, PLAYER_WIDTH, PLAYER_HEIGHT, SCISSOR))

    for rock in rocks:
        for scissor in scissors:
            if pygame.Rect.colliderect(rock.rect, scissor.rect):
                print("rock killed scissor")
                if scissor in scissors:
                    scissors.remove(scissor)
                if len(rocks) < MAX_ROCKS:
                    rocks.append(Rock(rock.x + 10, rock.y -5, PLAYER_WIDTH, PLAYER_HEIGHT, ROCK))



# Main function
def main():
    clock = pygame.time.Clock()

    papers = [Paper(650, 350, PLAYER_WIDTH, PLAYER_HEIGHT, PAPER) for _ in range(10)]
    rocks = [Rock(300 + 10, HEIGHT - 500, PLAYER_WIDTH, PLAYER_HEIGHT, ROCK) for _ in range(10)]
    scissors = [Scissor(500, HEIGHT - 500, PLAYER_WIDTH, PLAYER_HEIGHT, SCISSOR) for _ in range(10)]
    Objects.extend([*papers, *rocks, *scissors])

    run = True
    while run:
        WIN.fill(BLACK)
        WIN.blit(text1, textRect1)
        WIN.blit(text2, textRect2)
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # keys pressed can be used for user interaction
        
        ran = random.randint(2, 10)
        ran = 1/ran
        

        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_w]:
            rocks.append(Rock(WIDTH * ran, HEIGHT * ran, PLAYER_WIDTH, PLAYER_HEIGHT, ROCK))
        elif keysPressed[pygame.K_a]:
            papers.append(Paper(WIDTH * ran, HEIGHT * ran, PLAYER_WIDTH, PLAYER_HEIGHT, PAPER))
        elif keysPressed[pygame.K_d]:
            scissors.append(Scissor(WIDTH * ran, HEIGHT * ran, PLAYER_WIDTH, PLAYER_HEIGHT, SCISSOR))

        handle_collisions(papers, rocks, scissors)


        for paper in papers:
            paper.draw()
            paper.move()

        for rock in rocks:
            rock.draw()
            rock.move()

        for scissor in scissors:
            scissor.draw()
            scissor.move()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
