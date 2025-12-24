with open("www/subjects/inputs/day_12.txt", "r") as sub:
    content = sub.read()

parsed_input = content.strip()

def get_shapes_and_regions(
    parsed_input: str
) -> tuple[list[list[str]], list[dict[str, list[int] | int]]]:
    shapes = [
        elem[2:].strip().split("\n")
        for elem in parsed_input.split("\n\n")[:-1]
    ]

    regions = [
        {elem.split()[0]: [int(num) for num in elem.split()[1:]]}
        for elem in parsed_input.split("\n\n")[-1].split("\n")
    ]

    regions_can_be_fill = []

    for region in regions:
        for name, value in region.items():
            region_widht = int(name[:-1].split('x')[0])
            region_height = int(name[:-1].split('x')[1])
            air = region_widht * region_height
            air_of_shapes = sum(
                shapes[idx].count("#") * int(nb_shape) for idx, nb_shape in enumerate(value)
            )
            if air >= air_of_shapes:
                regions_can_be_fill.append(
                    {name: value, "widht": region_widht, "height": region_height}
                )

    return shapes, regions_can_be_fill

def letter_from_index(index):
     return chr(index + 65)


def get_all_transformations(shape: list[str]) -> list[list[str]]:

    def rotate(shape):
        return [''.join(row) for row in zip(*shape[::-1])]

    def flip(shape):
        return [row[::-1] for row in shape]

    unique_shapes = set()
    result = []
    current = shape

    for flip_first in [False, True]:
        if flip_first:
            current = flip(shape)

        for _ in range(4):
            shape_tuple = tuple(current)
            if shape_tuple not in unique_shapes:
                unique_shapes.add(shape_tuple)
                result.append(current)
            current = rotate(current)

    return result

def get_next_empty(grid: list[list[int]],) -> tuple[int | None, int | None]:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                return x, y
    return None, None

def can_be_place(shape, x, y, shape_w, shape_h, grid):
    grid_w = len(grid)
    grid_h = len(grid[0])
    # si la shape depasse en x ou en y de la grille on peut pas la placer
    if x + shape_w > grid_w or y + shape_h > grid_h:
        return False

    # pour chaque colonne dans la shape
    for y_shape in range(shape_h):
        row = shape[y_shape]
        #  Pour chaque symbol dans la colonne
        for x_shape in range(shape_w):
            # Si le symbol est plein (#)
            if row[x_shape] == '#':
                # Si la palce dans la grille est prise on peu pas placer la shape
                if grid[y + y_shape][x + x_shape] != 0:
                    # print(f"{shape} ne peut pas etre placer")
                    return False
    # On a verifier qe tout les emplacement de la grille qui doivent accueillir la forme
    # sont vide donc on renvoie True
    return True

def place_at(shape, x, y, shape_w, shape_h, shape_id, grid, placed):
    # pour chaque colonne dans la shape
    for y_shape in range(shape_h):
        row = shape[y_shape]
        #  Pour chaque symbol dans la colonne
        for x_shape in range(shape_w):
            # Si le symbole est plein (#)
            if row[x_shape] == '#':
                # On ajoute a la grille la lettre qui correspond a l'index (0 => A, 1 => B, ...)
                grid[y + y_shape][x + x_shape] = letter_from_index(shape_id) + str(placed[shape_id])

def remove_at(shape, x, y, shape_w, shape_h, grid):
    # pour chaque colonne dans la shape
    for y_shape in range(shape_h):
        row = shape[y_shape]
        #  Pour chaque symbol dans la colonne
        for x_shape in range(shape_w):
            # Si le symbole est plein (#)
            if row[x_shape] == '#':
                #  On enleve le symbole et on remet 0 qui est le caractere vide pour
                # notre grille
                grid[y + y_shape][x + x_shape] = 0

