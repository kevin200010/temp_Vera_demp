from cobaltspeech.transcribe.v5 import transcribe_pb2 as _transcribe_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VersionResponse(_message.Message):
    __slots__ = ("server",)
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: str
    def __init__(self, server: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ...) -> None: ...

class StreamingRecognizeRequest(_message.Message):
    __slots__ = ("config", "audio")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    config: Config
    audio: _transcribe_pb2.RecognitionAudio
    def __init__(self, config: _Optional[_Union[Config, _Mapping]] = ..., audio: _Optional[_Union[_transcribe_pb2.RecognitionAudio, _Mapping]] = ...) -> None: ...

class StreamingRecognizeResponse(_message.Message):
    __slots__ = ("transcribe", "sentimo", "error")
    TRANSCRIBE_FIELD_NUMBER: _ClassVar[int]
    SENTIMO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    transcribe: _transcribe_pb2.StreamingRecognizeResponse
    sentimo: SentimoResponse
    error: _transcribe_pb2.RecognitionError
    def __init__(self, transcribe: _Optional[_Union[_transcribe_pb2.StreamingRecognizeResponse, _Mapping]] = ..., sentimo: _Optional[_Union[SentimoResponse, _Mapping]] = ..., error: _Optional[_Union[_transcribe_pb2.RecognitionError, _Mapping]] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ("model_id", "recognition_config")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    RECOGNITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    recognition_config: _transcribe_pb2.RecognitionConfig
    def __init__(self, model_id: _Optional[str] = ..., recognition_config: _Optional[_Union[_transcribe_pb2.RecognitionConfig, _Mapping]] = ...) -> None: ...

class Model(_message.Message):
    __slots__ = ("id", "name", "attributes")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    attributes: ModelAttributes
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., attributes: _Optional[_Union[ModelAttributes, _Mapping]] = ...) -> None: ...

class ModelAttributes(_message.Message):
    __slots__ = ("class_labels", "available_transcribe_model_ids")
    CLASS_LABELS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_TRANSCRIBE_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    class_labels: _containers.RepeatedScalarFieldContainer[str]
    available_transcribe_model_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, class_labels: _Optional[_Iterable[str]] = ..., available_transcribe_model_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class SentimoResponse(_message.Message):
    __slots__ = ("predictions", "start_time_ms", "duration_ms")
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    predictions: _containers.RepeatedCompositeFieldContainer[Prediction]
    start_time_ms: int
    duration_ms: int
    def __init__(self, predictions: _Optional[_Iterable[_Union[Prediction, _Mapping]]] = ..., start_time_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class Prediction(_message.Message):
    __slots__ = ("label", "probability")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    label: str
    probability: float
    def __init__(self, label: _Optional[str] = ..., probability: _Optional[float] = ...) -> None: ...
