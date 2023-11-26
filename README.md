# Chalk

Chalk is a Python package for terminal text styling and coloring. Add vibrant colors, formatting, and animations to your terminal output with ease.

## Installation

You can install Chalk using pip:

```bash
pip install Chalk
```

## Usage

```python
from Chalk import Chalk

# Example usage
text = "Hello, Chalk!"
styled_text = Chalk.format_text(text, styles=[Chalk.BOLD, Chalk.BLUE])
print(styled_text)
```

## Features

- Stylish text formatting
- Colorful output for better visibility
- Text animations for a dynamic terminal experience


| Function | Description | Example Usage | Arguments |
| --- | --- | --- | --- |
| `format_text` | Formats text with styles and color | `Chalk.format_text("Hello", styles=[Chalk.BOLD, Chalk.RED])` | `text (str)`, `styles (list of str)`, `color (str)` |
| `colorized_banner` | Creates a colorized banner | `Chalk.colorized_banner("Welcome", styles=[Chalk.BOLD], color=Chalk.BLUE)` | `text (str)`, `styles (list of str)`, `color (str)`, `banner_char (str)` |
| `rainbow_text` | Creates rainbow-colored text | `Chalk.rainbow_text("Hello, Rainbow!")` | `text (str)` |
| `create_table` | Creates a table with a header and data | `Chalk.create_table(["Name", "Age"], [["Alice", 25], ["Bob", 30]])` | `header (list of str)`, `data (list of lists)` |
| `typewriter_text` | Outputs text with a typewriter effect | `Chalk.typewriter_text("Hello, Typewriter!")` | `text (str)`, `delay (float)` |
| `pulsating_text` | Outputs text with a pulsating effect | `Chalk.pulsating_text("Pulsating")` | `text (str)`, `period (float)` |
| `blinking_text` | Outputs text with a blinking effect | `Chalk.blinking_text("Blinking")` | `text (str)`, `blink_duration (float)` |
| `rotating_text` | Outputs text with a rotating effect | `Chalk.rotating_text("Rotating", rotations=3)` | `text (str)`, `rotations (int)` |
| `countdown` | Displays a countdown | `Chalk.countdown(5)` | `seconds (int)` |
| `progress_bar` | Displays a progress bar | `Chalk.progress_bar(0.75)` | `progress (float)`, `length (int)` |
| `random_color_text` | Outputs text with random colors | `Chalk.random_color_text("Random Colors")` | `text (str)` |
| `scrolling_text` | Scrolls text horizontally | `Chalk.scrolling_text("Scrolling Text", scroll_speed=0.1)` | `text (str)`, `scroll_speed (float)` |
| `center_text` | Centers text within a specified width | `Chalk.center_text("Centered Text", width=50)` | `text (str)`, `width (int)` |
| `fading_text` | Outputs text with a fading effect | `Chalk.fading_text("Fading Text", fade_duration=5)` | `text (str)`, `fade_duration (float)` |


## Examples

### Rainbow Text

```python
from Chalk import Chalk

text = "Rainbow Text"
rainbow_text = Chalk.rainbow_text(text)
print(rainbow_text)
```

### Table Creation

```python
from Chalk import Chalk

header = ["Name", "Age", "Country"]
data = [
    ["Alice", "25", "USA"],
    ["Bob", "30", "Canada"],
    ["Charlie", "22", "UK"],
]

table = Chalk.create_table(header, data)
print(table)
```

**Repository Views** ![Views](https://profile-counter.glitch.me/Chalk/count.svg)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
