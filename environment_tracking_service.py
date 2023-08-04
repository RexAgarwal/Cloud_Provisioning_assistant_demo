# environment_tracking_service.py

class EnvironmentTrackingService:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def track_temporary_environment(self, environment_id, user_id, expiration_date):
        # Simulate tracking temporary environment
        print(f"Tracking temporary environment: {environment_id}, User ID: {user_id}, Expiration Date: {expiration_date}")
        # Set up notifications for developers when their environments are about to expire
        self.notification_service.subscribe(user_id, self)

    def notify_developer(self, message):
        # Simulate sending notification to developers
        self.notification_service.send_notification(self,message)
        print(f"Notifying developer: {message}")

    def request_extension(self, environment_id, user_id):
        # Simulate requesting extension for temporary environment
        print(f"Requesting extension for Environment ID: {environment_id}, User ID: {user_id}")
        return {'status': 'pending'}

    def purge_environment(self, environment_id):
        # Simulate purging the specified environment
        print(f"Purging environment: {environment_id}")
        return {'status': 'success'}

# Observer Pattern
class NotificationService:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, user_id, observer):
        self.subscribers[user_id] = observer

    def unsubscribe(self, user_id):
        self.subscribers.pop(user_id, None)

    def send_notification(self, message):
        for user_id in self.subscribers:
            self.subscribers[user_id].notify_developer(message)
