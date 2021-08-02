import aiohttp_cors

from backend.api.auth.views import login, sing_out


def init_routes(app):
    r = app.router
    # r.add_route("GET", '/update', get_update)
    #
    r.add_route("POST", '/api/auth/login', login)
    r.add_route("GET", '/api/auth/logout', sing_out)
    #
    # r.add_route("POST", "/graphql",  gql_view)
    # r.add_route("PUT", "/graphql", gql_view)
    # r.add_route("GET", "/graphql", gql_view)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    for route in list(r.routes()):
        cors.add(route)
