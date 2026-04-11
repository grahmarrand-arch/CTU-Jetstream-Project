import time
from typing import Any, Dict, Tuple, Optional

class SearchCache:
    def __init__(self, ttl_seconds: int = 300):
        self.ttl = ttl_seconds
        self.cache: Dict[str, Tuple[Any, float]] = {}

    def get(self, key: str) -> Optional[Any]:
        """Retrieve cached result if not expired."""
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
                return value
            else:
                # expired → remove it
                del self.cache[key]
        return None

    def set(self, key: str, value: Any):
        """Store result with expiration time."""
        expiry = time.time() + self.ttl
        self.cache[key] = (value, expiry)

    def clear(self):
        """Clear all cached data."""
        self.cache.clear()


# ---------------------------
# Example search function
# ---------------------------

cache = SearchCache(ttl_seconds=120)

def search(query: str):
    # 1. check cache first
    cached_result = cache.get(query)
    if cached_result is not None:
        print("CACHE HIT")
        return cached_result

    # 2. simulate expensive search operation
    print("CACHE MISS - fetching results")
    result = expensive_search(query)

    # 3. store in cache
    cache.set(query, result)
    return result


def expensive_search(query: str):
    # Simulate API/db call
    time.sleep(2)
    return {
        "query": query,
        "results": [f"Result for {query} 1", f"Result for {query} 2"]
    }


# ---------------------------
# Demo
# ---------------------------
if __name__ == "__main__":
    print(search("flights to NYC"))
    print(search("flights to NYC"))  # cached