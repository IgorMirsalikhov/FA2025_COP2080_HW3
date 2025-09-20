from funcs import remove_min_max 
from funcs import seven_segment
from funcs import generate_html_tag
from funcs import check_negative
from funcs import even_or_odd
from funcs import conv_aggr


if __name__ == "__main__":
    #####################
    # Test remove_min_max
    #####################
    print(remove_min_max({1, 2, 3, 4, 5}, 1))
    print(remove_min_max({1, 2, 3, 4, 5}, 2))
    print(remove_min_max({1, 2, 3, 4, 5}, 3))
    print(remove_min_max({1, -98, 3, 400, 5}, 1))
    print()
    #####################
    # Test seven_segment
    #####################
    print(seven_segment({'B', 'C', 'G', 'F', 'A', 'a', 'c', 'd', 'f', 'g', 'b'}))
    print(seven_segment({'B', 'C', 'A', 'd', 'f', 'g', 'b'}))
    print(seven_segment({'B', 'C', 'A', 'b', 'c'}))
    print(seven_segment({'b', 'c', 'a'}))
    print(seven_segment({'B', 'C'}))
    print()

    ########################
    # Test generate_html_tag
    ########################
    print()
    print(generate_html_tag("div", "Hello", class_="container", id="main"))
    print(generate_html_tag("p", "Welcome to my site", style="color: blue"))
    print(generate_html_tag("span", "Click here"))
    print(generate_html_tag("a", "Visit Site", href="https://example.com", 
                            target="_blank", class_="link"))

    print()
    print(check_negative([7, 5, 4, -6]))
    print(check_negative([-7, -5, -4, -6]))
    print(check_negative([7, 5, 4, 6]))
    print(check_negative([]))
    print()

    ########################
    # Test even_or_odd
    ########################
    print(even_or_odd(5))
    print(even_or_odd(10))

    
    ########################
    # Test conv_aggr
    ########################
    print()
    print(conv_aggr([("a", 7), ("b", 8), ("a", 10)]))
    print(conv_aggr([]))
    print(conv_aggr([("a", 5), ("a", -5), ("a", 0)]))

