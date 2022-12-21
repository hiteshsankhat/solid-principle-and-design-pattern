#  separation of concerns (SOC)
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self) -> str:
        return "\n".join(self.entries)

    # def save(self, fileName) -> None:
    #     pass

    # def load(self, fileName) -> None:
    #     pass

class PersistenceManager():
    @staticmethod
    def save_to_file(journal, filename):
        pass

J = Journal()
J.add_entry("I cried today")
J.add_entry("I ate a bug")
PersistenceManager.save_to_file(J, "abc.txt")
print(J)