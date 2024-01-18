# Chukwueemka Nwachukwu
# W211379501
# Cosc - Intro to Python 2
# Umbrella leaks

mems = [
    ["John Smith", "john.smith@hotmail.com"],
    ["John Doe", "john.doe@aol.com"],
    ["Bill Jack", "billy.jack@aol.com"],
    ["Chuck Connors", "chuck.conors@hotmail.com"],
    ["Lucy Ball", "lucy.ball@yahoo.com"],
    ["Bing Hope", "bing.hope@aol.com"],
    ["Bob Crosby", "bob.crosby@aol.com"],
    ["Piers Anthony", "piers.anthony@hotmail.com"]
]

regs = [
    ["john.smith@hotmail.com"],
    ["john.doe@aol.com"],
    ["al.deniro@aol.com"],
    ["bob.crosby@aol.com"],
    ["billy.crystal@aol.com"],
    ["robert.pacino@aol.com"]
]


def print_v(list):
    # Function to print list vertically, one item per line
    for item in list:
        print(item)


def get_unreg(mems, regs):
    # Function to get unregistered members, aka the slackers who haven't signed up yet
    unreg = []
    for mem in mems:
        email = mem[1]
        if email not in regs:
            unreg.append(mem)
    return unreg


def get_nonmem(regs, mems):
    # Function to get unregistered registrants, aka the peeps who wanna join the party but aren't members yet
    nonmem = []
    for email in regs:
        found = False
        for mem in mems:
            if email[0] == mem[1]:
                found = True
                break
        if not found:
            nonmem.append(email)
    return nonmem


if __name__ == "__main__":
    # Main program block, where the magic happens
    print("Unregistered Members:")
    unreg_mems = get_unreg(mems, regs)
    print_v(unreg_mems)

    print("\nUnregistered Registrants:")
    non_mems = get_nonmem(regs, mems)
    print_v(non_mems)
