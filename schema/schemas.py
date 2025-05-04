def individual_serial(user) -> dict:
    return{
        "id": str(user["_id"]),
        "name": user["name"],
        "password": user["password"],
        "email": user["email"],
        "phoneNo": user["phoneNo"],
        "address": user["address"]
    }

def list_serial(users) -> dict:
    return [individual_serial(user) for user in users]