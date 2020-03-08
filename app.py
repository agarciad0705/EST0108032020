from flask import Flask, jsonify, request, make_response
import phonenumbers
from phonenumbers import geocoder
import csv
import codecs
import random
app = Flask(__name__)

# Task 1
#curl --request POST \
#  --url http://127.0.0.1:4000/phones/csv \
#  --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
#  --form numbers=
@app.route('/phones/csv', methods=['POST'])
def loadPhones():        
    file = request.files['numbers']
    read = csv.reader(codecs.iterdecode(file, 'utf-8'))
    my_list = []
    for row in read:
        for match in phonenumbers.PhoneNumberMatcher(row[0], "US"):
            numberFormated = (phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))    
            z = phonenumbers.parse(numberFormated, None)
            validNumber = phonenumbers.is_valid_number(z)
            ch_number = phonenumbers.parse(numberFormated, "CH")
            geo = geocoder.description_for_number(ch_number, "es")
            #numbers, valid, location
            my_list.append(str(row[0]+", "+str(validNumber)+", "+ifnull(geo,"n/a")))
    return jsonify(results = my_list)

# Task 2
#curl --request GET \
#  --url 'http://127.0.0.1:4000/phones/(213)%20416-0509'
@app.route('/phones/<string:number>', methods = ['GET'])
def addProductPost(number):
    my_list = []
    my_list.append("inputNumber:"+getPhoneData(number))    
    secondNumber = ("("+number[1:4]+") "+str(random.randint(0, 999))+"-"+str(random.randint(0, 9999)))
    my_list.append("generatedNumber:"+getPhoneData(secondNumber))    
    return jsonify(results = my_list)

def getPhoneData(phoneNumber):   
    number = str(phoneNumber)
    for match in phonenumbers.PhoneNumberMatcher(phoneNumber, "US"):
        numberFormated = (phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164))    
        z = phonenumbers.parse(numberFormated, None)
        validNumber = phonenumbers.is_valid_number(z)
        ch_number = phonenumbers.parse(numberFormated, "CH")
        geo = geocoder.description_for_number(ch_number, "es")        
        return ("number: "+number+" valid: "+str(validNumber)+" location: "+ifnull(geo,"n/a"))

        
def ifnull(var, val):
    if var is "":
        return val
    return var

if __name__ == '__main__':
    app.run(debug=True, port=4000)