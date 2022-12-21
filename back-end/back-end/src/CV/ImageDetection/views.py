from django.contrib.auth.models import User, Group
from .models import ImageDetection
from rest_framework import viewsets
from rest_framework import permissions
from ImageDetection.serializers import UserSerializer, GroupSerializer, ImageDetectionSerializer
import torch
from rest_framework.decorators import action
    # queryset = Group.objects.all().order_by()
from rest_framework.decorators import action
# Create your views here.
import os

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ImageDetectionViewSet(viewsets.ModelViewSet):
    queryset = ImageDetection.objects.all()
    serializer_class = ImageDetectionSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    model_state_dict = torch.load('../../../../resources/PS_TAIL.pt')
    model = torch.hub.load('../../../../yolov5', 'custom', path='../../../../resources/best.pt', source='local')
    model_loaded = model.load_state_dict(model_state_dict)
    folder_path = os.path.join("")

    @action(method=["POST"], url_path='evaluate', detail=False)
    def evaluate(self, request, model=model_loaded):
        image = request.query_params["image"]
        model_evaluation = model(image)
        model_evaluation_dict = model_evaluation.pandas().xyxy[0].to_dict(orient="records")
        return model_evaluation_dict 