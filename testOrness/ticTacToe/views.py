from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from testOrness.ticTacToe.models import TicTacToe, Cell


class Play(APIView):
    def post(self, request):
        x_vert = request.META.get("X-Vertical", None)
        x_horiz = request.META.get("X-Horizontal", None)
        x_game_id = request.META.get("X-Game-Id", None)

        if not x_vert or not x_horiz:
            return Response(status_code=status.HTTP_400_BAD_REQUEST)

        game = get_game(x_game_id)
        Cell(x_position=x_horiz, y_position=x_vert, game=game , value="")

        #check if winner
        winner, player = check_winner(game, player)
        #get children Game
        return


def get_game(game_id) -> TicTacToe:
    if game_id is None:
        game = TicTacToe()
    else:
        game = TicTacToe.objects.get(game_id=game_id)
    return game


def check_winner(game, player):

    cells = Cell.objects.filter(game=game, value=player, x_position=0)
    if cells.count() == 3:
        return True, player
    cells = Cell.objects.filter(game=game, value=player, x_position=1)
    if cells.count() == 3:
        return True, player
    cells = Cell.objects.filter(game=game, value=player, x_position=2)
    if cells.count() == 3:
        return True, player


    cells = Cell.objects.filter(game=game, value=player, y_position=0)
    if cells.count() == 3:
        return True, player
    cells = Cell.objects.filter(game=game, value=player, y_position=1)
    if cells.count() == 3:
        return True, player
    cells = Cell.objects.filter(game=game, value=player, y_position=2)
    if cells.count() == 3:
        return True, player

    return False, None
