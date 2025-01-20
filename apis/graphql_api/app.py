from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(description="A simple GraphQL API")
    def resolve_hello(root, info):
        return "Hello World from GraphQL API!"

schema = Schema(query=Query)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
