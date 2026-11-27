import inspect

def function_to_input_schema(func) -> dict:
    type_map = {
        str: "string",
        int: "integer",
        float: "number",
        bool: "boolean",
        list: "array",
        dict: "object",
        type(None): "null",
    }

    try:
        signature = inspect.signature(func)
    except ValueError as e:
        raise ValueError(f"Failed to get signature for function: {func.__name__}: {str(e)}")

    parameters = {}
    for param in signature.parameters.values():
        if param.name == "context":
            continue  # change from chapter 3 code to skip a parameter called 'context'
        param_type = type_map.get(param.annotation, "string") #unknown types fall back to "string" (e.g. list[str] -> wrong!) 
        parameters[param.name] = {"type": param_type}

    required = [param.name for param in signature.parameters.values() if param.default == inspect._empty and param.name != "context"]  # change from chapter 3 code to skip a parameter called 'context'
    return {"type": "object", "properties": parameters, "required": required}

def format_tool_definition(name: str, description:str, parameters:dict) -> dict:
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": parameters,
        },
    }

def function_to_tool_definition(func) -> dict:
    return format_tool_definition(
        func.__name__,
        func.__doc__ or "",
        function_to_input_schema(func)
    )