from collections import deque
def person_is_ending_with_t(name):
    return name[-1]=='t'
def search(name, false=None):
    search_queue=deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if person_is_ending_with_t(person):
                print("We found that",person,"is the one ending with t")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return false

graph={}
graph["you"]=["Simon","Maria","Ludovica"]
graph["Simon"]=["Luca","Isa","Jack"]
graph["Maria"]=[]
graph["Luca"]=[]
graph["Isa"]=[]
graph["Jack"]=[]
graph["Ludovica"]=["Matt","Matthew"]
search("you")