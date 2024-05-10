# Space_Invader
This is a mini game that developed using python, specially using pygame module.
you can enjoy the game by clone this repo and run

If you haven't install pygame module previously, please install it using <br/>
    **pip install pygame** <br/>command , before run the file.

This code is a basic implementation of a 2D space shooter game using the Pygame library in Python. Let's break down its components:

1. **Initialization**: 
   - Pygame is initialized.
   - A display surface of size 800x600 pixels is created.
   - Title and icon for the game window are set.

2. **Player Setup**:
   - The player's spaceship is loaded and its initial position is set.
   - Variables for player movement (`playerxchange` and `playerychange`) are initialized.

3. **Enemy Setup**:
   - Initially, a single enemy is created. Later, it's extended to multiple enemies.
   - For multiple enemies, lists are used to store their properties (`enemyimg`, `enemyx`, `enemyy`, `enemyxchange`, and `enemyychange`).

4. **Bullet Setup**:
   - Bullet properties (`bulletimg`, `bulletx`, `bullety`, `bulletxchange`, `bulletychange`, `bullet_state`) are initialized.

5. **Function Definitions**:
   - Functions are defined to draw the player, enemies, bullets, and to detect collisions.
   - `show_score` function displays the player's score.

6. **Main Game Loop**:
   - The game loop (`while running`) handles user input, updates game elements, and renders them on the screen.

7. **Event Handling**:
   - The loop checks for events like key presses and mouse clicks. Player movement and bullet firing are controlled by keyboard inputs.
   - When the space key is pressed, a bullet is fired from the player's position.

8. **Player Movement**:
   - Player movement is handled based on key presses. The player's position is updated within the boundaries of the game window.

9. **Enemy Movement**:
   - Enemies move horizontally across the screen. When they reach the edges, they move downwards and change direction.

10. **Collision Detection**:
   - Collision between the bullet and enemies is detected using distance calculation. When a collision occurs, the enemy is respawned at a random position and the score is incremented.

11. **Bullet Firing**:
   - When the space key is pressed, the bullet is fired from the player's position towards the top of the screen. The bullet's position is updated in subsequent frames until it reaches the top.

12. **Rendering**:
   - All game elements (player, enemies, bullets) are drawn onto the screen surface.
   - The player's score is displayed on the screen.

13. **Updating Display**:
   - The display is updated to show the latest changes in the game.

This code forms the core of a simple space shooter game, where the player controls a spaceship to shoot down enemies while avoiding collisions.