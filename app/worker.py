# app/worker.py
from concurrent.futures import ThreadPoolExecutor

# Singleton thread pool – rulează în fundal
executor = ThreadPoolExecutor(max_workers=4)

def run_async(func, *args, **kwargs):
    """Trimite funcția la executare în thread separat și returnează rezultatul (blocant)."""
    future = executor.submit(func, *args, **kwargs)
    return future.result()
