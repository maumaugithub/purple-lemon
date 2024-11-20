import time

@dataclass
class InkPicture(SerializableBase):
    source_resolution: str
    resize_resolution: str
    resize_file:str
    resize_path:str
    source_date: str
    source_file:str
    source_path: str
    source_file_hash: str = None
    resize_file_hash: str = None
    category: str
    is_display_ready: bool
    is_backed_up: bool
    year: str

    def __hash__(self):
        return hash((self.source_resolution,
                     self.resize_resolution,
                     self.category,
                     self.year,
                     self.source_date,
                     self.source_file_hash,
                     self.resize_file_hash
                     ))