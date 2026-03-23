import random
import math


# ==========================================
# TASK 1: Wizard Fight Simulation
# ==========================================
class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Wizard:
    def __init__(self, name, hp, strength=0, defense=0, agility=0):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defense = defense
        self.agility = agility
        self.attacks = []
        self.statuses = {'stunned': False, 'burning': 0}

    def add_attack(self, attack):
        self.attacks.append(attack)

    def is_alive(self):
        return self.hp > 0

    def attack(self, opponent):
        if self.statuses['stunned']:
            self.statuses['stunned'] = False
            return f"{self.name} is stunned and skips the turn!"

        if not self.attacks:
            return f"{self.name} has no attacks!"

        chosen = random.choice(self.attacks)
        base_dmg = chosen.damage + self.strength
        multiplier = random.uniform(0.8, 1.2)
        total_dmg = int(base_dmg * multiplier)

        # Dodge mechanics
        if random.random() < opponent.agility:
            return f"{self.name} uses {chosen.name}, but {opponent.name} dodged!"

        # Defense blocking
        blocked = int(total_dmg * opponent.defense)
        final_dmg = max(0, total_dmg - blocked)
        opponent.hp -= final_dmg

        return f"{self.name} hits {opponent.name} with {chosen.name} for {final_dmg} damage!"


def fight(wizard1, wizard2):
    turn = 0
    while wizard1.is_alive() and wizard2.is_alive():
        turn += 1
        attacker, defender = (wizard1, wizard2) if turn % 2 != 0 else (wizard2, wizard1)
        action_msg = attacker.attack(defender)
        yield f"Turn {turn}: {action_msg}"

        if not defender.is_alive():
            yield f"Outcome: {defender.name} is defeated! {attacker.name} wins!"


class Tournament:
    def __init__(self, wizards):
        self.wizards = wizards

    def __iter__(self):
        # Fight sequentially in pairs
        for i in range(0, len(self.wizards) - 1, 2):
            w1, w2 = self.wizards[i], self.wizards[i + 1]
            f = fight(w1, w2)
            for log in f:
                pass  # fast forward to the end
            yield log  # yield the outcome of the fight


def random_stats_generator():
    while True:
        yield {'hp': random.randint(50, 100), 'strength': random.randint(5, 15),
               'defense': random.uniform(0.1, 0.3), 'agility': random.uniform(0.1, 0.3)}


# ==========================================
# TASK 2: FibonacciSequence Iterator
# ==========================================
class FibonacciIterator:
    def __init__(self, n, reverse=False):
        self.n = n
        self.idx = 0
        self.seq = self._generate()
        if reverse:
            self.seq.reverse()

    def _generate(self):
        seq, a, b = [], 0, 1
        for _ in range(self.n):
            seq.append(a)
            a, b = b, a + b
        return seq

    def __next__(self):
        if self.idx < self.n:
            val = self.seq[self.idx]
            self.idx += 1
            return val
        raise StopIteration


class FibonacciSequence:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return FibonacciIterator(self.n)

    def reverse_iter(self):
        return FibonacciIterator(self.n, reverse=True)


# ==========================================
# TASK 3: Product & Cart
# ==========================================
class Product:
    def __init__(self, name, price, category):
        self.name, self.price, self.category = name, price, category


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def total_price(self):
        total = 0
        for item in self.items:
            price = item.price * 2 if item.category == "electronics" else item.price
            price = price * 0.90 if item.category == "food" else price
            total += price
        return total * 0.85  # 15% discount on the entire cart

    def show_items(self):
        for item in self.items: print(f"{item.name}: ${item.price} ({item.category})")

    def clear(self):
        self.items.clear()


# ==========================================
# TASK 4: Sum of Squares
# ==========================================
sum_squares = sum(x ** 2 for x in range(1, 1000001))

# ==========================================
# TASK 5: Longest Word Search
# ==========================================
text = "The goal of this task is to design and implement a system simulating a fight"
longest_word = max((word.strip(".,!?") for word in text.split()), key=len)

# ==========================================
# TASK 6: List Filtering
# ==========================================
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


div_by_7 = (num for sub in lst for num in sub if num % 7 == 0)
primes = (num for sub in lst for num in sub if is_prime(num))


# ==========================================
# TASK 7: Infinite Loop Generator
# ==========================================
def infinite_counter():
    i = 0
    while True:
        yield i
        i += 1


# ==========================================
# TASK 8: RGB Generator
# ==========================================
def RGB_generator():
    while True:
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        if r + g + b > 400:
            yield (r, g, b)


# ==========================================
# TASK 9: Playlist Management
# ==========================================
class Song:
    def __init__(self, name, duration, author):
        self.name, self.duration, self.author = name, duration, author


class Playlist:
    def __init__(self): self.songs = []

    def add_song(self, song): self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs: self.songs.remove(song)

    def __iter__(self): return iter(self.songs)

    def __len__(self): return len(self.songs)

    def __getitem__(self, index): return self.songs[index]

    def long_songs(self):
        return (song for song in self.songs if song.duration > 200)


# ==========================================
# TASK 10: Sentence Generator
# ==========================================
def sentence_generator(subjects, verbs, objects):
    while True:
        yield f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."


# ==========================================
# TASK 11: Infinite Dice Simulator
# ==========================================
def dice():
    while True:
        yield random.randint(1, 6)