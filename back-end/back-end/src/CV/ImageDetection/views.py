from django.contrib.auth.models import User, Group
from .models import ImageDetection
from rest_framework import viewsets
from rest_framework import permissions
from ImageDetection.serializers import UserSerializer, GroupSerializer, ImageDetectionSerializer
import torch
from rest_framework.decorators import action
from rest_framework.decorators import action

# Create your views here.
import os
from django.http import JsonResponse
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
    model.load_state_dict(model_state_dict)
    model.eval()

    @action(methods=["GET", "POST"], url_path='evaluate', detail=False)
    def evaluate(self, request, model=model):
        image = request.POST.get("image", "../../../../static/imagem.png" )
        image = request.GET.get("image", "../../../../static/imagem.png" )
        # image = request.GET.get("")
        model_evaluation = model(image)
        model_evaluation_dict = model_evaluation.pandas().xyxy[0].to_dict(orient="records")
        return JsonResponse(model_evaluation_dict, safe=False)

