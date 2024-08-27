from fastapi import FastAPI
import logging

app = FastAPI()

# Configurar logging
logging.basicConfig(filename='log/log1.log',level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("service1")

@app.get("/")
def read_root():
    logger.info("Request received in service 1")
    return {"message": "Hello from Service 1"}
