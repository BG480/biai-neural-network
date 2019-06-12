
class Player:
    def __init__(self, name, position, crossing, finishing, heading_accuracy, short_passing, volleys,
                 dribbling, curve, free_kick_accuracy, long_passing, ball_control,
                 acceleration, sprint_speed, agility, reactions, balance, shot_power,
                 jumping, stamina, strength, long_shots, aggression, interceptions,
                 positioning, vision, penalties, composure, marking, standing_tackle,
                 sliding_tackle, gk_diving, gk_handling, gk_kicking, gk_positioning,
                 gk_reflexes, overall):
        self._name = name
        self._position = position
        self._crossing = crossing
        self._finishing = finishing
        self._heading_accuracy = heading_accuracy
        self._short_passing = short_passing
        self._volleys = volleys
        self._dribbling = dribbling
        self._curve = curve
        self._free_kick_accuracy = free_kick_accuracy
        self._long_passing = long_passing
        self._ball_control = ball_control
        self._acceleration = acceleration
        self._sprint_speed = sprint_speed
        self._agility = agility
        self._reactions = reactions
        self._balance = balance
        self._shot_power = shot_power
        self._jumping = jumping
        self._stamina = stamina
        self._strength = strength
        self._long_shots = long_shots
        self._aggression = aggression
        self._interceptions = interceptions
        self._positioning = positioning
        self._vision = vision
        self._penalties = penalties
        self._composure = composure
        self._marking = marking
        self._standing_tackle = standing_tackle
        self._sliding_tackle = sliding_tackle
        self._gk_diving = gk_diving
        self._gk_handling = gk_handling
        self._gk_kicking = gk_kicking
        self._gk_positioning = gk_positioning
        self._gk_reflexes = gk_reflexes
        self._overall = overall

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @property
    def crossing(self):
        return self._crossing

    @property
    def finishing(self):
        return self._finishing

    @property
    def heading_accuracy(self):
        return self._heading_accuracy

    @property
    def short_passing(self):
        return self._short_passing

    @property
    def volleys(self):
        return self._volleys

    @property
    def dribbling(self):
        return self._dribbling

    @property
    def curve(self):
        return self._curve

    @property
    def free_kick_accuracy(self):
        return self._free_kick_accuracy

    @property
    def long_passing(self):
        return self._long_passing

    @property
    def ball_control(self):
        return self._ball_control

    @property
    def acceleration(self):
        return self._acceleration

    @property
    def sprint_speed(self):
        return self._sprint_speed

    @property
    def agility(self):
        return self._agility

    @property
    def reactions(self):
        return self._reactions

    @property
    def balance(self):
        return self._balance

    @property
    def shot_power(self):
        return self._shot_power

    @property
    def jumping(self):
        return self._jumping

    @property
    def stamina(self):
        return self._stamina

    @property
    def strength(self):
        return self._strength

    @property
    def long_shots(self):
        return self._long_shots

    @property
    def aggression(self):
        return self._aggression

    @property
    def interceptions(self):
        return self._interceptions

    @property
    def positioning(self):
        return self._positioning

    @property
    def vision(self):
        return self._vision

    @property
    def penalties(self):
        return self._penalties

    @property
    def composure(self):
        return self._composure

    @property
    def marking(self):
        return self._marking

    @property
    def standing_tackle(self):
        return self._standing_tackle

    @property
    def sliding_tackle(self):
        return self._sliding_tackle

    @property
    def gk_diving(self):
        return self._gk_diving

    @property
    def gk_handling(self):
        return self._gk_handling

    @property
    def gk_kicking(self):
        return self._gk_kicking

    @property
    def gk_positioning(self):
        return self._gk_positioning

    @property
    def gk_reflexes(self):
        return self._gk_reflexes

    @property
    def overall(self):
        return self._overall

    def __str__(self):
        return "{} {} {}".format(self.name, self.position, self.overall)