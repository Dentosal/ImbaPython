import imba
imba.install(["json", "requests"])

my_ip = "http://httpbin.org/ip".fetch().json["origin"]
print(my_ip)
