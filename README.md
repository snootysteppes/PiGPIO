# GPIO and Pygame Interaction

This Python script demonstrates how to use the `pygame` and `RPi.GPIO` libraries to interact with the GPIO pins on a Raspberry Pi.

## Dependencies

- `pygame`: A Python library for making multimedia applications like games.
- `RPi.GPIO`: A Python library that allows you to easily use the GPIO pins on a Raspberry Pi.

You can install these dependencies using pip:

```bash
pip3 install pygame RPi.GPIO
```

## How It Works

The script sets up a GPIO pin as an input pin, and then enters a loop where it continually checks the state of the pin. If the button connected to the pin is pressed, it calls a function that prints "Hello, world!" to the console.

## Usage

You can run the script using Python 3:

```bash
python3 script.py
```

Please note that you might need to modify the pin number in the script depending on how you've wired your button.

## References

- [RPi.GPIO PyPi Module](https://pypi.org/project/RPi.GPIO/)
- [RPi.GPIO Documentation](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)

## Compatibility

This script has been tested and is confirmed to be working with Python versions up to 3.10.
```

Please replace `script.py` with the actual name of your Python script.

: https://www.pygame.org/
: https://pypi.org/project/RPi.GPIO/
```
