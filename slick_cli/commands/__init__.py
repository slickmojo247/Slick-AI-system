# commands subpackage init
from .check_syntax import check_syntax
from .inspect_logic import inspect_logic
from .train_memory import train_memory
from .apply_cohesion import apply_cohesion
from .session_log import session_log

all_commands = [
    check_syntax,
    inspect_logic,
    train_memory,
    apply_cohesion,
    session_log,
]
