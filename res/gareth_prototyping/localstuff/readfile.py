import sys

file_name = sys.argv[1]

with open(file_name, "r") as f:
    for line in f:
        query, resp = line.split(":")
        bot_resp = getresp(query)
        if bot_resp == resp:
            print("Success")
        else:
            print("Fail")