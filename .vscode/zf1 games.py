import random
import turtle

# Setup screen
screen = turtle.Screen()
screen.title("F1 3D Perspective Arcade")
screen.setup(480, 700)
screen.bgcolor("#1a1a1a")
screen.tracer(0)

# Game State Variables
score = 0
lives = 3
game_over = False
game_speed = 4.5
moving_left = False
moving_right = False
invincible_timer = 0

# Player F1 Car
player = turtle.Turtle()
player.shape("square")
player.color("red")
player.shapesize(stretch_wid=3.0, stretch_len=1.4)
player.penup()
player.goto(0, -220)

# 3D Obstacle Cars List
obstacles = []


def spawn_obstacle():
  lanes = [-90, 0, 90]
  obs = turtle.Turtle()
  obs.shape("square")
  obs.color(random.choice(["dodger blue", "gold", "orange", "magenta", "cyan"]))
  obs.penup()
  # Start far away (small scale, near the horizon)
  obs.goto(random.choice(lanes), 180)
  obs.z_depth = 0.1  # Starts far away (depth from 0.1 to 1.0)
  obs.lane_x = obs.xcor()
  obstacles.append(obs)


# Smooth continuous controls
def set_left_true():
  global moving_left
  moving_left = True


def set_left_false():
  global moving_left
  moving_left = False


def set_right_true():
  global moving_right
  moving_right = True


def set_right_false():
  global moving_right
  moving_right = False


def reset_game():
  global score, lives, game_over, game_speed, obstacles
  score = 0
  lives = 3
  game_speed = 4.5
  game_over = False
  player.goto(0, -220)
  for obs in obstacles:
    obs.hideturtle()
  obstacles.clear()
  hud.clear()


screen.listen()
screen.onkeypress(set_left_true, "Left")
screen.onkeyrelease(set_left_false, "Left")
screen.onkeypress(set_right_true, "Right")
screen.onkeyrelease(set_right_false, "Right")
screen.onkey(reset_game, "r")
screen.onkey(reset_game, "R")

# Heads Up Display (HUD)
hud = turtle.Turtle()
hud.hideturtle()
hud.color("white")
hud.penup()
hud.goto(-210, 320)


def update_hud():
  hud.clear()
  hud.write(
      "Lives: "
      + str(lives)
      + "   Score: "
      + str(int(score))
      + "\nControls: Left/Right to steer | Press 'R' to Restart",
      font=("Arial", 11, "bold"),
  )


frame_count = 0

# Main Game Loop
while True:
  if not game_over:
    frame_count += 1

    if invincible_timer > 0:
      invincible_timer -= 1
      player.color("orange" if invincible_timer % 4 == 0 else "red")
    else:
      player.color("red")

    # Smooth steering movement
    if moving_left and player.xcor() > -100:
      player.setx(player.xcor() - 7)
    if moving_right and player.xcor() < 100:
      player.setx(player.xcor() + 7)

    # Spawn obstacles
    if frame_count % 40 == 0:
      spawn_obstacle()

    # Update 3D Perspective Obstacles
    for obs in obstacles[:]:
      # Increase depth to simulate coming closer toward the camera
      obs.z_depth += 0.015 * (game_speed / 4.0)

      # Project 3D coordinates onto 2D screen based on depth scaling
      # As z_depth goes from 0.1 (horizon) to 1.0 (foreground), car gets bigger and spreads out from center
      screen_y = 180 - (
          390 * obs.z_depth
      )  # moves down from y=180 to y=-210
      screen_x = obs.lane_x * (
          obs.z_depth * 1.5
      )  # widens out as it approaches

      obs.goto(screen_x, screen_y)

      # Scale size dynamically to create 3D depth illusion
      w_size = max(0.5, obs.z_depth * 3.0)
      h_size = max(0.5, obs.z_depth * 3.0)
      obs.shapesize(stretch_wid=h_size * 2, stretch_len=w_size * 1.2)

      # Collision detection when car reaches the foreground (z_depth close to 1.0)
      if obs.z_depth > 0.85 and player.distance(obs) < 45:
        if invincible_timer == 0:
          lives -= 1
          if lives <= 0:
            game_over = True
            hud.goto(0, 0)
            hud.write(
                "CRASH! GAME OVER\n\nFinal Score: "
                + str(int(score))
                + "\n\nPress 'R' to Play Again",
                align="center",
                font=("Arial", 16, "bold"),
            )
          else:
            invincible_timer = 90
            obs.hideturtle()
            obstacles.remove(obs)

      # Remove passed obstacles
      if obs.z_depth > 1.1:
        obs.hideturtle()
        obstacles.remove(obs)
        score += 10

    # Increase game speed gradually
    game_speed = 4.5 + (score / 150)
    update_hud()
    screen.update()

  turtle.time.sleep(0.015)
  