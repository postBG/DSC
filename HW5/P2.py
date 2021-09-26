def P2(input_filename: str, output_filename: str) -> None:
    with open(input_filename, 'r') as f:
        read_contents = [l.strip().split(' ') for l in f.readlines()]

    with open(output_filename, 'w') as f:
        for name, number, weight in read_contents:
            f.write(f"{name}'s atomic number is {number} and atomic weight is {weight}\n")
