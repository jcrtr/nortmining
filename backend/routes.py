import aiohttp_cors

from backend.graph.views import gql_view
from backend.views import login, sing_out, get_update


def init_routes(app, cors):
    app.router.add_route("GET", '/update', get_update)

    app.router.add_route("POST", '/api/auth/login', login)
    app.router.add_route("GET", '/api/auth/logout', sing_out)

    app.router.add_route("POST", "/graphql",  gql_view)
    app.router.add_route("PUT", "/graphql", gql_view)
    app.router.add_route("GET", "/graphql", gql_view)

    for route in list(app.router.routes()):
        cors.add(route)
