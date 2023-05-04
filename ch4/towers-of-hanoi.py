def move_tower(height, startPole, midPole, endPole):
    if height < 1:
        return
    move_tower(height - 1, startPole, endPole, midPole)
    move_disk(startPole, endPole)
    move_tower(height - 1, midPole, startPole, endPole)


# helper function
def move_disk(start, end):
    print("Move top disk from", start, "to", end)


# sample call:
move_tower(3, "A", "B", "C")

