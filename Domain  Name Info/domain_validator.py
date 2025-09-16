import whois
def is_registered(domain_name):
    try:
        w=whois.whois(domain_name)
    except:
        return False
    else:
        return bool(w.domain_name)

if __name__ == "__main__":
    l=["google.com","something-that-do-nt-exist.com"]
    for i in l:
        print(i," ",is_registered(i))




# import whois

# def is_registered(domain_name):
#     try:
#         w=whois.whois(domain_name)
#     except Exception :
#         return "Not registered"
#     else:
#         return "Registered"

# if __name__=='__main__':
#     print(is_registered('www.youtube.com'))
#     print(is_registered('www.something-that-do-nt-exist.com'))