"""
Problem Statement:
You are building a system that creates objects.
For example:
You need to create different types of notifications.
- Email Notification
- SMS Notification
- Push Notification

So here bad design would be

class NotificationService:
    def send(self, notification_type):
        if notification_type == "email":
            sender = EmailSender()
        if notification_type == "sms":
            sender = SMSSender()
        sender.send()

Problems:
- If-else keeps growing
-  Every new type - Modify this class
- Violates open-close principle
- Object creational logic is mixed with business logic.

These problems gets solved by Factory pattern design principle.
So the idea is to create a concrete factory class where the object
creational logic is handled.

Note: Factory pattern does not remove if-else completely. It just
centralized it rather than scatterd everywhere.
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending email.")


class SMSNotification(Notification):
    def send(self):
        print("Sendiong SMS")


class PushNotification(Notification):
    def send(self):
        print("Pushing Notification")


class NotificationFactory:
    @staticmethod
    def get_notification_object(type):
        if type == "email":
            return EmailNotification()
        elif type == "sms":
            return SMSNotification()
        elif type == "push":
            return PushNotification()
        else:
            raise ValueError("Invalid type.")


# Client code
factory = NotificationFactory()
notification = factory.get_notification_object("email")
notification.send()
