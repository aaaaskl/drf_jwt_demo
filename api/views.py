from rest_framework.views import APIView
from rest_framework.response import Response

from utils.jwt_auth import create_token
from extensions.auth import JwtQueryParamAuthentication, JwtAuthorizationAuthentication


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        """ 用户登录 """
        user = request.data.get('username')
        pwd = request.data.get('password')
        # 检测用户和密码是否正确，此处可以在数据进行校验。
        if user == 'wupeiqi' and pwd == '123':
            # 用户名和密码正确，给用户生成token并返回
            token = create_token({'username': 'wupeiqi'})
            return Response({'status': True, 'token': token})
        return Response({'status': False, 'error': '用户名或密码错误'})


class OrderView(APIView):
    # 通过url传递token
    # authentication_classes = [JwtQueryParamAuthentication, ]

    # 通过Authorization请求头传递token
    authentication_classes = [JwtAuthorizationAuthentication, ]

    def get(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '订单列表'})

    def post(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '添加订单'})

    def put(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '修改订单'})

    def delete(self, request, *args, **kwargs):
        print(request.user, request.auth)
        return Response({'data': '删除订单'})
