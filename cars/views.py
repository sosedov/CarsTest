from rest_framework.response import Response
from rest_framework.views  import APIView
from .models import CarsLabel
from .serializers import CarsLabelSerializer

class CarsView (APIView):
    def get(self, request, *args, **kwargs):
        labels = CarsLabel.objects.all()
        serializer = CarsLabelSerializer(labels, many=True)
        return Response(serializer.data)

    def post(self, request):
        label = request.data.get("label")        
        serializer = CarsLabelSerializer(data=label)
        if serializer.is_valid(raise_exeption=True):
            label_saved = serializer.save()
        return Response({"success": "Label '{}' created successfully".format(label_saved.name)})
    
    def put(self,request,pk):
        saved_label = get_object_or_404(CarsLabel.objects.all(), pk=pk)
        data = request.data.get("label") 
        serializer = CarsLabelSerializer (isinstance=saved_label,data=data, partial=True)

        if serializer.is_valid (aise_exeption=True):
            label_saved = serializer.save()
        
        return Response ({"success": "Article '{}' updated successfully".format(label_saved.title)})
    
    def delete(self, request, pk):    
        label = get_object_or_404(CarsLabel.objects.all(), pk=pk)
        label.delete()
        return Response({"message": "Label with id `{}` has been deleted.".format(pk)}, status=204)






       

