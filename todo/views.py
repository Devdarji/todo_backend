# Create your views here.
from rest_framework.views import APIView

from todo import utils as todo_utils


class TodoListView(APIView):
    @staticmethod
    def get(request):
        return todo_utils.create_response(data={}, code=200)
