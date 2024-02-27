from typing import List, Tuple
from collections import Counter
from itertools import combinations
    
def optimal_gift_package(season: str, gifts: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    season_rules = {
        'spring': [4, 5, 6],
        'summer': [1, 2, 3, 4, 5, 6],
        'autumn': [1, 2, 3, 6],
        'winter': [1, 4, 6]
    }
    optimal_basket = find_optimal_basket(season_rules[season], gifts)
    return optimal_basket

def __basket_weight(basket: List[Tuple[str, int]]) -> int:
    return sum(weight for _, weight in basket)

def __get_basket_type(basket: List[Tuple[str, int]]) -> int:
    shapes = [shape for shape, _ in basket]
    weights = [weight for _, weight in basket]
    shape_counts = Counter(shapes)
    weight_counts = Counter(weights)

    if len(shape_counts) == 5 and len(weight_counts) == 5:
        return 1 # Perfect Variety
    elif len(shape_counts) == 1 and len(weight_counts) == 5:
        return 2 # Weight Variety
    elif len(shape_counts) == 5 and len(weight_counts) == 1:
        return 3 # Shape Variety
    elif len(shape_counts) == 2 and len(set(shape_counts.values())) == 1 and len(weight_counts) == 1:
        return 4 # Perfect Pairing
    elif len(shape_counts) == 2 and len(weight_counts) > 1:
        return 5 # Shape Pairing
    else:
        return 6 # Discount Basket

def find_optimal_basket(season_rules: List[int], gifts: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    all_combinations = list(combinations(gifts, 5)) 
        
    optimal_basket = None
    optimal_basket_type = 7 
    optimal_basket_weight = 0

    for combo in all_combinations:
        basket_type = __get_basket_type(combo)
        if basket_type in season_rules:
            combo_weight = __basket_weight(combo)
            if optimal_basket is None or \
               (season_rules.index(basket_type) < season_rules.index(optimal_basket_type) or \
                (basket_type == optimal_basket_type and combo_weight > optimal_basket_weight)):
                optimal_basket = combo
                optimal_basket_type = basket_type
                optimal_basket_weight = combo_weight

    return list(optimal_basket) if optimal_basket else []