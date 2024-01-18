# Chukwueemka Nwachukwu, W211379501 , Cosc - Intro to Python 2

members = [
   ["John Smith", "john.smith@hotmail.com"],
   ["John Doe", "john.doe@aol.com"],
   ["Bill Jack", "billy.jack@aol.com"],
   ["Chuck Connors", "chuck.conors@hotmail.com"],
   ["Lucy Ball", "lucy.ball@yahoo.com"],
   ["Bing Hope", "bing.hope@aol.com"],
   ["Bob Crosby", "bob.crosby@aol.com"],
   ["Piers Anthony", "piers.anthony@hotmail.com"]
]

registered = [
   ["john.smith@hotmail.com"],
   ["john.doe@aol.com"],
   ["al.deniro@aol.com"],
   ["bob.crosby@aol.com"],
   ["billy.crystal@aol.com"],
   ["robert.pacino@aol.com"] 
]

# Function to print list vertically
def print_vertical(list):
   for item in list:
      print(item)

# Function to get unregistered members
def get_unregistered(members, registered):
   unregistered = []
   for member in members:
      email = member[1]
      if email not in registered:
         unregistered.append(member)
   return unregistered

# Function to get unregistered registrants  
def get_nonmembers(registered, members):
   nonmembers = []
   for email in registered:
      found = False
      for member in members:
         if email[0] == member[1]:
            found = True
            break
      if not found:
         nonmembers.append(email)
   return nonmembers
   
if __name__ == "__main__":
   print("Unregistered Members:")
   unreg_members = get_unregistered(members, registered)
   print_vertical(unreg_members)
   
   print("\nUnregistered Registrants:")
   non_members = get_nonmembers(registered, members)
   print_vertical(non_members)