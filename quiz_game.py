questions = [
    {
        "prompt"  : "What is the captial of India?",
        "options" : ["A. Mumbai ", "B. Chennai ", "C. Bengaluru ", "D. New Delhi "],
        "answer"  : "D"
    },
    
    {
        "prompt"  : "Which language is primarily speaks in India",
        "options" : ["A. Tamil ", "B. Telugu ", "C. Hindi", "D. Bengali "],
        "answer"  : "C"
    },

    {
        "prompt"  : "What is the smallest prime number?",
        "options" : ["A. 2 ", "B. 1 ", "C. 3 ", "D. 5 "],
        "answer"  : "A"
    },

    {
        "prompt"  : "Who wrote bhagavad gita",
        "options" : ["A. Kambar ", "B. Maharishi Veda Vyasa ", "C. Valmigi ", "D. Valikunjam"],
        "answer"  : "B"
    }

]


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter the answer  (A, B, C, D): ").upper()
        if answer == question["answer"]:
            print("Correct answer!!! Hooooray!!!!!!", "\n")   
            score += 1 
        else:    
            print("Wrong answer!!!! , The correct answer is :", question["answer"], "\n")

    print(f"You got {score} out of {len(questions)} questions correct.")


run_quiz(questions)        