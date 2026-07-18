from dataclasses import dataclass, field

from memory.user_profile import UserProfile


@dataclass
class Memory:

    profile: UserProfile = field(default_factory=UserProfile)

    preference: dict = field(default_factory=dict)

    summary: str = ""

    long_memory: list = field(default_factory=list)