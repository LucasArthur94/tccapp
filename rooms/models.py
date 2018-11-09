from django.db import models

class Room(models.Model):
    BLOCK_A = 'A'
    BLOCK_B = 'B'
    BLOCK_C = 'C'
    BLOCK_D = 'D'

    BLOCK_OPTIONS = (
        (BLOCK_A, 'Bloco A'),
        (BLOCK_B, 'Bloco B'),
        (BLOCK_C, 'Bloco C'),
        (BLOCK_D, 'Bloco D'),
    )

    FLOOR_0 = 'T'
    FLOOR_1 = '1'
    FLOOR_2 = '2'

    FLOOR_OPTIONS = (
        (FLOOR_0, 'Térreo'),
        (FLOOR_1, 'Primeiro'),
        (FLOOR_2, 'Segundo'),
    )

    REQUIRED_FIELDS = ('block', 'floor', 'identifier')

    block = models.CharField(
        max_length=1,
        choices=BLOCK_OPTIONS,
        default=BLOCK_A,
    )
    floor = models.CharField(
        max_length=1,
        choices=FLOOR_OPTIONS,
        default=FLOOR_0,
    )
    identifier = models.CharField(
        max_length=2,
    )
