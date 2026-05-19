info={
    "name":"bahubali",
    "profession":"politics and army",
    "position":"vice president",
    "wife":"devsena",
    "dynasty":"mahishmati",
    "type":"movie",
    "movie":{
        "director":"ss rajamouli",
        "scriptwriter":"rajamouli",
        "language":"telugu",
        "genre":"fiction",
        "type":"blockbuster"


    }
}

print(info.get("wife"))
print(info["wife"])
# print(info)
# print(info["movie"]["genre"])
# print(info["movie"].keys())
# print(info.values())
# print(info["movie"].values())
# print(info.items())  #key value pair ko tupple ke form mai deta hea
# pairs=list(info.items())   #type cast
# print(pairs[1])

