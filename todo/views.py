from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        # Placeholder for integration hooks
        try:
            from integrations.google_calendar import add_event
            from integrations.whatsapp import send_whatsapp_reminder
            from integrations.slack import send_slack_notification
            from integrations.notion import save_to_notion

            if task.due_date:
                add_event(task)
            send_whatsapp_reminder(task)
            send_slack_notification(task)
            save_to_notion(task)
        except Exception:
            # In a real application, proper logging should be added
            pass
