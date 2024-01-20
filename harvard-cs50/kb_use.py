from kb import *

rain = Symbol("rain")
hagrid= Symbol("hagrid")
dumbledore = Symbol("dumbledore")

print()
print("Check if when harry went to dumbledore,did it surely rain?")
knowledge =	And(
	Implication(Not(rain),hagrid),
	Or(hagrid,dumbledore),
	Not(And(hagrid,dumbledore)),
	dumbledore
)
print(f"Knowledge Base is: {knowledge.formula()}")
print(check_model(knowledge,rain))

print("\n")

print("Check if when harry went to hagrid, did it surely rain?")
knowledge =	And(
	Implication(Not(rain),hagrid),
	Or(hagrid,dumbledore),
	Not(And(hagrid,dumbledore)),
	hagrid
)

print(f"Knowledge Base is: {knowledge.formula()}")
print(check_model(knowledge,rain))