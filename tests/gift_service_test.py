from src.service.gift_service import optimal_gift_package

def test_optimal_gift_package():
    # Test case 2: Winter, expecting Perfect Variety or Perfect Pairing prioritized
    season = "winter"
    gifts = [("Square", 200), ("Square", 200), ("Circle", 200), ("Triangle", 200), ("Oval", 200), ("Rectangle", 200), ("Square", 50)]
    assert optimal_gift_package(season, gifts) in [
        [("Square", 200), ("Square", 200), ("Circle", 200), ("Triangle", 200), ("Oval", 200)],
        [("Square", 200), ("Square", 200), ("Square", 200), ("Triangle", 200), ("Oval", 200)]  # This is also a valid optimal basket for Winter
    ]

    # Test case 3: Autumn, expecting Shape Variety or Weight Variety prioritized
    season = "autumn"
    gifts = [("Square", 150), ("Square", 150), ("Square", 150), ("Square", 150), ("Square", 150), ("Square", 100), ("Square", 50)]
    assert optimal_gift_package(season, gifts) == [("Square", 150), ("Square", 150), ("Square", 150), ("Square", 150), ("Square", 150)]

    # Test case 4: Spring, expecting Shape Pairing or Perfect Pairing
    season = "spring"
    gifts = [("Square", 50), ("Square", 50), ("Circle", 50), ("Circle", 50), ("Rectangle", 50), ("Oval", 50), ("Triangle", 50)]
    assert optimal_gift_package(season, gifts) in [
        [("Square", 50), ("Square", 50), ("Circle", 50), ("Circle", 50), ("Rectangle", 50)],
        [("Square", 50), ("Square", 50), ("Circle", 50), ("Circle", 50), ("Oval", 50)]  # This is also a valid optimal basket for Spring
    ]