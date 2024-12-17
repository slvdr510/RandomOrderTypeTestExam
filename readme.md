# Overview
A simple Python script that:  
- Loops through data from a JSON file.
- Never repeats the order of questions and answers options.
- Lets you select an answer for each question.  
- Allows you to adjust `time.sleep()` after right and wrong answers.  
- Displays a summary at the end:  
  - Total correct and incorrect answers.  
  - A list of incorrectly answered questions with their correct answer.  

---

# Usage

1. Clone the repository:
```bash
git clone https://github.com/slvdr510/randomOrderTypeTestExam
```

2. Navigate to the folder:
```bash
cd randomOrderTypeTestExam
```

3. Run the script:
```bash
python random_order_type_test_exam.py
```
*(Use VSCode's terminal for emoji support)*

---

# Reusability

Create a JSON file with the following structure to run your own tests/quizzes.

```json
    [
        {
            "question": "Commodo sunt excepteur irure sint veniam",
            "option": [
                "Pariatur velit elit qui labore officia labore qui voluptate sint.",
                "Incididunt velit excepteur pariatur id excepteur.",
                "Proident eiusmod amet eiusmod incididunt reprehenderit sint anim laborum.",
                "Pariatur id velit mollit est dolore sint aute irure voluptate Lorem esse."
            ],
            "correctOption": 1
        },
        {
            "question": "Question",
            "option": [
                "Answer number 1",
                "Answer number 2",
                "Answer number 3",
                "Answer number 4"
            ],
            "correctOption": 1
        }
    ]
```

---

## License

[MIT](https://github.com/slvdr510/RandomOrderTypeTestExam/blob/main/LICENSE)