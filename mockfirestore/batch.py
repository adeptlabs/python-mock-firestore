import warnings
from typing import Any, List, Optional, Iterable, Dict, Tuple, Sequence

from mockfirestore import AlreadyExists
from mockfirestore._helpers import generate_random_string, Store, get_by_path, set_by_path, Timestamp
from mockfirestore.query import Query
from mockfirestore.document import DocumentReference, DocumentSnapshot
from mockfirestore.collection import CollectionReference
from mockfirestore._helpers import Store

class BatchReference:
    def __init__(self, data: Store) -> None:
        self._data = data
        self._operations : List[DocumentReference] = []
    
    def set(self, reference: DocumentReference, data: Dict):
        self._operations.append((reference, data))

    def commit(self) -> None:
        for reference, data in self._operations:
            reference.set(data)