from fastapi import Request
from logger import logger
import time

async def log_middleware(request: Request, call_next):
    start = time.time()
    
    response = await call_next(request)
    process_time = time.time() - start
    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'process_time': process_time,
        'status_code': response.status_code,
    }
    logger.info(log_dict)
    
    return response