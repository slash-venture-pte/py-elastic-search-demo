from datetime import datetime, timedelta
import random
import string
from dhc.data.constant import statuses, words
from random_word import RandomWords

randomWords = RandomWords()


class RandomData():
    seed_words = words

    def __init__(self) -> None:
        self.seed_words = randomWords.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", sortBy="alpha", sortOrder="asc", limit=100)
        if self.seed_words == None:
          self.seed_words = words
  
    def init_words(self):
      self.seed_words = randomWords.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", sortBy="alpha", sortOrder="asc", limit=100)
      if self.seed_words == None:
        self.seed_words = words

    def get_id(self):
        """Look, random numbers!"""
        return random.randint()

    def get_lag(self):
        return random.uniform(9.50, 11.99)

    def get_lng(self):
        return random.uniform(99, 104.99)

    def get_price(self):
        return random.random()

    def get_status(self):
        word =  ''.join(random.sample(statuses, 1))
        return word

    def get_str(self, k: int, ntokens: int,
                pool: str = string.ascii_letters) -> set:
        """Generate a set of unique string tokens.

        k: Length of each token
        ntokens: Number of tokens
        pool: Iterable of characters to choose from

        For a highly optimized version:
        https://stackoverflow.com/a/48421303/7954504
        """

        seen = set()

        # An optimization for tightly-bound loops:
        # Bind these methods outside of a loop
        join = ''.join
        add = seen.add

        while len(seen) < ntokens:
            token = join(random.choices(pool, k=k))
            add(token)
        return list(seen)

    def get_name(self):
        len = random.randint(1, 5)
        print('self.seed_words')
        print(self.seed_words)
        words = random.sample(sorted(self.seed_words), len)
        return ' '.join(list(words))

    def get_desc(self, seed = 400):
        len = random.randint(10, 20)
        words = random.sample(self.seed_words, len)
        return ' '.join(list(words))

    def get_date(self):
        current = datetime.now()
        hours = random.randrange(60)
        return current + timedelta(hours=hours)
