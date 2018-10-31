class Poem:
    _poemCount = 0


    def __init__(self, author, poemName,):
        self.author = author
        self.poemName = poemName
        Poem._poemCount += 1


    def setPoemText(self, *text):
        self.text = list(text)


    def setPoemType(self, haikuPoem):
        self.haikumPoem = haikuPoem


    def getPoemText(self):
        return self.text

    def getPoemType(self):
        return self.haikumPoem

    def __str__(self):
        return "\"{}\" by {} is {}:\n\n{}\n".format(
            self.poemName,
            self.author,
            "a Haiku Poem" if self.getPoemType() else "NOT a Haiku Poem",
            "\n".join(str(x)for x in self.getPoemText()))

def main():
    jClement = Poem("Joyce Clement","Period")
    jClement.setPoemText("Period ", "One blue egg all summer long", "Now gone")
    jClement.setPoemType(True)
    print(jClement)

    Shakespeare = Poem("William Shakespeare","All the world's a stage")
    Shakespeare.setPoemText("All the world's a stage,", "And all the men and women merely players;", "They have their exits and their entrances,", "And one man in his time plays many parts,")
    Shakespeare.setPoemType(False)
    print(Shakespeare)

    kShuson = Poem("Kato Shuson","An Ant")
    kShuson.setPoemText("I kill an ant", "and realize my three children", "have been watching.")
    kShuson.setPoemType(True)
    print(kShuson)


if __name__ == '__main__':
    main()


