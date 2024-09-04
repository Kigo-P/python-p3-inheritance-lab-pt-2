class Student:
    # a method called hello()
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
    
    # a method called raise_hand()
    def raise_hand(self):
        print("Pick me!")

    pass

class ChattyStudent(Student):
    # a method called hello() that inherits from the superclass
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
    
    # a method called raise_hand() that inherits from the superclass
    def raise_hand(self):
        for element in range(1, 11, 1):
            element = super().raise_hand()
        return element
    
    pass



peter = ChattyStudent()
peter.hello()
peter.raise_hand()