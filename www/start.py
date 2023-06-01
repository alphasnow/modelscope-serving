import uvicorn

# python -O start.py
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host="0.0.0.0", port=8800, log_level="info",
    )