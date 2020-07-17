from functools import wraps


def print_message(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        RED = "\033[1;31m"
        GREEN = "\033[0;32m"
        CLOSE_TAG = "\033[0;0m"

        try:
            result = func(*args, **kwargs)
            message = (
                f"{GREEN}PASSED{CLOSE_TAG}" if result else f"{RED}FAILED{CLOSE_TAG}"
            )
        except Exception as err:
            message = f"\t{RED}Error!{CLOSE_TAG} - "
            message += f"{type(err)} - {str(err)}"

        print(f"\t {func.__name__}: {message}")

    return decorated_view
