# This is the database expert system (DBES) module.
imports = """
from experta import Fact, Rule, KnowledgeEngine, AND, OR, DefFacts
"""

db_fact = """
class Database(Fact):
    # Info about the database.
    pass
"""

rules = """
class DatabaseSuggestion(KnowledgeEngine):

    # @DefFacts()
    # def _initial_facts(self):
    #     yield Database(name="MySQL", type="relational", scale="large", consistency="high", license="open-source")
    #     yield Database(name="PostgreSQL", type="relational", scale="medium", consistency="high", license="open-source")
    #     yield Database(name="SQLite", type="relational", scale="small", consistency="high", license="public-domain")
    #     yield Database(name="Oracle Database", type="relational", scale="large", consistency="high", license="proprietary")
    #     yield Database(name="Microsoft SQL Server", type="relational", scale="large", consistency="high", license="proprietary")
    #     yield Database(name="MariaDB", type="relational", scale="medium", consistency="high", license="open-source")
    #     yield Database(name="MongoDB", type="document-oriented", scale="large", consistency="eventual", license="server-side-public-license")
    #     yield Database(name="Firebase", type="document-oriented", scale="medium", consistency="eventual", license="proprietary")
    #     yield Database(name="Elasticsearch", type="search-engine", scale="large", consistency="high", license="open-source")
    #     yield Database(name="Redis", type="key-value", scale="large", consistency="high", license="open-source")
    #     yield Database(name="Couchbase", type="document-oriented", scale="large", consistency="high", license="open-source")
    #     yield Database(name="Cassandra", type="wide-column", scale="large", consistency="eventual", license="open-source")
    #     yield Database(name="Neo4j", type="graph", scale="medium", consistency="high", license="open-source")
    #     yield Database(name="HBase", type="wide-column", scale="large", consistency="high", license="open-source")
    #     yield Database(name="InfluxDB", type="time-series", scale="medium", consistency="high", license="open-source")
    #     yield Database(name="RavenDB", type="document-oriented", scale="medium", consistency="high", license="proprietary")
    #     yield Database(name="CouchDB", type="document-oriented", scale="small", consistency="eventual", license="open-source")
    #     yield Database(name="RethinkDB", type="document-oriented", scale="medium", consistency="eventual", license="open-source")
    #     yield Database(name="Memcached", type="key-value", scale="medium", consistency="high", license="open-source")
    #     yield Database(name="ArangoDB", type="multi-model", scale="medium", consistency="high", license="open-source")
    
    @Rule(AND(Database(type="relational"), Database(scale="large"), Database(consistency="high"), Database(license="open-source")))
    def suggest_mysql(self):
        print("We suggest using MySQL for your project.")

    @Rule(AND(Database(type="relational"), Database(scale="medium"), Database(consistency="high"), Database(license="open-source")))
    def suggest_postgresql(self):
        print("We suggest using PostgreSQL for your project.")

    @Rule(AND(Database(type="relational"), Database(scale="small"), Database(consistency="high"), Database(license="public-domain")))
    def suggest_sqlite(self):
        print("We suggest using SQLite for your project.")

    @Rule(AND(Database(type="relational"), Database(scale="large"), Database(consistency="high"), Database(license="proprietary")))
    def suggest_oracle(self):
        print("We suggest using Oracle Database for your project.")

    @Rule(AND(Database(type="relational"), Database(scale="large"), Database(consistency="high"), Database(license="proprietary")))
    def suggest_sql_server(self):
        print("We suggest using Microsoft SQL Server for your project.")

    @Rule(AND(Database(type="relational"), Database(scale="medium"), Database(consistency="high"), Database(license="open-source")))
    def suggest_mariadb(self):
        print("We suggest using MariaDB for your project.")

    @Rule(AND(Database(type="document-oriented"), Database(scale="large"), Database(consistency="eventual"), Database(license="server-side-public-license")))
    def suggest_mongodb(self):
        print("We suggest using MongoDB for your project.")

    @Rule(AND(Database(type="document-oriented"), Database(scale="medium"), Database(consistency="eventual"), Database(license="proprietary")))
    def suggest_firebase(self):
        print("We suggest using Firebase for your project.")
        
    @Rule(AND(Database(type="search-engine"), Database(scale="large"), Database(consistency="high"), Database(license="open-source")))
    def suggest_elasticsearch(self):
        print("We suggest using Elasticsearch for your project.")

    @Rule(AND(Database(type="key-value"), Database(scale="large"), Database(consistency="high"), Database(license="open-source")))
    def suggest_redis(self):
        print("We suggest using Redis for your project.")

    @Rule(AND(Database(type="document-oriented"), Database(scale="large"), Database(consistency="high"), Database(license="open-source")))
    def suggest_couchbase(self):
        print("We suggest using Couchbase for your project.")

    @Rule(AND(Database(type="wide-column"), Database(scale="large"), Database(consistency="eventual"), Database(license="open-source")))
    def suggest_cassandra(self):
        print("We suggest using Cassandra for your project.")

    @Rule(AND(Database(type="graph"), Database(scale="medium"), Database(consistency="high"), Database(license="open-source")))
    def suggest_neo4j(self):
        print("We suggest using Neo4j for your project.")

    @Rule(AND(Database(type="wide-column"), Database(scale="large"), Database(consistency="high"), Database(license="open-source")))
    def suggest_hbase(self):
        print("We suggest using HBase for your project.")

    @Rule(AND(Database(type="time-series"), Database(scale="medium"), Database(consistency="high"), Database(license="open-source")))
    def suggest_influxdb(self):
        print("We suggest using InfluxDB for your project.")

    @Rule(AND(Database(type="document-oriented"), Database(scale="medium"), Database(consistency="high"), Database(license="proprietary")))
    def suggest_ravendb(self):
        print("We suggest using RavenDB for your project.")

    @Rule(AND(Database(type="document-oriented"), Database(scale="small"), Database(consistency="eventual"), Database(license="open-source")))
    def suggest_couchdb(self):
        print("We suggest using CouchDB for your project.")

    @Rule(AND(Database(type="document-oriented"), Database(scale="medium"), Database(consistency="eventual"), Database(license="open-source")))
    def suggest_rethinkdb(self):
        print("We suggest using RethinkDB for your project.")

    @Rule(AND(Database(type="key-value"), Database(scale="medium"), Database(consistency="high"), Database(license="open-source")))
    def suggest_memcached(self):
        print("We suggest using Memcached for your project.")

    @Rule(AND(Database(type="multi-model"), Database(scale="medium"), Database(consistency="high"), Database(license="open-source")))
    def suggest_arangodb(self):
        print("We suggest using ArangoDB for your project.")
"""

engine = """
engine = DatabaseSuggestion()
engine.reset()
engine.declare(Database(type="relational", scale="medium", consistency="high", license="open-source"))
engine.run()

"""

if __name__ == "__main__":
    compiled_imports = compile(imports, '<string>', 'exec')
    compiled_db_fact = compile(db_fact, '<string>', 'exec')
    compiled_rules = compile(rules, '<string>', 'exec')
    compiled_engine = compile(engine, '<string>', 'exec')

    print("\nadded the compile + exec tests: \n")
    
    exec(compiled_imports)
    exec(compiled_db_fact)
    exec(compiled_rules)
    exec(compiled_engine)