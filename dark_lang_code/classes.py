class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name


class IntVariable(Variable):
    def __init__(self, name, value):
        super().__init__(name, int(value))

class StrVariable(Variable):
    def __init__(self, name, value):
        super().__init__(name, str(value))

class ListVariable(Variable):
    def __init__(self, name, value):
        super().__init__(name, list(value))

class DictVariable(Variable):
    def __init__(self, name, value):
        super().__init__(name, dict(value))

class VariableStore:
    def __init__(self):
        self.variables = {}

    def add_variable(self, variable):
        self.variables[variable.name] = variable

    def get_variable(self, name):
        return self.variables.get(name)

    def delete_variable(self, name):
        if name in self.variables:
            del self.variables[name]
            return True
        return False

class BlockStore:
    def __init__(self):
        self.blocks = {}

    def add_block(self, name_block, command_block):
        self.blocks[name_block] = command_block

    def get_block(self, name_block):
        return self.blocks.get(name_block)

    def delete_block(self, name_block):
        if name_block in self.blocks:
            del self.blocks[name_block]
            return True
        return False


_mods = {}

def add_mod(mod_name, mod):
    global _mods
    _mods[mod_name] = mod

def get_mod(mod_name):
    global _mods
    return _mods.get(mod_name, None)

class VariableError(Exception):
    pass

class BlockError(Exception):
    pass

class CommandError(Exception):
    pass