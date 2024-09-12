from graphene import ObjectType, String, Schema, Int, List
from neo4j import GraphDatabase
from flask_graphql import GraphQLView

from flask import Flask



# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "")

# with GraphDatabase.driver(URI, auth=AUTH) as driver:
#     driver.verify_connectivity()
#     print("Connection established.")


class Player(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `first_name`
    # By default, the argument name will automatically be camel-based into firstName in the generated schema
    name = String(first_name=String(default_value="stranger"))
    role = String()
    age = Int()
    
class Team(ObjectType):
    name = String()
    country = String()
    
class Query(ObjectType):
    players = List(Player)
    teams = List(Team)
    

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (first_name) for the Field and returns data for the query Response
    def resolve_players(root, info):
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            driver.verify_connectivity()
            print("Connection established.")
            records, summary, keys = driver.execute_query(
            "MATCH (p:Player) RETURN p.name AS name, p.role as role, p.age as age",

            database_="neo4j",
            )
            return [Player(name=record["name"], role=record["role"], age=record["age"]) for record in records]
        
    def resolve_teams(root, info):
        with GraphDatabase.driver(URI, auth=AUTH) as driver:
            driver.verify_connectivity()
            print("Connection established.")
            records, summary, keys = driver.execute_query(
            "MATCH (p:Team ) RETURN p.name AS name, p.country as country",
            database_="neo4j",
            )
            return [Team(name=record["name"], country=record["country"]) for record in records]
        

schema = Schema(query=Query)




# query_string = '{players {name role age}}'
# result = schema.execute(query_string)


# @app.route('/')
# def root_route():
#     return {"data": result.data}


app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)



if __name__ == '__main__':
    app.run(debug=True)


