
"""
group - 5 person

tall-skinny-white -guy

short-skinny-asian -guy

fat-ponytail -guy

crazy facial hair -some guy

east indian guy

***************************************

height : tall - short

size : skinny - fat

ethnicity : asian - east indian - white

specs : ponytail - crazy facial hair

***************************************

made for fun :]

"""

import random

class Programmer():
    def __init__(self,height=["tall","short"],size=["skinny","fat"],eth=["asian","east indian","white"],specs=["ponytail","crazy facial hair"]):
        self.height = height
        self.size = size 
        self.eth = eth
        self.specs = specs

    def GenerateProgrammer(self):
        
        for i in range(1,6):
            hrand = random.randrange(len(self.height))
            srand = random.randrange(len(self.size))
            erand = random.randrange(len(self.eth))
            sprand = random.randrange(len(self.specs))

            x = self.height[hrand]
            y   = self.size[srand]
            z    = self.eth[erand]
            t  = self.specs[sprand]

            print(f"Programmer {i} = Height : {x} , Size : {y} , Eth : {z} , Specs : {t}")


programmer = Programmer()

programmer.GenerateProgrammer()