class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            res = True
            ip = queryIP.split(".")

            if len(ip) != 4:
                return "Neither"

            for ip_t in ip:
                if len(ip_t) < 1 or len(ip_t) > 3:
                    res = False
                    break
                for i in range(len(ip_t)):
                    if not ip_t[i].isdigit():
                        print(ip_t[i])
                        res = False
                        break
                if not res:
                    break
                if int(ip_t) < 0 or int(ip_t) > 255:
                    res = False
                    break
                if int(ip_t) > 0 and ip_t[0] == "0":
                    res = False
                    break
                if int(ip_t) == 0 and len(ip_t) > 1 and ip_t[0] == "0":
                    res = False
                    break
                if not res:
                    break
            
            if not res:
                return "Neither"
            else:
                return "IPv4"
        
        elif ":" in queryIP:
            res = True
            ip = queryIP.split(":")

            if len(ip) != 8:
                return "Neither"

            for ip_t in ip:
                if len(ip_t) > 4 or len(ip_t) < 1:
                    #print(ip_t)
                    res = False
                    break
                for i in range(len(ip_t)):
                    if not ip_t[i].isdigit() and not ip_t[i].lower() in ['a','b','c','d','e','f']:
                        res = False
                        print(ip_t)
                        break
                if not res:
                    break
            
            if not res:
                return "Neither"
            else:
                return "IPv6"
        else:
            return "Neither"



        




        