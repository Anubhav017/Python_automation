from uuid import uuid4


def build_customer() -> dict[str, str]:
    # unique login and email per run, so re-runs and parallel runs never clash
    suffix = uuid4().hex[:8]
    return {
        "first_name": "Anubhav",
        "last_name": f"Test{suffix}",
        "email": f"anubhav_{suffix}@example.com",
        "address": "1 MG Road",
        "city": "Bangalore",
        "country": "India",
        "zone": "Karnataka",
        "postcode": "560001",
        "login_name": f"anu{suffix}",
        "password": f"Pass{suffix}!",
    }
