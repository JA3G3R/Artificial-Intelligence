from kb import *

mustard = Symbol("mustard")
plum = Symbol("plum")
scarlet = Symbol("scarlet")

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")

knife = Symbol('knife')
revolver = Symbol("revolver")
wrench = Symbol("wrench")

knowledge = And(

	Or(mustard,plum,scarlet),
	Or(ballroom,kitchen,library),
	Or(knife,revolver,wrench)

)

people = [mustard, plum, scarlet]
rooms = [ballroom,kitchen,library]
weapons = [knife,revolver,wrench]
symbols = people+rooms+weapons

def analyse_clues(knowledge):
	for sym in symbols:
		if check_model(knowledge,sym):
			print(f"{sym}: YES")
		elif not check_model(knowledge,Not(sym)):
			print(f"{sym}: MAYBE")

knowledge.add(Not(mustard))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))

knowledge.add(Or(
	Not(scarlet), Not(library), Not(wrench)
))

knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

# knowledge.add()
analyse_clues(knowledge)
# print(check_model(knowledge,Not(ballroom)))
