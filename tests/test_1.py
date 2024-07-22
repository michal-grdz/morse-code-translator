import requests

ans_base = requests.get('http://127.0.0.1:5000/')
ans_morse = requests.get('http://127.0.0.1:5000/morse/testing_testing')

print(f'Testing base: \n status code: {ans_base.status_code} \n text: {ans_base.text}')
print(f'Testing morse: \n status code: {ans_morse.status_code} \n text: {ans_morse.text}')
