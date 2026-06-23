import arrow
brewing_time=arrow.utcnow().shift()
brewing_time.to('Europe/Rome')

from collections import namedtuple
chaiProfile=namedtuple("ChaiProfile",["flavor","aroma"])
