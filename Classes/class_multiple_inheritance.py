''' There are times we may use multiple inheritance. Let's have an example:
Let's say, we have two base classes Flyer and Swimmer. Then we will create a new class FlyingFish
that have both base class inherited. 

Here in the code line-16 it inherited both base classes. Then we call the function we get the outcomes. '''


# class Flyer:
#     def flying(self):
#         print("Can fly")

# class Swimmer:
#     def swimming(self):
#         print("Can swim")

# class FlyingFish(Flyer, Swimmer):
#     def fly_fish(self):
#         print("Can fly and swim")


# flying_fishes = FlyingFish()
# flying_fishes.flying()            # Output: Can fly
# flying_fishes.swimming()          # Output: Can swim
# flying_fishes.fly_fish()          # Output: Can fly and swim


''' Now time to make it better shape. Let's create constractor and initialize.
1. Constractor for Flyer: initialize attribute flying_rang, and supply as parameter.
2. Constractor for Swimmer: initialize attribute swimming_rang, and supply as parameter.
3. Constractor for FlyingFish: initialize attribute flying_rang first and since base class __init__
   method overides the subclass constractor so I need call the supper() function and the base class
   __init__ method at this stage if we run the program we get desire Output. But at the same time 
   it gives AttributeError: 'FlyingFish' object has no attribute 'swimming_range'. See line-58 
4. To fix this, we explicitly call(line-59, 60) the constructors of both Flyer and Swimmer within the FlyingFish 
   class's constructor. This ensures that both attributes, flying_range and swimming_range, are properly 
   initialized. Also pass them as parameters. Now, the code should work without any errors. 
5. Finally, return all the function instead print. and print when call the functions. and pass the functions of 
   the base classes since the both functions are combined and achive the same result in subclass(FlyingFish). '''

class Flyer:
    def __init__(self, flying_range):
        self.flying_range = flying_range

    def flying(self):
        pass
        # return f"The flying fish can fly {self.flying_range}"

class Swimmer:
    def __init__(self, swimming_range):
        self.swimming_range = swimming_range

    def swimming(self):
        pass
        # return f"The flying fish can {self.swimming_range}"

class FlyingFish(Flyer, Swimmer):
    def __init__(self, flying_range, swimming_range):
        # super().__init__(flying_range)
        Flyer.__init__(self, flying_range)
        Swimmer.__init__(self, swimming_range)

    def fly_fish(self):
        return f"The flying fish can fly {self.flying_range} also can swim {self.swimming_range}"


flying_fishes = FlyingFish("10m", "100m")
fly = flying_fishes.flying()
swim = flying_fishes.swimming()
fly_and_swim = flying_fishes.fly_fish()
print(fly_and_swim)
# Output: The flying fish can fly 10m also can swim 100m
