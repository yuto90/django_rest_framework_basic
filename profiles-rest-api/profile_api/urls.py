from django.urls import path

from profile_api import views

"""
as_view()でDjangoのビューの条件を満たす関数を作り出している
Class-based viewsをFunction-based viewsと同じ働きをするようよしなにやってくれている
・requestオブジェクトを(第一引数として)受け取る
・callableである
・responseオブジェクトを返す
"""

urlpatterns = [
    # ? urlが叩かれた時にas_view()が自動でmethodを判別してくれて、それに対応したクラスメソッドを実行してくれる
    # ? example: GETメソッドで叩かれたらHelloAPIViewクラスのget()メソッドを自動で実行してくれる
    path('hello-view', views.HelloAPIView.as_view()),
]
