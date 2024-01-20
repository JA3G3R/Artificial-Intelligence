# This file is an attempt to replicating the code displayed by Brian Yu @https://www.youtube.com/watch?v=5NgNicANyqM&t=8352s with as little assistance as possible
# TODO
# 1. It's really messy and completely the opposite of OOPS principles lol. FIX IT!
# 2. Make a lexical parser to make sort of PL/SQL type interpreter

class Statement():

	stmts = []
	def __init__():
		pass

	def evaluate(self):
		raise Exception("Nothing to evaluate")

	def formula(self):
		return ""

	def symbols(self):
		return {}

	def add(self,*stmts):
		self.stmts += stmts

class Symbol(Statement):

	def __init__(self,string):
		self.repr = string		

	def __str__(self):
		return self.repr

	def formula(self):
		return self.repr

	def evaluate(self,model):
		try:
			
			return model[self.repr]
		except KeyError:
			raise Exception("Model is incomplete!")

	def symbols(self):
		return {self.repr}


class Not(Statement):

	def __init__(self,st):
		self.st = st
		
	def evaluate(self,model):
		return not self.st.evaluate(model)

	def formula(self):
		return f"¬({self.st.formula()})"

	def symbols(self):
		return self.st.symbols()

class And(Statement):

	def __init__(self,*stmts):
		# store the two statements s1 ^ s2
		if len(stmts) <=1:
			raise Exception("Illegal declaration of And()")
		self.stmts=stmts

	def evaluate(self,model):
		truth=True
		for st in self.stmts:
			truth = truth and st.evaluate(model)
		return truth

	def formula(self):
		return f"({' ^ '.join([st.formula() for st in self.stmts])})"

	def symbols(self):
		symbols = set()
		for st in self.stmts:
			
			symbols.update(st.symbols())
		return symbols

	# def add(self,*stmts):
	# 	self.stmts+=stmts


class Or(Statement):

	def __init__(self,*stmts):
		# store the two statements s1 ^ s2
		if len(stmts) <=1:
			raise Exception("Illegal declaration of And()")
		self.stmts=stmts

	def evaluate(self,model):
		truth = False
		for st in self.stmts:
			truth = truth or st.evaluate(model)
		return truth

	def formula(self):
		return f"({' V '.join([st.formula() for st in self.stmts])})"

	def symbols(self):
		symbols = set()
		for st in self.stmts:
			symbols.update(st.symbols())
		return symbols


class Implication(Statement):

	def __init__(self,s1,s2):
		self.st1 = s1
		self.st2 = s2

	def evaluate(self,model):
		return not (self.st1.evaluate(model)) or (self.st1.evaluate(model) and self.st2.evaluate(model))

	def formula(self):
		return f"({self.st1.formula()} => {self.st2.formula()})"

	def symbols(self):
		return set.union(self.st1.symbols(),self.st2.symbols())


def check_model(knowledge, query):

	def check_all(knowledge,query,remaining,model):
		symbols=remaining.copy()
		
		if not symbols:
			if knowledge.evaluate(model):
				truth = query.evaluate(model)
				return truth
			return True
		else:
			sym = symbols.pop()
			model_true = model.copy()
			model_true[sym] = True 

			model_false = model.copy()
			model_false[sym] = False

		return check_all(knowledge,query,symbols,model_true) and check_all(knowledge,query,symbols,model_false)
		# In the above return statement we added an and because, we need to make sure that there is no case where the knowledge base is true but the query condition is false. Since that would mean that it is not necessarily true that the knowledge base results in the query being true.

	# join together all the symbols from knowledge and query
	symbols = set.union(knowledge.symbols(),query.symbols())

	return check_all(knowledge,query,symbols,{})