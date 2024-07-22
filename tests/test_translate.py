import requests

ans_1 = requests.get('http://127.0.0.1:5000/to_morse/This is a test')
ans_2 = requests.get('http://127.0.0.1:5000/from_morse/- .... .. ... , .. ... , .- , - . ... -')

print("Text to translate into morse: This is a test")
print(f"Translation: {ans_1.text}")
print(f"Code: {ans_1.status_code}")
print("Morse to translate into latin: - .... .. ... , .. ... , .- , - . ... -")
print(f"Translation: {ans_2.text}")
print(f"Code: {ans_2.status_code}")
