# Mohammad Qureshi
# PSID 1789301
# LAB 10.11



class FoodItem:
    def __init__(self, name = 'None', fat = 0.00, carbs = 0.00, protein = 0.00):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

    def set_name(self, name):
        self.name = name
    def set_fat(self, fat):
        self.fat = fat
    def set_carbs(self, carbs):
        self.carbs = carbs
    def set_protein(self, protein):
        self.protein = protein


if __name__ =="__main__":
    name = str(input())
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    servings = float(input())


    getInfo = FoodItem()

    getInfo.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings,getInfo.get_calories(servings)))
    print()

    getInfo.set_name(name)
    getInfo.set_fat(fat)
    getInfo.set_carbs(carbs)
    getInfo.set_protein(protein)
#servings = float(input())

#print('Number of calories for {:.2f} serving(s): 0.00'.format(servings))
#print()

    getInfo.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings, getInfo.get_calories(servings)))