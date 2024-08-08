import requests


def trivia_questions():
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    if response.status_code == 200:
        data = response.json()
        fetched_questions = [{'text': item['question'], 'answer': item['correct_answer']} for item in data['results']]
        print(fetched_questions)
        return fetched_questions
    else:
        print("Failed to retrieve data", response.status_code)
