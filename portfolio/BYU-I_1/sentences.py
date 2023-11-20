import random
import nltk


class GrammaticalQuantity:
    """Generate random grammatical sentences.

    This class provides methods to generate random sentences
    with determiners, nouns, verbs, adjectives, adverbs,
    and prepositions. The sentences can be constructed in
    different tenses (past, present, future) and quantities
    (singular or plural).

    Methods:
        get_determiner(self)
        get_noun(self, quantity)
        get_verb(self, quantity, tense)
        get_preposition(self)
        get_prepositional_phrase(self, quantity)
        get_adjective(self)
        get_adverb(self)
        make_sentence(self, quantity=None, tense=None, verb=None)

    Example usage:
        generator = GrammaticalQuantity()
        sentence = generator.make_sentence(quantity=2, tense='past')
        print(sentence)
    """
    
    # Constructor to initialize
    def __init__(self):
        self.determiners = ["A", "One", "The", "Some", "Many"]
        self.singular_nouns = ["cat", "man", "woman", "dog", "bird"]
        self.plural_nouns = ["birds", "boys", "cars", "cats", "children",
                             "dogs", "girls", "men", "rabbits", "women"]
        self.past_verbs = ["drank", "ate", "grew", "laughed", "thought",
                           "ran", "slept", "talked", "walked", "wrote"]
        self.present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                              "runs", "sleeps", "talks", "walks", "writes"]
        self.future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                             "will think", "will run", "will sleep", "will talk",
                             "will walk", "will write"]

    # sample method 1
    def get_determiner(self):
        """Return a randomly chosen determiner. A determiner is
        a word like "the", "a", "one", "some", "many".
        If quantity is 1, this function will return either "a",
        "one", or "the". Otherwise this function will return
        either "some", "many", or "the".

        Parameter
            quantity: an integer.
                If quantity is 1, this function will return a
                determiner for a single noun. Otherwise this
                function will return a determiner for a plural
                noun.
        Return: a randomly chosen determiner.
        """
        return random.choice(self.determiners)

    # sample method 1
    def get_noun(self, quantity):
        """Return a randomly chosen noun.
        If quantity is 1, this function will
        return one of these ten single nouns:
            "bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"
        Otherwise, this function will return one of
        these ten plural nouns:
            "birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"

        Parameter
            quantity: an integer that determines if
                the returned noun is single or plural.
        Return: a randomly chosen noun.
        """
        if quantity == 1:
            return random.choice(self.singular_nouns)
        else:
            return random.choice(self.plural_nouns)

    # sample method 1
    def get_verb(self, quantity, tense):
        """Return a randomly chosen verb. If tense is "past",
        this function will return one of these ten verbs:
            "drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"
        If tense is "present" and quantity is 1, this
        function will return one of these ten verbs:
            "drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"
        If tense is "present" and quantity is NOT 1,
        this function will return one of these ten verbs:
            "drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"
        If tense is "future", this function will return one of
        these ten verbs:
            "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"

        Parameters
            quantity: an integer that determines if the
                returned verb is single or plural.
            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
        Return: a randomly chosen verb.
        """
        if tense == "past":
            return random.choice(self.past_verbs)
        elif tense == "present":
            if quantity == 1:
                return random.choice(self.present_verbs)
            else:
                return random.choice(self.present_verbs).rstrip("s")
        elif tense == "future":
            return random.choice(self.future_verbs)
            
     
    def get_preposition(self):
        """Return a randomly chosen preposition
        from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

        Return: a randomly chosen preposition.
        """
        prepositions = ["about", "above", "across", "after", "along",
                        "around", "at", "before", "behind", "below",
                        "beyond", "by", "despite", "except", "for",
                        "from", "in", "into", "near", "of",
                        "off", "on", "onto", "out", "over",
                        "past", "to", "under", "with", "without"]
        return random.choice(prepositions)

    
    def get_prepositional_phrase(self, quantity):
        """Build and return a prepositional phrase composed
        of three words: a preposition, a determiner, and a
        noun by calling the get_preposition, get_determiner,
        and get_noun functions.

        Parameter
            quantity: an integer that determines if the
                determiner and noun in the prepositional
                phrase returned from this function should
                be single or plural.
        Return: a prepositional phrase.
        """
        preposition = self.get_preposition()
        determiner = self.get_determiner()
        noun = self.get_noun(quantity)

        determiner = determiner.capitalize()
        noun = noun.capitalize()

        return f"{preposition} {determiner} {noun}"
    
    
    def get_adjective(self):
       """Return a randomly chosen adjective from a list of adjectives."""
       adjectives = ["happy", "big", "green", "small", "friendly", "loud"]
       return random.choice(adjectives)

        
    def get_adverb(self):
       """Return a randomly chosen adverb from a list of adverbs."""
       adverbs = ["quickly", "quietly", "happily", "slowly", "loudly", "carefully"]
       return random.choice(adverbs)
   
    def make_sentence(self, quantity=None, tense=None, verb=None):
        """Build and return a sentence with four parts:
        a determiner, a noun, a verb, and a prepositional phrase.
        The grammatical quantity of the determiner and noun will
        match the number in the quantity parameter. The grammatical
        quantity and tense of the verb will match the number and
        tense in the quantity and tense parameters.

        Parameter
            quantity: an integer that determines if the determiner
                and noun should be single or plural.
            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
            verb: a string representing the verb.
        """
        determiner = self.get_determiner()
        if quantity is None:
            quantity = 1 if determiner in ["A", "One", "The"] else random.randint(2, 5)
        noun = self.get_noun(quantity)
        if tense is None:
            tense = random.choice(["past", "present", "future"])
        if verb is None:
            verb = self.get_verb(quantity, tense)

        determiner = determiner.capitalize()
        noun = noun.capitalize()
        
        prepositional_phrase_1 = self.get_prepositional_phrase(quantity) + ","
        prepositional_phrase_2 = self.get_prepositional_phrase(quantity) + "."
        adjective = self.get_adjective().lower()
        adverb = self.get_adverb().lower()
        return f"{determiner} {adjective} {noun} {prepositional_phrase_1} {adverb} {verb} {determiner} {adjective} {noun} {prepositional_phrase_2}"
    
  
    def check_sentence_structure(self, sentence):
        """Check the grammatical and lexical structure of a sentence.

        This method performs the following steps:
            1. Tokenization
            2. Part-of-Speech Tagging
            3. Syntax Analysis (Basic check for a complete sentence)

        Parameters
            sentence: a string representing a sentence.

        Return: True if the sentence structure is correct, False otherwise.
        """
        # Step 1: Tokenization
        tokens = nltk.word_tokenize(sentence)

        # Step 2: Part-of-Speech Tagging
        tagged_tokens = nltk.pos_tag(tokens)

        # Step 3: Basic Syntax Analysis (check for period at the end)
        if not sentence.endswith('.'):
            return False
        
        # Step 4 ensure sentence starts in sentence case and apply correct punctuations
        first_word = tokens[0].capitalize()
        if not first_word[0].isalpha():
            return False

        return True




def main():
    """Generate and print random sentences.

    This function initializes a GrammaticalQuantity generator and
    generates random sentences using different quantities (1 or random),
    tenses (past, present, future), and verbs. It then prints these
    sentences to the console.

    Example usage:
        main()
    """
    generator = GrammaticalQuantity()

    # Generate sentences with various quantities and tenses
    for quantity in [1, 1, 1, random.randint(2, 5), random.randint(2, 5), random.randint(2, 5)]:
        for tense in ["past", "present", "future"]:
            sentence = generator.make_sentence(quantity, tense)
            print(sentence)

if __name__ == "__main__":
    main()
