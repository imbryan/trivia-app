from model import Question
from view import View
import json, random, glob


class Controller:
    def __init__(self):
        self.view = View(self)
        self.json_file = None
        self.all_questions = list()
        self.selected_questions = list()

    def main(self):
        self.file_selector()
        self.parse_json()
        self.select_questions()

        self.view.question_var.set("1. " + self.selected_questions[0].question)
        answers = self.shuffle_answers(0)
        self.view.A_var.set(answers[0])
        self.view.B_var.set(answers[1])
        self.view.C_var.set(answers[2])
        self.view.D_var.set(answers[3])

        self.view.main()

    def file_selector(self):
        try:
            json_files = glob.glob("*.json")
            self.json_file = open(json_files[0])

        except Exception as e:
            self.view.popup_window("Error", f"Could not find a file:\n{e}")

    def parse_json(self):
        try:
            questions_json = json.loads(self.json_file.read())

            # Iterating through an array of JSON objects and filling out Question objects
            for json_object in questions_json:
                self.all_questions.append(Question(
                    question=json_object['question'],
                    incorrect=json_object['incorrect'],
                    correct=json_object['correct'],
                ))

        except Exception as e: print(e)

    # Select 10 questions, as per specification
    def select_questions(self):
        random.shuffle(self.all_questions)

        for i in range(10):
            self.selected_questions.append(self.all_questions[i])

    # Shuffles the answers positions so that it won't be predictable
    def shuffle_answers(self, index):
        answers = list()
        answers.extend(self.selected_questions[index].incorrect)
        answers.append(self.selected_questions[index].correct)
        random.shuffle(answers)
        return answers

    def on_button_click(self, option):
        correct = False
        correct_option = str()
        current_index = self.view.current_question

        if self.selected_questions[current_index].correct == self.view.A_var.get(): correct_option = "A"
        elif self.selected_questions[current_index].correct == self.view.B_var.get(): correct_option = "B"
        elif self.selected_questions[current_index].correct == self.view.C_var.get(): correct_option = "C"
        elif self.selected_questions[current_index].correct == self.view.D_var.get(): correct_option = "D"

        if correct_option == option: correct = True

        if correct: self.view.score = self.view.score + 1

        self.view.popup_window("Notification", f"{correct}! The answer was {correct_option}: {self.selected_questions[current_index].correct}\n\nCurrent score: {self.view.score}")

        current_index += 1
        self.view.current_question = current_index

        if current_index < 10:
            self.view.question_var.set(f"{current_index + 1}. " + self.selected_questions[current_index].question)
            answers = self.shuffle_answers(current_index)
            self.view.A_var.set(answers[0])
            self.view.B_var.set(answers[1])
            self.view.C_var.set(answers[2])
            self.view.D_var.set(answers[3])
        else:
            self.view.popup_window("Result", f"Final score: {self.view.score}\n\nThank you for playing!")
            self.view.destroy()


if __name__ == '__main__':
    trivia = Controller()
    trivia.main()
