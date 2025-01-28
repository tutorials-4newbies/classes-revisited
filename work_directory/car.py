"""
Exercise 2: Car Class with Inheritance

    Create a class called Vehicle with an __init__ method that takes make, model, and year as parameters.
    Add a method called start_engine() to the Vehicle class that prints "Engine started!".
    Create a class called Car that inherits from the Vehicle class.
    The Car class should have an __init__ method that takes make, model, year, and num_doors as parameters.
    Add a method called honk_horn() to the Car class that prints "Beep beep!".
    Create an instance of the Car class and call the start_engine() and honk_horn() methods.
"""
"""
Bonus Exercise!
Implement the methods start_engine and honk_horn so that honk_horn works only if the engine was first started!
For Example:
    car = Car(...)
    car.honk_horn()
Should print >> "Can't honk horn before engine started"

But:
    car = Car(...)
    car.start_engine()
    car.honk_horn()
Should work
"""