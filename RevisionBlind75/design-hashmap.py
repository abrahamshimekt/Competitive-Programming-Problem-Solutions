class MyHashMap:

    def __init__(self):
        self.size = 10**6 
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        bucket = self.buckets[hash_key]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        bucket = self.buckets[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        bucket = self.buckets[hash_key]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


