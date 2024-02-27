from typing import List, Tuple


class Parser:
    seasons = ["spring", "summer ", "autumn ", "winter"]
    shapes = {"Square", "Rectangle", "Circle", "Oval", "Triangle"}

    def validate_season(self, season: str) -> Tuple[bool, str]:
        """
        Validate the season input to check if it matches the expected format.
        - season (str): The input string entered by the user.
        - Returns: True if the input is valid, False otherwise.
        """
        if season.lower() not in self.seasons:
            return (False, f"Invalid season: {season}, must be one of {', '.join(self.seasons)}")
        return (True, "Input is valid")
    
    def validate_gifts(self, input: str) -> Tuple[bool, str]:
        """
        Validate the input string to check if it matches the expected format.
        - input (str): The input string entered by the user.
        - Returns: True if the input is valid, False otherwise.
        """
        gifts_str = input.split(", ")

        for gift_str in gifts_str:
            parts = gift_str.split(" ")
            if len(parts) != 2:
                return (False, "Invalid format: Each gift should be in the format '<weight>g <shape>'")
            
            weight_part, shape = parts
            if not weight_part.endswith("g"):
                return (False, "Weight must be in grams")
            
            try:
                weight = int(weight_part[:-1])
                if weight < 50 or weight > 250 or weight % 50 != 0:
                    return (False, "Weight must be a multiple of 50 with a max of 250 grams")
            except ValueError:
                return (False , "Invalid weight: Weight must be a number followed by 'g'")

            if shape not in self.shapes:
                return (False, f"Invalid shape: {shape}, must be one of {', '.join(sorted(self.shapes))}")
        return (True, "Input is valid")

    @staticmethod
    def parse_gifts(input) -> List[Tuple[str, int]]:
        """
        Parse the input string of gifts and convert it into a list of tuples.
        input: A string representing a list of gifts, e.g., "50g Square, 100g Circle, ..."
        Returns: A list of tuples where each tuple is (shape, weight)
        """
        gifts_str = input.split(", ")
        gifts = []

        for gift_str in gifts_str:
            # Split each gift by space, assuming the format is always "weight shape"
            parts = gift_str.split(" ")
            weight = int(parts[0][:-1])  # Remove the 'g' and convert to int
            shape = parts[1]
            gifts.append((shape, weight))

        return gifts