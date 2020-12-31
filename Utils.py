class utils:
    def __init__(self, screen_width = 1920, screen_height = 1080):
        width_Ratio = screen_width / 1920
        height_ratio = screen_height / 1080

        self.POSITIONS = []
        self.EMOTE_POSITION = [[816,686], [769,769],[771,861],[1103,686],[1157,766],[1144,865]]
        self.HERO_POSITION = [960, 770]
        self.ENEMY_HERO_POSITION = [970, 200]
        self.HERO_POWER_POSITION = [1130, 830]
        self.START_GAME_POSITION = [1380, 850]
        self.END_TURN_POSITION = [1600, 500]
        self.MINION_FROM_POSITION = [811, 1050]
        self.MINION_TO_POSITION = [970, 200]
        self.MINION_INITIAL_POSITION = [930, 580]
        self.ENEMY_MINION_POSITION = [937, 405]
        self.RECONNECT_BUTTON_POSITION = [800, 830]
        self.CONFIRM_CARD_POSITION = [950, 850]

        # color code
        self.TAUNT_COLOR = [236, 227, 217]
        self.CONFIRM_BUTTON_COLOR = [126, 195, 255]
        self.MY_TURN_COLOR = [206, 163, 2]
        self.ENEMY_TURN_COLOR = [82, 73, 62]
        self.END_TURN_COLOR = [33, 158, 3]




        self.HERO_POSITION = [self.HERO_POSITION[0] * width_Ratio, self.HERO_POSITION[1] * height_ratio]
        self.ENEMY_HERO_POSITION = [self.ENEMY_HERO_POSITION[0] * width_Ratio,
                                    self.ENEMY_HERO_POSITION[1] * height_ratio]
        self.HERO_POWER_POSITION = [self.HERO_POWER_POSITION[0] * width_Ratio,
                                    self.HERO_POWER_POSITION[1] * height_ratio]


    def get_hero_position(self):
        return self.HERO_POSITION

    def get_taunt_color(self):
        return self.TAUNT_COLOR


obj = utils()

pos = obj.get_hero_position()
print(pos)

pos = obj.get_taunt_color()
print(pos)
