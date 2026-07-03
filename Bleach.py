class Bankai():
    """
    A bankai is the zenith of a Soul Reaper(Shinigami)
    """

    def __init__(self, Ichigo='Tensa Zangetsu', Aizen='Kyoka Suigetsu'):
        self.Ichigo = Ichigo
        self.Aizen = Aizen
    
    def description(self):
        return f"I wonder which is stronger? {self.Ichigo} or {self.Aizen}"
    
    @classmethod
    def Humans(cls, Ichigo=None):
        if not Ichigo:
            Ichigo = 'Human'
            return cls(Ichigo, None)

print(hasattr(Bankai, '__init__'))