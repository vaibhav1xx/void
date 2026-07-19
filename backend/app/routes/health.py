@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": APP_NAME,
        "version": VERSION,
    }