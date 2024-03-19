import random

# Clinical Data Element
class ClinicalDataElement:

    # default constructor
    def __init__(self, clinical_attribute_id, belongs_to, attribute_type,
                 min, max, options):
        self.clinical_attribute_id = clinical_attribute_id
        self.belongs_to = belongs_to.upper()
        self.attribute_type = attribute_type.lower()
        self.min = min
        self.max = max
        self.options = options
        if self.attribute_type == "continuous":
            self.min = int(self.min)
            self.max = int(self.max)
        else:
            self.options = self.options.split("|")

    # Get random value
    def get_random(self):
        if self.attribute_type == "continuous":
            return random.randint(self.min, self.max)
        else:
            random_index = random.randint(0, len(self.options)-1)
            return self.options[random_index]