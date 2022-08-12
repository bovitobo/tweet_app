# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.db.models import Q
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.response import Response
from rest_framework import permissions, decorators

from tweet_app.models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'


class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    #permission_classes = [permissions.IsAuthenticated]


    @decorators.permission_classes(permissions.AllowAny)
    def create(self, request, *args, **kwargs):
        if 'action' in request.data:
            action = request.data.get('action')
            if 'username' in request.data:
                username = request.data.get('username')
            if 'password' in request.data:
                password = request.data.get('password')
            if 'email' in request.data:
                email = request.data.get('email')

            if not UserAccount.objects.filter(username=username, email=email).exists():
                UserAccount.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                if user and user.is_active:
                    login(request, user)
                    return redirect('index.html')
            else:
                return Response({"success": False, "errors": 'User already exists'}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": 'action argument is required'}, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        try:
            if 'action' in request.query_params:
                action = request.query_params.get('action')
                if action == 'register':
                    return render(request, 'registration.html')

            start = int(request.query_params.get('start'))
            limit = int(request.query_params.get('limit'))
            sort_attrib = request.query_params.get('sort')
            sort = []
            if sort_attrib:
                sort_attrib = json.loads(sort_attrib)
                for s in sort_attrib:
                    if s['property'] is None:
                        continue
                    if s['direction'] == 'DESC':
                        s['property'] = '-' + s['property']
                    sort.append(s['property'])

            # logger.info('sort: ' + str(sort))

            sq = Q()

            query = self.request.query_params.get('query')
            # logger.info('query: ' + str(query))

            if query:
                query = query.strip()

                sq = Q(name__icontains=query) | Q(synonyms__icontains=query)

            queryset = Brand.objects.filter(sq).extra(order_by=sort)[start:start + limit]
            serializer = self.get_serializer(queryset, many=True)
            response = {"success": True, "items": serializer.data, 'total': Brand.objects.filter(sq).count()}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            raise


