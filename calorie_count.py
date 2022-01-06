class calorie:
    def __init__(self,age,gender,weight,height,activity_level):
        self.age=age
        self.weight=weight
        self.height=height
        self.gender=gender
        self.activity_level=activity_level
    def user_info(self):

        if self.gender == 'M':
            c1 = 66
            hm = 6.2 * self.height
            wm = 12.7 * self.weight
            am = 6.76 * self.age
        elif self.gender == 'F':
            c1 = 655.1
            hm = 4.35 * self.height
            wm = 4.7 * self.weight
            am = 4.7 * self.age

        #BMR = 665 + (9.6 X 69) + (1.8 x 178) – (4.7 x 27)
        bmr_result = c1 + hm + wm - am
        return(int(bmr_result))

    def calculate_activity(self,bmr_result):
        # activity_level = input('What is your activity level (none, light, moderate, heavy, or extreme): ')
        activity_level=0
            
        if self.activity_level == 'light':
            activity_level = 1.375 * bmr_result
        elif self.activity_level == 'moderate':
            activity_level = 1.55 * bmr_result
        elif self.activity_level == 'heavy':
            activity_level = 1.725 * bmr_result
        elif self.activity_level == 'extreme':
            activity_level = 1.9 * bmr_result
        else:
            activity_level = 1.2 * bmr_result

        return(int(activity_level))

    def gain_or_lose(self):
        goals = input('Do you want to lose, maintain, or gain weight: ')

        if goals == 'lose':
            calories = activity_level - 500
        elif goals == 'maintain':
            calories = activity_level
        elif goals == 'gain':
            gain = int(input('Gain 1 or 2 pounds per week? Enter 1 or 2: '))
            if gain == 1: 
                calories = activity_level + 500
            elif gain == 2:
                calories = activity_level + 1000

        print('in order to ', goals, 'weight, your daily caloric goals should be', int(calories), '!')