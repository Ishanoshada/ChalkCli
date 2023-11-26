import time
import math
import random
import re

class Chalk:
    """A Python package for terminal text styling and coloring."""

    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    REVERSED = "\033[7m"
    STRIKETHROUGH = "\033[9m"

    LIGHT_GRAY = "\033[37m"
    DARK_GRAY = "\033[90m"

    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_CYAN = "\033[96m"

    FAINT = "\033[2m"
    BLINK = "\033[5m"
    DOUBLE_UNDERLINE = "\033[21m"

    @staticmethod
    def format_text(text, styles=None, color=None):
        style_str = "".join(styles) if styles else ""
        color_str = color if color else ""
        return f"{style_str}{color_str}{text}{Chalk.RESET}"

    @staticmethod
    def colorized_banner(text, styles=None, color=None, banner_char="*"):
        banner_line = banner_char * len(text)
        banner = f"{banner_line}\n{text}\n{banner_line}"
        return Chalk.format_text(banner, styles, color)

    @staticmethod
    def rainbow_text(text):
        rainbow_colors = [
            Chalk.RED, Chalk.LIGHT_RED,
            Chalk.YELLOW, Chalk.LIGHT_YELLOW,
            Chalk.GREEN, Chalk.LIGHT_GREEN,
            Chalk.CYAN, Chalk.LIGHT_CYAN,
            Chalk.BLUE, Chalk.LIGHT_BLUE,
            Chalk.MAGENTA, Chalk.LIGHT_MAGENTA,
        ]

        rainbow_text = ""
        for i, char in enumerate(text):
            color = rainbow_colors[i % len(rainbow_colors)]
            rainbow_text += Chalk.format_text(char, color=color)

        return rainbow_text

    @staticmethod
    def create_table(header, data):
        table = f"{Chalk.BOLD}{Chalk.UNDERLINE}{header}{Chalk.RESET}\n"

        for row in data:
            table += " | ".join(row) + "\n"

        return table

    @staticmethod
    def typewriter_text(text, delay=0.1):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def pulsating_text(text, period=1):
        amplitude = 0.5
        frequency = 2 * math.pi / period
        while True:
            for i, char in enumerate(text):
                intensity = amplitude * math.sin(frequency * i) + amplitude + 1
                color = Chalk.interpolate_color(Chalk.LIGHT_CYAN, Chalk.LIGHT_RED, intensity)
                print(Chalk.format_text(char, color=color), end='', flush=True)
            print('\r', end='', flush=True)
            time.sleep(0.1)

    @staticmethod
    def blinking_text(text, blink_duration=1):
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time % (2 * blink_duration) < blink_duration:
                print(text, end='', flush=True)
            else:
                print(' ' * len(text), end='', flush=True)
            print('\r', end='', flush=True)
            time.sleep(0.1)

    @staticmethod
    def rotating_text(text, rotations=5):
        for _ in range(rotations):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(0.05)
                print('\r' + ' ' * len(text), end='', flush=True)
                time.sleep(0.05)

    @staticmethod
    def bouncing_ball(rows=10, columns=20, ball_char="O"):
        ball_position = [0, 0]
        velocity = [1, 1]

        while True:
            for i in range(rows):
                for j in range(columns):
                    if i == ball_position[0] and j == ball_position[1]:
                        print(ball_char, end='', flush=True)
                    else:
                        print(' ', end='', flush=True)
                print()
            
            ball_position[0] += velocity[0]
            ball_position[1] += velocity[1]

            if ball_position[0] == 0 or ball_position[0] == rows - 1:
                velocity[0] *= -1
            if ball_position[1] == 0 or ball_position[1] == columns - 1:
                velocity[1] *= -1

            time.sleep(0.1)
            print('\033[H')  # Move the cursor to the top-left corner

    @staticmethod
    def dynamic_background(rows=15, columns=30):
        while True:
            for i in range(rows):
                for j in range(columns):
                    color = random.choice([Chalk.RED, Chalk.GREEN, Chalk.BLUE, Chalk.YELLOW, Chalk.CYAN, Chalk.MAGENTA])
                    print(Chalk.format_text(' ', color=color), end='', flush=True)
                print()
            time.sleep(0.2)
            print('\033[H')  # Move the cursor to the top-left corner

    @staticmethod
    def scrolling_text(text, scroll_speed=0.1):
        padding = " " * len(text)
        text_with_padding = f"{padding}{text}{padding}"
        text_length = len(text_with_padding)
        
        while True:
            for i in range(text_length):
                substring = text_with_padding[i:i+len(text)]
                print(substring, end='\r', flush=True)
                time.sleep(scroll_speed)

    @staticmethod
    def center_text(text, width=80):
        padding = " " * ((width - len(text)) // 2)
        centered_text = f"{padding}{text}{padding}"
        print(centered_text)

    @staticmethod
    def fading_text(text, fade_duration=5):
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time < fade_duration:
                intensity = 1 - elapsed_time / fade_duration
                color = Chalk.interpolate_color(Chalk.LIGHT_CYAN, Chalk.LIGHT_RED, intensity)
                print(Chalk.format_text(text, color=color), end='\r', flush=True)
            else:
                break

    @staticmethod
    def progress_bar(progress, length=30):
        filled_length = int(length * progress)
        bar = f"[{'#' * filled_length}{'.' * (length - filled_length)}] {progress * 100:.1f}%"
        print(bar, end='\r', flush=True)

    @staticmethod
    def random_color_text(text):
        for char in text:
            color = random.choice([Chalk.RED, Chalk.GREEN, Chalk.BLUE, Chalk.YELLOW, Chalk.CYAN, Chalk.MAGENTA])
            print(Chalk.format_text(char, color=color), end='', flush=True)
            time.sleep(0.1)
        print()

    @staticmethod
    def countdown(seconds):
        for i in range(seconds, 0, -1):
            print(f"Time left: {i} seconds", end='\r', flush=True)
            time.sleep(1)
        print("Countdown complete!")

    @staticmethod
    def bar_chart(data):
        max_value = max(data)
        for value in data:
            bar_length = int(value / max_value * 30)
            bar = f"{'#' * bar_length}{'.' * (30 - bar_length)} {value}"
            print(bar)

    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            row_str = ' '.join(map(str, row))
            print(row_str)

    @staticmethod
    def print_chessboard(size=8):
        for i in range(size):
            row = " ".join(["■" if (i + j) % 2 == 0 else "□" for j in range(size)])
            print(row)

    @staticmethod
    def print_spiral(rows=10, columns=10):
        matrix = [[' ' for _ in range(columns)] for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        row, col = 0, 0

        for i in range(1, rows * columns + 1):
            matrix[row][col] = str(i)
            next_row, next_col = row + directions[direction][0], col + directions[direction][1]

            if (
                0 <= next_row < rows and
                0 <= next_col < columns and
                matrix[next_row][next_col] == ' '
            ):
                row, col = next_row, next_col
            else:
                direction = (direction + 1) % 4
                row, col = row + directions[direction][0], col + directions[direction][1]

        Chalk.print_matrix(matrix)

    @staticmethod
    def print_star_pattern(size=5):
        for i in range(1, size + 1):
            spaces = ' ' * (size - i)
            stars = '*' * (2 * i - 1)
            print(f"{spaces}{stars}")

    @staticmethod
    def print_hexagonal_pattern(size=5):
        for i in range(size, 0, -1):
            spaces = ' ' * (size - i)
            stars = '*' * (2 * i - 1)
            print(f"{spaces}{stars}")

        for i in range(2, size + 1):
            spaces = ' ' * (size - i)
            stars = '*' * (2 * i - 1)
            print(f"{spaces}{stars}")

    @staticmethod
    def print_multiplication_table(n=9):
        for i in range(1, n + 1):
            row = [f"{i * j:2}" for j in range(1, n + 1)]
            print(" ".join(row))

    @staticmethod
    def print_random_walk(steps=20):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = 0, 0

        for _ in range(steps):
            direction = random.choice(directions)
            row += direction[0]
            col += direction[1]
            print(f"{' ' * row}{'*' * col}")

    @staticmethod
    def print_heart(size=5):
        for i in range(size):
            spaces = ' ' * (size - i)
            hearts = '♥' * (2 * i + 1)
            print(f"{spaces}{hearts}")

        for i in range(size - 1, 0, -1):
            spaces = ' ' * (size - i)
            hearts = '♥' * (2 * i - 1)
            print(f"{spaces}{hearts}")

    @staticmethod
    def print_diagonal_lines(rows=10):
        for i in range(rows):
            spaces = ' ' * i
            line = '*' + ' ' * (rows - i - 1) + '*'
            print(f"{spaces}{line}")



    # New utility function for printing a digital clock
    @staticmethod
    def digital_clock():
        """Display a digital clock."""
        while True:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"\r{current_time}", end='', flush=True)
            time.sleep(1)

    

    # New utility function for printing a simple snake game
    @staticmethod
    def snake_game():
        """Play a simple snake game."""
        snake = [(0, 0)]
        fruit = Chalk.generate_fruit(snake)
        direction = (1, 0)

        while True:
            os.system('clear' if os.name == 'posix' else 'cls')  # Clear the terminal screen
            Chalk.draw_game_board(snake, fruit)
            Chalk.move_snake(snake, direction)
            if Chalk.check_collision(snake):
                print("Game Over!")
                break
            if snake[0] == fruit:
                snake.append(snake[-1])  # Grow the snake
                fruit = Chalk.generate_fruit(snake)
            time.sleep(0.1)

    # Helper function for generating a fruit for the snake game
    @staticmethod
    def generate_fruit(snake):
        """Generate a random fruit position for the snake game."""
        while True:
            fruit = (random.randint(0, 9), random.randint(0, 9))
            if fruit not in snake:
                return fruit

    # Helper function for drawing the game board in the snake game
    @staticmethod
    def draw_game_board(snake, fruit):
        """Draw the game board for the snake game."""
        for i in range(10):
            for j in range(10):
                if (i, j) == fruit:
                    print(Chalk.RED + 'F' + Chalk.RESET, end=' ')
                elif (i, j) in snake:
                    print(Chalk.GREEN + 'S' + Chalk.RESET, end=' ')
                else:
                    print('O', end=' ')
            print()

    # Helper function for moving the snake in the snake game
    @staticmethod
    def move_snake(snake, direction):
        """Move the snake in the specified direction."""
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)
        if new_head != snake[-1]:
            snake.pop()

    # Helper function for checking collision in the snake game
    @staticmethod
    def check_collision(snake):
        """Check for collision with walls or itself."""
        head = snake[0]
        if (
            head[0] < 0 or head[0] >= 10 or
            head[1] < 0 or head[1] >= 10 or
            head in snake[1:]
        ):
            return True
        return False

    # New utility function for printing a matrix transposition
    @staticmethod
    def matrix_transposition(matrix):
        """Display the transposition of a matrix."""
        transposed_matrix = list(map(list, zip(*matrix)))
        for row in transposed_matrix:
            row_str = ' '.join(map(str, row))
            print(row_str)

    # New utility function for printing a simple histogram
    @staticmethod
    def print_histogram(data):
        """Display a simple histogram."""
        for value in data:
            bar = '#' * value
            print(bar)

    # New utility function for printing a rotating Earth animation
    @staticmethod
    def rotating_earth_animation():
        """Display a rotating Earth animation."""
        earth_chars = ['🌍', '🌎', '🌏']
        while True:
            for char in earth_chars:
                print(f"\r{char}", end='', flush=True)
                time.sleep(0.5)
