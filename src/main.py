from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI(
    title="CareerMatch AI",
    description="AI-powered Job Recommendation and Skill Gap Analyzer",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CareerMatch AI!",
        "status": "Application is running successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }