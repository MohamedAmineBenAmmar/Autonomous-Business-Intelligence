import uvicorn
from fastapi import FastAPI
from database_expert_system import DatabaseExpertSystem, db_facts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/suggest_databases")
def read_item(constraints: dict):
    # Create an instance of the ExpertSystem class
    db_expert_sys = DatabaseExpertSystem()

    # Reset the system to clear any previous state
    db_expert_sys.reset()

    # Gather data from the user questions
    for constraint in constraints:
        if constraints[constraint]:
            db_expert_sys.declare(db_facts[constraint]())

    # Run the expert system and make a recommendation
    db_expert_sys.run()

    print(db_expert_sys.suggestions)
        
    return db_expert_sys.suggestions

# Configuring CORSMiddleware
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")