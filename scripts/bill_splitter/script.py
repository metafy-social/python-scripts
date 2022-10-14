# python script to split bills among a group
from os import system

# function to create contribution object from input string


def createContribution(s):
    s = s.split(' ')
    return {'name': s[0], 'contribution': int(s[1])}

# function to split bill among group


def split_bill(pool: "list[dict]") -> dict:
    contribution_list = [x["contribution"] for x in pool]
    total = sum(contribution_list)
    each = total / len(contribution_list)
    more = []
    less = []
    solution = []
    for i in pool:
        if i["contribution"] < each:
            less.append(
                {"name": i["name"], "contribution": each - i["contribution"]})
        else:
            more.append(
                {"name": i["name"], "contribution": i["contribution"] - each})
    for i in more:
        a = i["contribution"]
        m = [{"name": k["name"], "contribution": 0} for k in less]
        for j in range(len(less)):
            b = less[j]["contribution"]
            if a == 0:
                m[j]["contribution"] = 0
            elif a - b == 0:
                a = a - b
                m[j]["contribution"] = b
                less[j]["contribution"] = 0
            elif a - b > 0:
                a = a - b
                less[j]["contribution"] = 0
                m[j]["contribution"] = b
            elif a - b < 0:
                less[j]["contribution"] = b - a
                m[j]["contribution"] = a
                a = 0
        solution.append({"name": i["name"], "payment": m})
    return {"solution": solution, "total": total, "each": each, "pool": pool}

# function to print solution in a format


def print_solution(result: dict) -> None:
    for i in result["pool"]:
        print(f"{i['name']} paid    ${i['contribution']}")
    print("------------------------------------------------------------------")
    print(f"Total pool amount  : ${result['total']}")
    print(f"Per head           : ${result['each']}")
    print("------------------------------------------------------------------")
    for i in result["solution"]:
        for j in i["payment"]:
            if j["contribution"] > 0:
                print(
                    f"{j['name']} should pay ${j['contribution']} to {i['name']}")
        print("------------------------------------------------------------------")


def print_banner():
    banner = '''
███████╗██████╗ ██╗     ██╗████████╗    ██████╗ ██╗██╗     ██╗     ███████╗
██╔════╝██╔══██╗██║     ██║╚══██╔══╝    ██╔══██╗██║██║     ██║     ██╔════╝
███████╗██████╔╝██║     ██║   ██║       ██████╔╝██║██║     ██║     ███████╗
╚════██║██╔═══╝ ██║     ██║   ██║       ██╔══██╗██║██║     ██║     ╚════██║
███████║██║     ███████╗██║   ██║       ██████╔╝██║███████╗███████╗███████║
╚══════╝╚═╝     ╚══════╝╚═╝   ╚═╝       ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝
---------------------------------------------------------------------------
'''
    print(banner)


system('cls')
print_banner()
pool = []
n = int(input('Number of participants : '))
for i in range(n):
    print('Enter name and contribution of participant ', i+1, ' : ')
    pool.append(createContribution(input()))
system('cls')
print_banner()
print_solution(split_bill(pool))
