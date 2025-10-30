from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class SMS(Notification):
    def notify(self, message):
        print(f"\n{message} notification send via SMS")

class Email(Notification):
    def notify(self, message):
        print(f"\n{message} notification send via Email")

class PushNotification(Notification):
    def notify(self, message):
        print(f"\n{message} notification send via Push Notification")

notifications = [SMS(), Email(), PushNotification()]

for n in notifications:
    n.notify(message="Welcome to the Club")

