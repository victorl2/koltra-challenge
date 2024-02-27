from service.parser import Parser
from service.gift_service import optimal_gift_package

if __name__ == "__main__":
    parser = Parser()
    print("Welcome to the Gift Basket CLI!")
    print(f'Please enter the season for the gift basket: {', '.join(parser.seasons)} ')
    season_input = input("Enter the season: ")
    is_season_valid, season_message = parser.validate_season(season_input.strip())
    
    if not is_season_valid:
        print(season_message)
        exit(1)

    print("\nPlease enter the gifts separated by commas.")
    print("Format each gift as '<weight>g <shape>', e.g., '50g Square, 100g Circle'.")

    gift_input = input("Enter the gifts: ")
    is_gift_valid, gift_message = parser.validate_gifts(gift_input.strip())
    
    if not is_gift_valid:
        print(gift_message)
        exit(1)

    parsed_gifts = parser.parse_gifts(gift_input)

    optimal_package = optimal_gift_package(season_input, parsed_gifts)
    print(f"\nOptimal gift package for {season_input} is: {optimal_package}")

