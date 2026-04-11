from enum import Enum
from functools import wraps


# ----------------------------
# 1. Roles Definition
# ----------------------------
class Role(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"


# ----------------------------
# 2. User Model
# ----------------------------
class User:
    def __init__(self, user_id: int, username: str, role: Role):
        self.user_id = user_id
        self.username = username
        self.role = role

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.username}, role={self.role})"


# ----------------------------
# 3. Permission Map (Optional Extension)
# ----------------------------
ROLE_PERMISSIONS = {
    Role.ADMIN: {"create", "read", "update", "delete"},
    Role.MANAGER: {"create", "read", "update"},
    Role.USER: {"read"},
}


def has_permission(user: User, action: str) -> bool:
    return action in ROLE_PERMISSIONS.get(user.role, set())


# ----------------------------
# 4. Role-Based Access Decorator
# ----------------------------
def require_roles(*allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(user: User, *args, **kwargs):
            if user.role not in allowed_roles:
                raise PermissionError(
                    f"Access denied: {user.username} ({user.role}) "
                    f"cannot access '{func.__name__}'"
                )
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


# ----------------------------
# 5. Protected Functions (System Actions)
# ----------------------------
@require_roles(Role.ADMIN)
def delete_booking(user: User, booking_id: int):
    return f"Booking {booking_id} deleted by {user.username}"


@require_roles(Role.ADMIN, Role.MANAGER)
def update_booking(user: User, booking_id: int, status: str):
    return f"Booking {booking_id} updated to '{status}' by {user.username}"


@require_roles(Role.ADMIN, Role.MANAGER, Role.USER)
def view_booking(user: User, booking_id: int):
    return f"Booking {booking_id} viewed by {user.username}"


# ----------------------------
# 6. Demo / Test Run
# ----------------------------
if __name__ == "__main__":
    admin = User(1, "Alice", Role.ADMIN)
    manager = User(2, "Bob", Role.MANAGER)
    user = User(3, "Charlie", Role.USER)

    print("\n--- RBAC SYSTEM DEMO ---\n")

    # Admin actions
    print(delete_booking(admin, 101))
    print(update_booking(admin, 102, "confirmed"))
    print(view_booking(admin, 103))

    print("\n--- Manager Actions ---\n")

    print(update_booking(manager, 201, "pending"))
    print(view_booking(manager, 202))

    try:
        print(delete_booking(manager, 203))
    except PermissionError as e:
        print("ERROR:", e)

    print("\n--- User Actions ---\n")

    print(view_booking(user, 301))

    try:
        print(update_booking(user, 302, "failed"))
    except PermissionError as e:
        print("ERROR:", e)

    print("\n--- Permission Check Example ---\n")
    print("User can 'read'?", has_permission(user, "read"))
    print("User can 'delete'?", has_permission(user, "delete"))