# Create your views here.
from rest_framework.views import APIView

from django.utils import timezone

from todo import utils as todo_utils
from todo import serializers as todo_serializers
from todo import models as todo_models


# Done
class GetCardItemView(APIView):
    @staticmethod
    def get(request):
        all_card_instance = todo_models.CardItem.objects.filter(is_active=True)

        return todo_utils.create_response(
            data=[card_item.get_card_details() for card_item in all_card_instance],
            code=200,
        )


# Done
class CreateCardView(APIView):
    @staticmethod
    def post(request):
        all_card_instance = todo_models.CardItem.objects.filter(is_active=True)

        serializer_instance = todo_serializers.CardSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return todo_utils.create_response(serializer_instance.errors, 400)

        if not serializer_instance.validated_data.get("task_instance"):
            todo_models.CardItem.objects.create(**serializer_instance.validated_data)

        return todo_utils.create_response(
            data=[card_item.get_card_details() for card_item in all_card_instance],
            code=200,
        )


class UpdateCardView(APIView):
    @staticmethod
    def put(request, card_id):
        current_time = timezone.now()

        all_card_instance = todo_models.CardItem.objects.filter(is_active=True)

        card_instance = todo_models.CardItem.objects.filter(id=card_id).last()

        if not card_instance:
            return todo_utils.create_response("Not Found", 400)

        serializer_instance = todo_serializers.CardSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return todo_utils.create_response(serializer_instance.errors, 400)

        if serializer_instance.validated_data.get("card_name"):
            card_instance.card_name = serializer_instance.validated_data.get(
                "card_name"
            )

        card_instance.updated_date_time = current_time

        card_instance.save(update_fields=["card_name", "updated_date_time"])

        return todo_utils.create_response(
            data=[card_item.get_card_details() for card_item in all_card_instance],
            code=200,
        )


class DeleteCardView(APIView):
    @staticmethod
    def delete(request, card_id):
        current_time = timezone.now()

        all_card_instance = todo_models.CardItem.objects.filter(is_active=True)

        card_instance = todo_models.CardItem.objects.filter(id=card_id).last()

        if not card_instance:
            return todo_utils.create_response(card_instance.errors, 400)

        card_instance.is_active = False
        card_instance.updated_date_time = current_time

        card_instance.save(update_fields=["is_active", "updated_date_time"])

        return todo_utils.create_response(
            data=[card_item.get_card_details() for card_item in all_card_instance],
            code=200,
        )


# Done
class CreateTodoItemView(APIView):
    @staticmethod
    def post(request, card_id):
        card_instance = todo_models.CardItem.objects.filter(
            id=card_id, is_active=True
        ).last()

        if not card_instance:
            return todo_utils.create_response("Not Found", code=400)

        serializer_instance = todo_serializers.TaskItemSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return todo_utils.create_response(serializer_instance.errors, code=400)

        task_item_instance = todo_models.TaskItem.objects.create(
            **serializer_instance.validated_data
        )

        card_instance.task.add(task_item_instance)

        return todo_utils.create_response(
            data=card_instance.get_card_details(), code=200
        )


# Done
class DeleteTodoView(APIView):
    @staticmethod
    def delete(request, todo_id):
        current_time = timezone.now()
        todo_item_instance = todo_models.TaskItem.objects.filter(id=todo_id).last()

        if not todo_item_instance:
            return todo_utils.create_response(data="Not Found", code=400)

        todo_item_instance.is_active = False
        todo_item_instance.updated_date_time = current_time

        todo_item_instance.save(update_fields=["is_active", "updated_date_time"])

        return todo_utils.create_response(data="Ok", code=200)


# Done
class UpdateTodoView(APIView):
    @staticmethod
    def put(request, todo_id):
        current_time = timezone.now()
        todo_item_instance = todo_models.TaskItem.objects.filter(
            id=todo_id, is_active=True
        ).last()

        if not todo_item_instance:
            return todo_utils.create_response(data="Not Found", code=400)

        serializer_instance = todo_serializers.TaskItemSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return todo_utils.create_response(serializer_instance.errors, code=400)

        if serializer_instance.validated_data.get("title"):
            todo_item_instance.title = serializer_instance.validated_data.get("title")

        todo_item_instance.updated_date_time = current_time

        todo_item_instance.save(update_fields=["title", "updated_date_time"])

        return todo_utils.create_response(
            data=todo_item_instance.get_task_details(), code=200
        )


class DoneTodoView(APIView):
    @staticmethod
    def post(request, todo_id):
        current_time = timezone.now()
        todo_item_instance = todo_models.TaskItem.objects.filter(
            id=todo_id, is_active=True
        ).last()

        if not todo_item_instance:
            return todo_utils.create_response(data="Not Found", code=400)

        serializer_instance = todo_serializers.DoneTaskSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return todo_utils.create_response(serializer_instance.errors, code=400)

        todo_item_instance.is_pending = serializer_instance.validated_data.get(
            "is_pending"
        )

        todo_item_instance.updated_date_time = current_time

        todo_item_instance.save(update_fields=["is_pending", "updated_date_time"])

        return todo_utils.create_response(
            data=todo_item_instance.get_task_details(), code=200
        )