def backtrack(
    idx: int,
    # IDX correspond a l'index de la shape que l'on essie de placer
    # (shape et tansformations)
    grid: list[list[int]],
    shapes_and_transformations_info: list[list[str]],
    placed: list[int],
    counts: list[int],
) -> bool:
    # print(f"{placed = }")
    if all(nb_placed == nb_count for nb_placed, nb_count in zip(placed, counts)):
        print("On a placer toutes les shapes le bon nombre de fois")
        return True

    if idx >= len(shapes_and_transformations_info):
        print("j'ai fait toutes les shapes et leurs transforamtions")
        return False

    x, y = get_next_empty(grid)
    if x is None: #if x == None then y == None
        print("On est arriver au bout de la grille sans pouvoir placer toutes les formes")
        return False

    grid_height = len(grid)
    grid_widht = len(grid[0])

    #  On essaie de placer une forme
    for idx_shape in range(idx, len(shapes_and_transformations_info)):
        shape_id = shapes_and_transformations_info[idx_shape]["idx"]
        shape = shapes_and_transformations_info[idx_shape]["shape"]

        shape_height = len(shape)
        shape_widht = len(shape[0])

        if placed[shape_id] >= counts[shape_id]:
            continue

        # On essaie toutes les positions jusqu'a ce qu'il y en ai une de valide

        # pour chaque y dans range(le premier y vide jusqu'a le y max (hauteur de la grille) - la hauteur de la forme)
        # (+1 car index de base est 0)
        for try_y in range(y, grid_height - shape_height + 1):
            #  Le premier x est le premier x trouver avec get_next_empty si y est le
            # premier y vide trouvé sinon x = 0
            first_x = x if try_y == y else 0
            # Pour chaque x dans range(le premier x cide de la line (y) jusqu'a le x max (largeur de la grille) - la largeur de la forme)
            # (+1 car index de base est 0)
            for try_x in range(first_x, grid_widht - shape_widht + 1):
                #  On verifie qu l'on peut placer la forme
                if can_be_place(
                    shape,
                    try_x,
                    try_y,
                    shape_widht,
                    shape_height,
                    grid
                ):
                    # Si oui on la place
                    place_at(
                        shape,
                        try_x,
                        try_y,
                        shape_widht,
                        shape_height,
                        shape_id,
                        grid,
                        placed,
                    )
                    # Et on ajoute 1 au tableau du compte des forme placée a l'id
                    # correspondant a la forme
                    # print(f"On a placer la forme {shape_id}")
                    placed[shape_id] += 1

                    # On lance la suite avec l'id de la forme que l'on vient de placer
                    if backtrack(
                        idx_shape,
                        grid,
                        shapes_and_transformations_info,
                        placed,
                        counts,
                    ):
                        # # print("On a placer la forme")
                        return True

                    # il y a pas pu tout placer donc on enleve la forme
                    remove_at(
                        shape,
                        try_x,
                        try_y,
                        shape_widht,
                        shape_height,
                        grid
                    )
                    # print(f"On a enleve la forme {shape_id}")
                    placed[shape_id] -= 1

    # print("On est a la fin")
    return False

def place(shape, x, y, shape_w, shape_h, shape_id, grid):
    # pour chaque colonne dans la shape
    for y_shape in range(shape_h):
        row = shape[y_shape]
        #  Pour chaque symbol dans la colonne
        for x_shape in range(shape_w):
            # Si le symbole est plein (#)
            if row[x_shape] == '#':
                # On ajoute a la grille la lettre qui correspond a l'index (0 => A, 1 => B, ...)
                grid[y + y_shape][x + x_shape] = letter_from_index(shape_id)

def remove(shape, x, y, shape_w, shape_h, grid):
    # pour chaque colonne dans la shape
    for y_shape in range(shape_h):
        row = shape[y_shape]
        #  Pour chaque symbol dans la colonne
        for x_shape in range(shape_w):
            # Si le symbole est plein (#)
            if row[x_shape] == '#':
                #  On enleve le symbole et on remet 0 qui est le caractere vide pour
                # notre grille
                grid[y + y_shape][x + x_shape] = 0

def solve(parsed_input: str) -> int:
    shapes, regions_can_be_fill = get_shapes_and_regions(parsed_input)
    # print(f"{shapes = }")
    # print(f"{regions_can_be_fill = }")

    for idx, region in enumerate(regions_can_be_fill):
        # if idx == 0 or idx == 2:
        #     continue
        grid = [[0] * region["widht"] for _ in range(region["height"])]

        # print(f"{grid = }")

        transformations = [get_all_transformations(shape) for shape in shapes]
        # print(f"{transformations = }")

        shapes_and_transformations_info = []
        for idx_shape, _ in enumerate(shapes):
            for transformation in transformations[idx_shape]:
                shapes_and_transformations_info.append({"idx":idx_shape, "shape": transformation})
        # print(f"{shapes_and_transformations_info = }")

        placed_shapes_by_id = [0] * len(shapes)
        # print(f"{placed_shapes_by_id = }")

        count_shap_by_id = list(region.values())[0]
        # print(f"{count_shap_by_id = }")

        # print()
        res = backtrack(0, grid, shapes_and_transformations_info, placed_shapes_by_id, count_shap_by_id)
        print(f"region n°{idx} = {res}")
        print(grid)
        print()
        # print(backtrack(0, grid, shapes_and_transformations_info, placed_shapes_by_id, count_shap_by_id))

print(solve(parsed_input))

#  CODE QUI MARCHE PAS MAILS IL Y A LES EXPLICATION EN COMMENTAIRE
