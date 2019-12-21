#The code is broken, if kept with the original indent

# Sample of broken code
# class Spell:
#     def __init__(self, incantation, name):
#         self.name = name
#         self.incantation = incantation
#     def __str__(self):
#         return self.name + '  ' + self.incantation + '\n' + self.get_description()
#     def get_description(self):
#         return 'No description'
#     def execute(self):
#         print(self.incantation)

# class Accio(Spell):
#     def __init__(self):
#         Spell.__init__(self, '’Accio’', '’Summoning Charm’')

#         class Confundo(Spell):
#     def __init__(self):
#         Spell.__init__(self, '’Confundo’', '’Confundus Charm’')
#     def get_description(self):
#         return '’Causes the victim to become confused and befuddled.’'
#     def study_spell(spell):
#         print(spell)
    
# spell = Accio()
# spell.execute()
# study_spell(spell)
# study_spell(Confundo())

# reasons for why the code is broken : 
# - the confundo class has too much indentation
# - study_spell cannot be called without creating a Confundo Object, therefore it will yield an error on line 29


# code that works :
# differences :
# -Fixed indentation on confundo class
# -study_spell is now not a function inside a class, but a global function

class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + '  ' + self.incantation + '\n' + self.get_description()
    def get_description(self):
        return 'No description'
    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, '’Accio’', '’Summoning Charm’')
    # def __str__(self):
        # return "This charm summons an object to the caster, potentially over a significant distance"

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, '’Confundo’', '’Confundus Charm’')
    def get_description(self):
        return '’Causes the victim to become confused and befuddled.’'

def study_spell(spell):
    print(spell)
    
spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
# print(Accio())

# A.
    # 1. Parent class : Spell
    # 2. Child class : Accio, Confundo
# 
# B.
    # The fixed code prints out :
        # Accio
        # Summoning Charm  Accio
        # No Description
        # Confundus Charm  Confundo
        # Causes the victim to become confused and befuddled
# 
# C.
    # The get description on the confudo class. Because, when the child class have the same function identifier with its parent class,
    # it will overwrite the parent function. Meaning, the code on the child class will be executed instead of the parents class.
# 
# D.
    # Make a __str__(self) function which returns "This charm summons an object to the caster, potentially over a significant distance"
# 
    # changed class:
    # class Accio(Spell):
        # def __init__(self):
            # Spell.__init__(self,'Accio','Summoning Charm')
        # 
        # added function
        # def __str__(self):
            # return "This charm summons an object to the caster, potentially over a significant distance"
# 