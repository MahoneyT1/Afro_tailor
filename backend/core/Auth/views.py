from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to obtain JWT tokens.
    This can be extended to include additional user information in the token.
    """
    # You can override methods here if you need to customize the token payload
    # For example, to add user roles or other custom claims
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to obtain JWT tokens.
        """
        response =  super().post(request, *args, **kwargs)

        if response.status_code == 200:
           data = response.data

           access = data.get('access')
           refresh = data.get('refresh')
           
           if access:
            response.set_cookie(
                'access': access,
                httponly=True,
                secure=False,
                samesite='Lax',
            )
                
            if refresh:
                response.set_cookie(
                    'refresh': refresh,
                    httponly=True,
                    secure=False,
                    samesite='Lax',
                )
            return response
        return Response(
            {"detail": "Invalid credentials."},
            status=status.HTTP_401_UNAUTHORIZED
        )

            
               

