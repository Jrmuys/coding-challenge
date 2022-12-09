# Joel's Coding Challenge

Welcome to my coding challenge, I hope you have fun (and learn something)

## Getting Started

To get started, you'll have to install some things

1. Install git (https://git-scm.com/downloads)
2. Check if you have python 3 installed using `python --version` (if you don't have it, install it from https://www.python.org/downloads/)
3. Install visual studio code (https://code.visualstudio.com/download)
4. Clone this repository using `git clone https://github.com/Jrmuys/coding-challenge.git` (or download it as a zip file)
5. Open the folder in visual studio code
6. Install the recommended extensions (you can do this by clicking the button in the bottom right corner of the screen)
7. Create a virtual environment
   1. Press `ctrl+shift+p` and type `python: create environment`
   2. Select the option that says `Venv`
   3. Select latest python 3 version
8. When the virtual environment is created, there should be a popup in the bottom right corner of the screen asking if you want to select it for the workspace folder, click the button that says `Yes`. If this does not show up, you can press `ctrl+shift+p` and type `python: select interpreter` and select the virtual environment you just created.
9. Install the required packages using `pip install -r requirements.txt`
10.   You're all set up! You can now start coding

## How to run the code

To run the code, you can press `ctrl+shift+p` and type `python: run file in terminal` and select the file you want to run. You can also press `ctrl+shift+p` and type `python: run current file in terminal` to run the file you have open in the editor.

If you want to run the code in the terminal, you can use `python <filename>` to run the file.

If you select a section of code, you can run it by pressing `ctrl+enter` (or `cmd+enter` on mac). You can also run the whole file by pressing `f5`. If you want to make a keyboard shortcut for running the file in terminal, you can press `ctrl+shift+p` and type `keyboard shortcuts` and search for `python: run file in terminal` and set a keyboard shortcut for it.

## How to run the tests

To run the tests, you can run the `main_test.py` file. You can also configure the tests to run them in the sidebar by clicking on the beaker icon in the sidebar and

If you want to run the tests in the terminal, you can use `python -m unittest <filename>` to run the file.

## How to debug the code

To debug the code, you can press `f5` to start debugging. You can also set a keyboard shortcut for debugging by pressing `ctrl+shift+p` and type `keyboard shortcuts` and search for `python: debug current file` and set a keyboard shortcut for it.

## How to format the code

To format the code, you can press `ctrl+shift+p` and type `python: format document` and select the file you want to format. You can also press `ctrl+shift+p` and type `python: format current file` to format the file you have open in the editor.

I would recommend setting format on save to true, you can do this by pressing `ctrl+shift+p` and type `settings` and search for `format on save` and set it to true.

# Challenge 1 - Is the number prime?

The goal is to write a function that takes a number and returns true if it is prime and false if it isn't.

Before you start, pull the latest changes from the repository using `git pull`. You should also create a new branch using `git checkout -b challenge1`.

To get started, navigate to the `challenge1` folder and open the `main.py` file. Write your code in the `is_prime` function.

You can run the code by pressing `ctrl+shift+p` and type `python: run file in terminal` and select the file you want to run. You can also press `ctrl+shift+p` and type `python: run current file in terminal` to run the file you have open in the editor.

When you run the file in the terminal, it will ask you for a number, enter a number and press enter. It will then print out the result of your function.

To test your code, you can run the tests by running the `main_test.py` file. You can also configure the tests to run them in the sidebar by clicking on the beaker icon in the sidebar and clicking on the gear icon and selecting `Configure Tests`.

Once you're done, you can commit your changes using the vscode git ui, or with `git add .` and `git commit -m "challenge1"` and push your changes using `git push origin challenge1`. You can then create a spull request on github.
