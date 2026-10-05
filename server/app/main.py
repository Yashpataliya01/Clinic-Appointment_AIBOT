from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routes.ai_help import router as ai_router
from app.routes.clinic import router as clinic_router


app = FastAPI(
    title="PulseClinic Healthcare Management & LangChain AI API",
    description="Enterprise Clinic Management Backend powered by FastAPI, MongoDB Atlas & LangChain",
    version="1.0.0"
)

# Enable CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ai_router)
app.include_router(clinic_router)


@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "PulseClinic Healthcare Management System",
        "ai_engine": "LangChain + Google Gemini",
        "mode": "In-Memory Full Dummy Database"
    }

