from random_madlibs_samples import code_madlibs, zombie_madlibs, hungergames_madlibs
import random

madlibs_choice = random.choice([code_madlibs, zombie_madlibs, hungergames_madlibs])
madlibs_choice.madlib()