class Disk:
    def __init__(self, total, used):
        self._total = total
        self._used = used
    
    @property
    def total(self):
        return self._total
    
    @property
    def used(self):
        return self._used
    
    @property
    def free(self):
        return self._total - self._used
    
    @property
    def used_perc(self):
        return self._used / self._total
    
    def __str__(self):
        return f"Disk[total: {self._total} Gb, used: {self._used} Gb]"
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, other):
        return self.used_perc < other.used_perc
    

