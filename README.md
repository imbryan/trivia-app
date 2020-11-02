# Trivia Training app
This is a trivia training app, designed per code challenge.

## Requirements
 * Desktop environment (uses GUI)
 * Python 3.7
 
## Running the program
 * Navigate to download location. In the same directory as project files, insert a JSON file containing your trivia data. Such data must exist as an array of at **least** 10 JSON objects, such that **each** object contains the following key-value pairs: 
   * "question": (1 string - this is the question text)
   * "incorrect": (array of 3 strings - these are the incorrect options)
   * "correct": (1 string - this is the correct answer to the question)
 * Open CMD or terminal and navigate to the project directory. Run **python controller.py**.

## Features
 * Selects 10 questions randomly from your array of JSON objects (program assumes at least 10 given)
 * 4-option multiple choice; answers are shuffled to decrease predictability

## Known issues
