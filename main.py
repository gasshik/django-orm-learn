from django_setup import *
from lesson.models import Task, User

# user1 = User.objects.create(name="Кирило", email="kirillgarhsnov@gmail.com", role="user")
# user2 = User.objects.create(name="Андрій", email="ostapenko.andrii@gmail.com", role="user")
# user3 = User.objects.create(name="Вова", email="lebedenko.vova@gmail.com", role="user")

print(User.objects.all())

# user2.role = "admin"
# user2.save()
print(User.objects.get(id=2))

task1 = Task.objects.create(
    title="Зробити систему тасків",
    description="Зробити систему управління тасками",
    assigned_to=User.objects.get(id=2),
)
task2 = Task.objects.create(
    title="Створити Django моделі для системи блогу та коментарів",
    description="Створити екземпляр постів та забезпечте взаємодію, наприклад, додавання коменатрів до посту чи редагування посту.",
    assigned_to=User.objects.get(id=3),
)

print(Task.objects.all())

task1.status = "complited"
task1.save()
print(task1)

task2.assigned_to = User.objects.get(id=1)
task2.save()
print(task2, task2.assigned_to)
