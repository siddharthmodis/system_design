import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()  # Lock to ensure thread-safety during instantiation

    def __new__(cls, *args, **kwargs):
        # Ensure that only one thread can create the instance
        with cls._lock:
            if not cls._instance:
                # If no instance exists, create it
                cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        # Initialize only if the instance is not initialized yet
        if not hasattr(self, '_initialized'):
            self.value = value
            self._initialized = True  # Mark as initialized

# Testing Singleton in a multi-threaded environment
def test_singleton(thread_id):
    singleton = Singleton("Singleton Instance in Thread {}".format(thread_id))
    print(f"Thread {thread_id}: {singleton.value}")

# Create multiple threads
threads = []
for i in range(5):  # Let's create 5 threads to test the Singleton
    thread = threading.Thread(target=test_singleton, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
