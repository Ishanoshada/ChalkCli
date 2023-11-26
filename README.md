# ChalkCli

ChalkCli is a Python package for terminal text styling and coloring. Add vibrant colors, formatting, and animations to your terminal output with ease.

## Installation

You can install ChalkCli using pip:

```bash
pip install ChalkCli
```

## Usage

```python
from ChalkCli import ChalkCli

# Example usage
text = "Hello, ChalkCli!"
styled_text = ChalkCli.format_text(text, styles=[ChalkCli.BOLD, ChalkCli.BLUE])
print(styled_text)
```

## Features

- Stylish text formatting
- Colorful output for better visibility
- Text animations for a dynamic terminal experience


| Function | Description | Example Usage | Arguments |
| --- | --- | --- | --- |
| `format_text` | Formats text with styles and color | `ChalkCli.format_text("Hello", styles=[ChalkCli.BOLD, ChalkCli.RED])` | `text (str)`, `styles (list of str)`, `color (str)` |
| `colorized_banner` | Creates a colorized banner | `ChalkCli.colorized_banner("Welcome", styles=[ChalkCli.BOLD], color=ChalkCli.BLUE)` | `text (str)`, `styles (list of str)`, `color (str)`, `banner_char (str)` |
| `rainbow_text` | Creates rainbow-colored text | `ChalkCli.rainbow_text("Hello, Rainbow!")` | `text (str)` |
| `create_table` | Creates a table with a header and data | `ChalkCli.create_table(["Name", "Age"], [["Alice", 25], ["Bob", 30]])` | `header (list of str)`, `data (list of lists)` |
| `typewriter_text` | Outputs text with a typewriter effect | `ChalkCli.typewriter_text("Hello, Typewriter!")` | `text (str)`, `delay (float)` |
| `pulsating_text` | Outputs text with a pulsating effect | `ChalkCli.pulsating_text("Pulsating")` | `text (str)`, `period (float)` |
| `blinking_text` | Outputs text with a blinking effect | `ChalkCli.blinking_text("Blinking")` | `text (str)`, `blink_duration (float)` |
| `rotating_text` | Outputs text with a rotating effect | `ChalkCli.rotating_text("Rotating", rotations=3)` | `text (str)`, `rotations (int)` |
| `countdown` | Displays a countdown | `ChalkCli.countdown(5)` | `seconds (int)` |
| `progress_bar` | Displays a progress bar | `ChalkCli.progress_bar(0.75)` | `progress (float)`, `length (int)` |
| `random_color_text` | Outputs text with random colors | `ChalkCli.random_color_text("Random Colors")` | `text (str)` |
| `scrolling_text` | Scrolls text horizontally | `ChalkCli.scrolling_text("Scrolling Text", scroll_speed=0.1)` | `text (str)`, `scroll_speed (float)` |
| `center_text` | Centers text within a specified width | `ChalkCli.center_text("Centered Text", width=50)` | `text (str)`, `width (int)` |
| `fading_text` | Outputs text with a fading effect | `ChalkCli.fading_text("Fading Text", fade_duration=5)` | `text (str)`, `fade_duration (float)` |


## Examples

### Rainbow Text

```python
from ChalkCli import ChalkCli

text = "Rainbow Text"
rainbow_text = ChalkCli.rainbow_text(text)
print(rainbow_text)
```

### Table Creation

```python
from ChalkCli import ChalkCli

header = ["Name", "Age", "Country"]
data = [
    ["Alice", "25", "USA"],
    ["Bob", "30", "Canada"],
    ["Charlie", "22", "UK"],
]

table = ChalkCli.create_table(header, data)
print(table)
```

**Repository Views** ![Views](https://profile-counter.glitch.me/ChalkCli/count.svg)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
