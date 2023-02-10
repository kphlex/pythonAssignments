class User:
    def __init__(self, first_name, last_name, email, age, member, points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = member
        self.gold_card_points = points
        
    # Method prints Users Info on separate lines 
    
    def display_info(self):
        print(f"\n{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}")
        return self
    
    # Method changes Users membership status and adds gold points if not a member. Prints on separate lines.
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            
        elif self.is_rewards_member == False:
            self.is_rewards_member, self.gold_card_points  = True, 200
            print(f"New Membership!!\nGold Points Sign up bonus:{self.gold_card_points}")
        return self
    
    # Method decreases User's points by the amount specified.
    
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough gold points, jedi")
            return amount
        else:
            self.gold_card_points = self.gold_card_points - amount
            
            print(f"Updated Gold Card Points:{self.gold_card_points}")
            return self


userOne = User("Jabba", "DaHut", "jabba@idkwherehesfrom.com", "146", True, 300)

userTwo = User("Hans", "Solo", "hans@falcon.com", "45", False, 0)

userThree = User("Darth", "Vader", "vader@deathstar.com", "60", False, 0)

userOne.display_info().enroll().spend_points(50)

userTwo.display_info().enroll().spend_points(80)

userThree.display_info().spend_points(40)


