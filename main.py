import requests

url = 'https://ocrcodesimpleonlyocr.vercel.app/ocr/'

# Prepare the form data
data = {
    'firstName': 'Deep',
    'lastName': 'Gohil',
    'mobileNumber': '08104680835',
    'email': 'deepgohil777@gmail.com',
    'date': '02-202-03'
}

# Prepare the file
files = {
    'image': ('test1.jpeg', open('test1.jpeg', 'rb'), 'image/jpeg')
}

# Make the POST request
try:
    response = requests.post(url, data=data, files=files)
    
    # Check if request was successful
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code)
        print(response.text)
        
except Exception as e:
    print("An error occurred:", str(e))

# Don't forget to close the file
files['image'][1].close()