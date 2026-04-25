def ipclass_check(ip_prompt):
    ip_strip = ip_prompt.split(".")
    first_oct = int(ip_strip[0])

    if 1 <= first_oct <= 126:
        return "ClassA"
    elif 128 <= first_oct <= 191:
        return "ClassB"
    elif 192 <= first_oct <= 223:
        return "ClassC"
    elif 224 <= first_oct <= 239:
        return "ClassD"
    elif 240 <= first_oct <= 255:
        return "ClassE"
    else:
        return "Invalid"


def ip_to_binary(ip_prompt):
    check = ipclass_check(ip_prompt)

    if check == "A":
        return "11111111.00000000.00000000.00000000"
    elif check == "B":
        return "11111111.11111111.00000000.00000000"
    elif check == "C":
        print ("11111111.11111111.11111111.00000000")
    elif check == "D":
        return "Multicast (No default subnet mask)"
    elif check == "E":
        return "Experimental (No default subnet mask)"
    else:
        return "Invalid IP address"
ip_to_binary("192.168.11.66")
