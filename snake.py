# بسم الله الرحمن الرحيم
# import modules necessary for the game 
import random
import curses

# initialize the curses library to create our screen
screen = curses.initscr()

# hide the mouse cursor
curses.curs_set(0)

# getmax screen height and width
screen_height, screen_width = screen.getmaxyx()

# create a new window
window = curses.newwin(screen_height, screen_width, 0, 0 )

# allow window to receive input from keyboard
window.keypad(1)

# set the delay for updating the screen
window.timeout(125)

# set the x.y coordinates of the initial position of snake's head
snk_x = screen_width // 4
snk_y = screen_height // 2

# define the initial posisiton of the snake body
snake = [
  [snk_y, snk_x], #head
  [snk_y, snk_x-1], #belly
  [snk_y, snk_x-2], #tail
]

# creat the food in the middle of window
food = [screen_height // 2, screen_width // 2]

# add the food by using PI character from curses module
window.addch(food[0], food[1], curses.ACS_PI)

# set initial movement direction to right
key = curses.KEY_RIGHT

# create a game loop that loops Forever Until the player loses or quite the game
while True:
  
  # get the next key that will be pressed by user
  next_key = window.getch()
  
  # if user doesn't input abything, key remains same, else key will be set to the new pressed key
  key = key if next_key == -1 else next_key

  # check if snake collided with the walls or itself
  if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
    curses.endwin() #closing the window
    quit() #exit the program

  # set the new position of the snakehead based on the direction
  new_head = [snake[0][0], snake[0][1]]

  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1

  # insert the new head into the first position of the snake list
  snake.insert(0, new_head)

  # check if the snake ate the food
  if snake[0] == food:
    food = None #remov food if snake ate it
    
    # while food is removed generate new food in a random place on the screen
  while food is None:
    new_food = [
    random.randint(1, screen_height-1),
    random.randint(1, screen_width-1),
      ]
    #set the food to new food if the new food generated is not in the snake body and add it to the screen
    food = new_food if new_food not in snake else None
    window.addch(food[0], food[1], curses.ACS_PI)
  # otherwise, remove the last segment of the snake body 
  else:
    tail = snake.pop()
    window.addch(tail[0], tail[1], ' ')

#update the position of the snake on the screen
  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)