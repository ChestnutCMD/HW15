def animal_for_id(animals, animal_id):
    ani = [animal for animal in animals if animal_id in animal]

    return ani[0]
