from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TicTacToe, Cell


class PlayX(APIView):
    def post(self, request) -> Response:
        player = "X"
        x_vert = request.META.get("X-Vertical", None)
        x_horiz = request.META.get("X-Horizontal", None)
        x_game_id = request.META.get("X-Game-Id", None)

        if not x_vert or not x_horiz:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        game = get_game(x_game_id)

        winner = play(game, x_horiz, x_vert, player)
        cells = Cell.objects.get(game=game)

        if winner:
            return Response(status=status.HTTP_200_OK, data={"winner": player, "board": cells})
        return Response(status=status.HTTP_200_OK, data={"board": cells})


class Play0(APIView):
    def post(self, request) -> Response:
        player = "O"
        x_vert = request.META.get("X-Vertical", None)
        x_horiz = request.META.get("X-Horizontal", None)
        x_game_id = request.META.get("X-Game-Id", None)

        if not x_vert or not x_horiz:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        game = get_game(x_game_id)

        winner = play(game, x_horiz, x_vert, player)
        cells = Cell.objects.get(game=game)

        if winner:
            return Response(status=status.HTTP_200_OK, data={"winner": player, "board": cells})
        return Response(status=status.HTTP_200_OK, data={"board": cells})


def get_game(game_id) -> TicTacToe:
    if game_id is None:
        game = TicTacToe.objects.create()
    else:
        game = TicTacToe.objects.get(game_id=game_id)
    return game


def play(game: TicTacToe, x_horiz: int, x_vert: int, player: str) -> bool:
    cell = Cell.objects.create(x_position=x_horiz, y_position=x_vert, game=game, value=player)

    # check if winner
    return check_winner(cell, player)


def check_winner(cell, player) -> bool:
    cells = Cell.objects.filter(game=cell.game, value=player, x_position=cell.x_position)
    if cells.count() == 3:
        return True
    cells = Cell.objects.filter(game=cell.game, value=player, x_position=cell.y_position)
    if cells.count() == 3:
        return True

    cell = Cell.objects.filter(game=cell.game, value=player, x_position=1, y_position=1).first()
    if cell:
        cells = (Cell.objects.filter(game=cell.game, value=player, x_position=0, y_position=0).first() &
                 Cell.objects.filter(game=cell.game, value=player, x_position=2, y_position=2).first())
        if cells.count == 2:
            return True
        cells = (Cell.objects.filter(game=cell.game, value=player, x_position=0, y_position=2).first() &
                 Cell.objects.filter(game=cell.game, value=player, x_position=2, y_position=0).first())
        if cells.count == 2:
            return True

    return False
