class InMemoryEntityMeta(type):
    """Metaclass for in memory entities"""

    def __new__(mcs, name, bases, attrs):
        if name != "InMemoryEntity":
            if "Config" not in attrs.keys():
                raise NotImplementedError("Config must be implemented")
            if not hasattr(attrs["Config"], "storage_name"):
                raise NotImplementedError("storage_name must be defined")
        return super().__new__(mcs, name, bases, attrs)


class InMemoryEntity(metaclass=InMemoryEntityMeta):
    pass
