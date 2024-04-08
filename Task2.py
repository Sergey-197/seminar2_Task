from abc import ABC, abstractmethod

class QueueBehaviour(ABC):
    @abstractmethod
    def enqueue(self, person):
        pass

    @abstractmethod
    def dequeue(self):
        pass

class MarketBehaviour(ABC):
    @abstractmethod
    def enter_market(self, person):
        pass

    @abstractmethod
    def exit_market(self, person):
        pass

class Market(QueueBehaviour, MarketBehaviour):
    def __init__(self):
        self.queue = []

    def enqueue(self, person):
        self.queue.append(person)
        print(f"{person} has been added to the queue.")

    def dequeue(self):
        if len(self.queue) > 0:
            person = self.queue.pop(0)
            print(f"{person} has been removed from the queue.")
            return person
        else:
            print("Queue is empty.")

    def enter_market(self, person):
        print(f"{person} has entered the market.")

    def exit_market(self, person):
        print(f"{person} has exited the market.")

# Пример использования класса Market
market = Market()
market.enqueue("Alice")
market.enqueue("Bob")
person = market.dequeue()
market.enter_market(person)
market.exit_market(person)