import requests

questions = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
questions.raise_for_status()
questions = questions.json()
# print(questions["results"])

question_data = [question for question in questions["results"]]
print(question_data)

