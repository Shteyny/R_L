class hero_fight:
    def __init__(self, screen):
        self.screen = screen

    def preparation(self, experience, abilities, picture):
        for i in range(len(abilities)):  # abilities = [[att, name, cd, type], [...], ...]
            abilities[i][0] += int(experience * 0.02)
        self.experience = experience
        self.abilities = abilities
        self.picture = picture
        self.health = int(20 + experience * 0.1)

    def update(self, dop_exp):
        for i in range(len(self.abilities)):
            self.abilities[i][0] += int((self.experience + dop_exp) * 0.02)
        self.experience += dop_exp
        self.health = int(20 + self.experience * 0.1)

    def give_ability(self):
        return self.abilities

    def give_health(self):
        return self.health

    def give_experience(self):
        return self.experience

    def otris(self):
        self.screen.blit(self.picture, (200, 200))