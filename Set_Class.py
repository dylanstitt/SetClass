

class Set:

    def __init__(self, name, values=[]):
        self.name = name
        self.values = [i for i in values]

    
    def __str__(self):
        if len(self.values) == 0:
            return '{}'
        
        out = '{'
        for val in range(len(self.values)):
            if self.values[val] == self.values[-1]:
                out += str(self.values[val])
            else:
                out += str(self.values[val]) + ', '
        return out + '}'
    

    def power_set(self):
        result = Set(f"P({self.name})", ["∅"])
        if self.values == None:
            return result

        x = len(self.values)
        for i in range(1 << x):
            val = [self.values[j] for j in range(x) if (i & (1 << j))]
            val = tuple(val)

            if val != ():
                result.add(val)

        return result
    

    def add(self, value):
        if isinstance(value, list):
            for vals in value:
                if vals not in self.values:
                    self.values.append(vals)
            self.values.sort()

        if isinstance(value, int):
            if value not in self.values:
                self.values.append(value)
            self.values.sort()

        else:
            if value not in self.values:
                self.values.append(value)


    def has_element(self, value):
        if value in self.values:
            return True
        return False


    def cardinality(self):
        return len(self.values)


    def is_subset(self, s):
        if len(self.values) == 0 or self.values == s:
            return True
        
        needed = len(self.values)
        total = 0
        for val in self.values:
            if val in s.values:
                total += 1

        if needed == total:
            return True
        
        return False


    def cartesian_product(self, s):
        new = Set("Car Product")
        for i in self.values:
            for j in s.values:
                new.add((i, j))
        return new


    def union(self, s):
        new = Set('Union', s.values)
        for val in self.values:
            if val not in new.values:
                new.add(val)
        return new
        


    def intersection(self, s):
        new = Set('Intersection')

        if s.cardinality() < len(self.values):
            smallest = s.values
            larger = self.values

        else:
            smallest = self.values
            larger = s.values

        for val in smallest:
            if val in larger:
                new.add(val)
        return new


    def difference(self, s):
        new = Set('Difference')
        
        if s.cardinality() < len(self.values):
            larger = self.values
            smallest = s.values

        else:
            smallest = s.values
            larger = self.values

        for val in larger:
            if val not in smallest:
                new.add(val)

        return new
    