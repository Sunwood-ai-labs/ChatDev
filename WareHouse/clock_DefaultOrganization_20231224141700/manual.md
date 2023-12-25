# Simple Clock User Manual

## Introduction

The Simple Clock is a Python-based application that displays the current time on a graphical user interface. It is a simple and easy-to-use clock that can be run on a website.

## Installation

To use the Simple Clock, you need to have the following dependencies installed:

- Python (version 3.6 or higher)
- tkinter library

You can install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

To use the Simple Clock, follow these steps:

1. Open the terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the following command to start the clock:

```
python main.py
```

4. A tkinter window will open, displaying the current time in a large font size.
5. The time will be automatically updated every second.

## Customization

You can customize the Simple Clock according to your preferences. Here are a few suggestions:

- Font: You can change the font of the time label by modifying the `font` parameter in the `time_label` definition in the `main.py` file.
- Window title: You can change the title of the tkinter window by modifying the `title` parameter in the `window` definition in the `main.py` file.
- Time format: You can change the format of the displayed time by modifying the `strftime` parameter in the `get_current_time` method in the `clock.py` file.

## Conclusion

The Simple Clock is a straightforward and user-friendly application that displays the current time. It can be easily customized to suit your preferences. Enjoy using the Simple Clock!