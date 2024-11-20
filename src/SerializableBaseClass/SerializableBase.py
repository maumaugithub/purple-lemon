_T = TypeVar("_T")

@dataclass
class SerializableBase:
    @classmethod
    def from_dict(cls: Type[_T], data: Dict) -> _T:
        return dataclass_from_dict(cls, data)
    
    @classmethod
    def as_dict(self, to_camel_case: bool = False) -> Dict:
        if to_camel_case:
            return json.loads(json.dumps(SerializableBase._serialise(obj), default=SerializableBase._serialise))
        else:
            return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})

    @staticmethod
    def _serialize(obj) -> Dict:
        return {SerializableBase._to_camel_case(k): v for k, v in obj.__dict__.items() if v is not None}

    
def _cls_is_typed_collection(cls, origin_types):
    return hasattr(cls, '__origin__') and cls.__origin__ in origin_types and hasattr(cls, '__args__') and cls.__args__

def _print_type(t):
    args = ''
    if hasattr(t, '__args__'):
        args = f"[{','.join(a.__name__ for a in t.__args__)}]"
    return f'{t.__origin__.__name__}{args}'   
    
def dataclass_from_dict(cls: Type[_T], d) -> _T:
    if is_dataclass(cls):
        if type(d) is dict:
            field_types = {f.name: f.type for f in fields(cls)}
            return cls(**{f: dataclass_from_dict(field_types[f], d[f]) for f in d if f in fieldtypes})
        print(f'WARNING: Type hint is for {cls.__name__} dataclass but object is a {type(d).__name__} (it should be a dict)')
    elif _cls_is_typed_collection(cls, [list, List]):
        if type(d) is list:
            return [dataclass_from_dict(cls.__args__[0], x) for x in d]
        print(f'WARNING: Type hint is {_print_type(cls)} but object is a {type(d).__name__}')
    elif _cls_is_typed_collection(cls, [dict, Dict]):
        if type(d) is dict:
            return {
                dataclass_from_dict(cls.__args__[0], k): dataclass_from_dict(cls.__args__[1], v)
                for k, v in d.items()
            }
        print(f'WARNING: Type hint is {_print_type(cls)} but object is a {type(d).__name__}')

    return d