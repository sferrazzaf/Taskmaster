from django.test import TestCase
from models import Task
from views import movetask
from django.utils import timezone


class TaskMethodTests(TestCase):

    def test_was_moved_correctly(self):
        x = Task.objects.create(text="First", priority=1, created=timezone.now())
        y = Task.objects.create(text="Second", priority=2, created=timezone.now())
        z = Task.objects.create(text="Third", priority=3, created=timezone.now())
        movetask(z.id, 1)
        self.assertEqual(Task.objects.get(id=x.id).priority, 2)
        self.assertEqual(Task.objects.get(id=y.id).priority, 3)
        self.assertEqual(Task.objects.get(id=z.id).priority, 1)
        movetask(z.id, 3)
        self.assertEqual(Task.objects.get(id=x.id).priority, 1)
        self.assertEqual(Task.objects.get(id=y.id).priority, 2)
        self.assertEqual(Task.objects.get(id=z.id).priority, 3)
        movetask(x.id, 3)
        self.assertEqual(Task.objects.get(id=x.id).priority, 3)
        self.assertEqual(Task.objects.get(id=y.id).priority, 1)
        self.assertEqual(Task.objects.get(id=z.id).priority, 2)
