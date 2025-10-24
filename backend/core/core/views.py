from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """
    View to check the health status of the application.
    """

    def get(self, request):
        """
        Return a simple health status message.
        """
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
