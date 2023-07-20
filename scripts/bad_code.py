import requests


def donothingfunc():
    print("Function")


api_key = "sldkf090-dummykey-kj454k4007"
headers = {
    "Content-type": "application/json",
    "Authorization": f"ApiKey {api_key}",
}

requests.get("https://someurl", auth=None, headers=headers)

time = int(1)
loop = int(0)
while loop == 0:
    print(
        "Extremely inefficient and pointless time loop, purposefully making bad source code"
    )
    if time != 0:
        print("Time")
        if time != 0:
            print("Time")
            if time != 0:
                print("Time")
                if time != 0:
                    print("Time")
                    if time != 0:
                        print("Time")
                        if time != 0:
                            print("Time")
                            if time != 0:
                                print("Time")
                                if time != 0:
                                    print("Time")
                                    break

else:
    print("Featured on 'what a waste of time'")
    noMore = input("Press [ENTER] key to quit")
    break
return 0
