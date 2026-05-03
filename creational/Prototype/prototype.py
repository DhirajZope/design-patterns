import copy


class IPrototype:
    def clone(self):
        return copy.deepcopy(self)


class APIRequest(IPrototype):
    def __init__(self, url, headers, payload, retry_policy, timeout) -> None:
        self.url = url
        self.headers = headers
        self.payload = payload
        self.retry_policy = retry_policy
        self.timeout = timeout

    def send(self) -> None:
        print(f"Sending request to {self.url}")
        print(f"Headers: {self.headers}")
        print(f"Payload: {self.payload}")


# Driver Code
base_request = APIRequest(
    url="https://api.example.com",
    headers={"Authorization": "Bearer TOKEN", "Content-Type": "application/json"},
    payload={},
    retry_policy={"retries": 3, "backoff": "exponential"},
    timeout=5,
)

user_request = base_request.clone()
user_request.url = "https://api.example.com/users"
user_request.payload = {"user_id": 123}

user_request.send()
