import warnings
from typing import Any, List, Optional, Iterable, Dict, Tuple, Sequence

from mockfirestore import AlreadyExists
from mockfirestore._helpers import generate_random_string, Store, get_by_path, set_by_path, Timestamp
from mockfirestore.query import Query
from mockfirestore.document import DocumentReference, DocumentSnapshot
from mockfirestore.collection import CollectionReference

class BatchReference:
    def __init__(self) -> None:
        self._data : List[DocumentReference] = []
    
    def set(self, reference: DocumentReference, data: Dict):
        self._data.append((reference, data))

    def commit(self) -> None:
        for reference, data in self._data:
            reference.update(data)