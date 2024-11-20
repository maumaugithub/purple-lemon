@dataclass
class MyGrafanaLog(SerializableBase):
    tracking_hash: str
    image_id: str
    error_details: str
    error_status: bool
    process_tag: str
    user_id: int