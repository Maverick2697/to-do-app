from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo.views import TaskList, TaskCreate, TaskUpdate, TaskDelete

class TestUrls(SimpleTestCase):

    def test_task_list_url(self):
        url = reverse('mytasks')
        self.assertEquals(resolve(url).func.view_class, TaskList)
    
    def test_task_create_url(self):
        url = reverse('task_create')
        self.assertEquals(resolve(url).func.view_class, TaskCreate)
    
    def test_task_update_url(self):
        url = reverse('task_update', args=[1])
        self.assertEquals(resolve(url).func.view_class, TaskUpdate)
    
    def test_task_delete_url(self):
        url = reverse('task_delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, TaskDelete)