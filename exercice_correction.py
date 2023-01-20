class Tank:
    def __init__(self, penetration, armor, armor_type, name=None):
        self.penetration = penetration
        self.armor = armor
        if armor_type not in ['chobham', 'composite', 'ceramic']:
            raise Exception(f'Invalid armor type : {armor_type}')
        self.armor_type = armor_type
        self.name = name

    def __str__(self):
        return self.name.lower().replace(' ', '-')

    def vulnerable_against(self, enemy_tank):
        """
        Check if the tank can resist to an enemy shoot
        """
        if self.armor <= enemy_tank.penetration:
            print(f"The tank <{self}> with stats (armor: {self.armor}, armor_type: {self.armor_type}) is "
                  f"vulnerable against the tank <{enemy_tank}> with stats (penetration: {enemy_tank.penetration})")
            return True
        print(f"The tank <{self}> with stats (armor: {self.armor}, armor_type: {self.armor_type}) isn't vulnerable "
              f"against the tank <{enemy_tank}> with stats (penetration: {enemy_tank.penetration})")
        return False

    def swap_armor(self, othertank):
        """
        Exchange the armor of 2 tanks
        """
        self.armor, othertank.armor = othertank.armor, self.armor


# Check if a tank is vulnerable against the same model
print("Check if a tank is vulnerable against the same model")
shooter = Tank(600, 670, 'chobham', 'Shooter')
shooter.vulnerable_against(shooter)

# Trying of successively more protected tanks against the Shooter
print("\nTrying of successively more protected tanks against the Shooter")
at_least_one_safe = False

for i in range(5):
    new_tank = Tank(400,
                    400 + i*70,
                    'ceramic',
                    'Tank' + str(i) + "_Small")
    if not new_tank.vulnerable_against(shooter):
        at_least_one_safe = True

if at_least_one_safe:
    print("At least 1 tank is safe !")
else:
    print("No tank is safe")
