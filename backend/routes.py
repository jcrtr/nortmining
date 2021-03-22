import aiohttp_cors

from backend.graph.views import gql_view
from backend.views import coin_add, deposit


def init_routes(app, cors):
    app.router.add_get('/coin', deposit, name='coin'),
    app.router.add_get('/add', coin_add, name='coin_add'),

    # app.router.add_route('*', '/graphiql', gqil_view, name='graphiql')

    resource = cors.add(app.router.add_resource("/graphql"), {
        "*": aiohttp_cors.ResourceOptions(
            expose_headers="*",
            allow_headers="*",
            allow_credentials=True,
            allow_methods=["POST", "PUT", "GET"]),
    })
    resource.add_route("POST", gql_view)
    resource.add_route("PUT", gql_view)
    resource.add_route("GET", gql_view)
