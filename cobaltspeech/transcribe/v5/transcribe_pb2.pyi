from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ByteOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BYTE_ORDER_UNSPECIFIED: _ClassVar[ByteOrder]
    BYTE_ORDER_LITTLE_ENDIAN: _ClassVar[ByteOrder]
    BYTE_ORDER_BIG_ENDIAN: _ClassVar[ByteOrder]

class AudioEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_ENCODING_UNSPECIFIED: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_SIGNED: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_UNSIGNED: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_IEEE_FLOAT: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_ULAW: _ClassVar[AudioEncoding]
    AUDIO_ENCODING_ALAW: _ClassVar[AudioEncoding]

class AudioFormatHeadered(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIO_FORMAT_HEADERED_UNSPECIFIED: _ClassVar[AudioFormatHeadered]
    AUDIO_FORMAT_HEADERED_WAV: _ClassVar[AudioFormatHeadered]
    AUDIO_FORMAT_HEADERED_MP3: _ClassVar[AudioFormatHeadered]
    AUDIO_FORMAT_HEADERED_FLAC: _ClassVar[AudioFormatHeadered]
    AUDIO_FORMAT_HEADERED_OGG_OPUS: _ClassVar[AudioFormatHeadered]
BYTE_ORDER_UNSPECIFIED: ByteOrder
BYTE_ORDER_LITTLE_ENDIAN: ByteOrder
BYTE_ORDER_BIG_ENDIAN: ByteOrder
AUDIO_ENCODING_UNSPECIFIED: AudioEncoding
AUDIO_ENCODING_SIGNED: AudioEncoding
AUDIO_ENCODING_UNSIGNED: AudioEncoding
AUDIO_ENCODING_IEEE_FLOAT: AudioEncoding
AUDIO_ENCODING_ULAW: AudioEncoding
AUDIO_ENCODING_ALAW: AudioEncoding
AUDIO_FORMAT_HEADERED_UNSPECIFIED: AudioFormatHeadered
AUDIO_FORMAT_HEADERED_WAV: AudioFormatHeadered
AUDIO_FORMAT_HEADERED_MP3: AudioFormatHeadered
AUDIO_FORMAT_HEADERED_FLAC: AudioFormatHeadered
AUDIO_FORMAT_HEADERED_OGG_OPUS: AudioFormatHeadered

class VersionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VersionResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

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
    config: RecognitionConfig
    audio: RecognitionAudio
    def __init__(self, config: _Optional[_Union[RecognitionConfig, _Mapping]] = ..., audio: _Optional[_Union[RecognitionAudio, _Mapping]] = ...) -> None: ...

class StreamingRecognizeResponse(_message.Message):
    __slots__ = ("result", "error")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    result: RecognitionResult
    error: RecognitionError
    def __init__(self, result: _Optional[_Union[RecognitionResult, _Mapping]] = ..., error: _Optional[_Union[RecognitionError, _Mapping]] = ...) -> None: ...

class CompileContextRequest(_message.Message):
    __slots__ = ("model_id", "token", "phrases")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    token: str
    phrases: _containers.RepeatedCompositeFieldContainer[ContextPhrase]
    def __init__(self, model_id: _Optional[str] = ..., token: _Optional[str] = ..., phrases: _Optional[_Iterable[_Union[ContextPhrase, _Mapping]]] = ...) -> None: ...

class CompileContextResponse(_message.Message):
    __slots__ = ("context",)
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: CompiledContext
    def __init__(self, context: _Optional[_Union[CompiledContext, _Mapping]] = ...) -> None: ...

class RecognitionConfig(_message.Message):
    __slots__ = ("model_id", "audio_format_raw", "audio_format_headered", "selected_audio_channels", "audio_time_offset_ms", "enable_word_details", "enable_confusion_network", "metadata", "context")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FORMAT_RAW_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FORMAT_HEADERED_FIELD_NUMBER: _ClassVar[int]
    SELECTED_AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TIME_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_WORD_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CONFUSION_NETWORK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    audio_format_raw: AudioFormatRAW
    audio_format_headered: AudioFormatHeadered
    selected_audio_channels: _containers.RepeatedScalarFieldContainer[int]
    audio_time_offset_ms: int
    enable_word_details: bool
    enable_confusion_network: bool
    metadata: RecognitionMetadata
    context: RecognitionContext
    def __init__(self, model_id: _Optional[str] = ..., audio_format_raw: _Optional[_Union[AudioFormatRAW, _Mapping]] = ..., audio_format_headered: _Optional[_Union[AudioFormatHeadered, str]] = ..., selected_audio_channels: _Optional[_Iterable[int]] = ..., audio_time_offset_ms: _Optional[int] = ..., enable_word_details: bool = ..., enable_confusion_network: bool = ..., metadata: _Optional[_Union[RecognitionMetadata, _Mapping]] = ..., context: _Optional[_Union[RecognitionContext, _Mapping]] = ...) -> None: ...

class AudioFormatRAW(_message.Message):
    __slots__ = ("encoding", "bit_depth", "byte_order", "sample_rate", "channels")
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    BYTE_ORDER_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    encoding: AudioEncoding
    bit_depth: int
    byte_order: ByteOrder
    sample_rate: int
    channels: int
    def __init__(self, encoding: _Optional[_Union[AudioEncoding, str]] = ..., bit_depth: _Optional[int] = ..., byte_order: _Optional[_Union[ByteOrder, str]] = ..., sample_rate: _Optional[int] = ..., channels: _Optional[int] = ...) -> None: ...

class RecognitionMetadata(_message.Message):
    __slots__ = ("custom_metadata",)
    CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    custom_metadata: str
    def __init__(self, custom_metadata: _Optional[str] = ...) -> None: ...

class RecognitionContext(_message.Message):
    __slots__ = ("compiled",)
    COMPILED_FIELD_NUMBER: _ClassVar[int]
    compiled: _containers.RepeatedCompositeFieldContainer[CompiledContext]
    def __init__(self, compiled: _Optional[_Iterable[_Union[CompiledContext, _Mapping]]] = ...) -> None: ...

class CompiledContext(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class ContextPhrase(_message.Message):
    __slots__ = ("text", "boost")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BOOST_FIELD_NUMBER: _ClassVar[int]
    text: str
    boost: float
    def __init__(self, text: _Optional[str] = ..., boost: _Optional[float] = ...) -> None: ...

class RecognitionAudio(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

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
    __slots__ = ("sample_rate", "context_info", "supported_sample_rates")
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_INFO_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_SAMPLE_RATES_FIELD_NUMBER: _ClassVar[int]
    sample_rate: int
    context_info: ContextInfo
    supported_sample_rates: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, sample_rate: _Optional[int] = ..., context_info: _Optional[_Union[ContextInfo, _Mapping]] = ..., supported_sample_rates: _Optional[_Iterable[int]] = ...) -> None: ...

class ContextInfo(_message.Message):
    __slots__ = ("supports_context", "allowed_context_tokens")
    SUPPORTS_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONTEXT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    supports_context: bool
    allowed_context_tokens: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, supports_context: bool = ..., allowed_context_tokens: _Optional[_Iterable[str]] = ...) -> None: ...

class RecognitionResult(_message.Message):
    __slots__ = ("alternatives", "is_partial", "cnet", "audio_channel")
    ALTERNATIVES_FIELD_NUMBER: _ClassVar[int]
    IS_PARTIAL_FIELD_NUMBER: _ClassVar[int]
    CNET_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    alternatives: _containers.RepeatedCompositeFieldContainer[RecognitionAlternative]
    is_partial: bool
    cnet: RecognitionConfusionNetwork
    audio_channel: int
    def __init__(self, alternatives: _Optional[_Iterable[_Union[RecognitionAlternative, _Mapping]]] = ..., is_partial: bool = ..., cnet: _Optional[_Union[RecognitionConfusionNetwork, _Mapping]] = ..., audio_channel: _Optional[int] = ...) -> None: ...

class RecognitionError(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class RecognitionAlternative(_message.Message):
    __slots__ = ("transcript_formatted", "transcript_raw", "start_time_ms", "duration_ms", "confidence", "word_details")
    TRANSCRIPT_FORMATTED_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_RAW_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    WORD_DETAILS_FIELD_NUMBER: _ClassVar[int]
    transcript_formatted: str
    transcript_raw: str
    start_time_ms: int
    duration_ms: int
    confidence: float
    word_details: WordDetails
    def __init__(self, transcript_formatted: _Optional[str] = ..., transcript_raw: _Optional[str] = ..., start_time_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., confidence: _Optional[float] = ..., word_details: _Optional[_Union[WordDetails, _Mapping]] = ...) -> None: ...

class WordDetails(_message.Message):
    __slots__ = ("formatted", "raw")
    FORMATTED_FIELD_NUMBER: _ClassVar[int]
    RAW_FIELD_NUMBER: _ClassVar[int]
    formatted: _containers.RepeatedCompositeFieldContainer[WordInfo]
    raw: _containers.RepeatedCompositeFieldContainer[WordInfo]
    def __init__(self, formatted: _Optional[_Iterable[_Union[WordInfo, _Mapping]]] = ..., raw: _Optional[_Iterable[_Union[WordInfo, _Mapping]]] = ...) -> None: ...

class WordInfo(_message.Message):
    __slots__ = ("word", "confidence", "start_time_ms", "duration_ms")
    WORD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    word: str
    confidence: float
    start_time_ms: int
    duration_ms: int
    def __init__(self, word: _Optional[str] = ..., confidence: _Optional[float] = ..., start_time_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class RecognitionConfusionNetwork(_message.Message):
    __slots__ = ("links",)
    LINKS_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[ConfusionNetworkLink]
    def __init__(self, links: _Optional[_Iterable[_Union[ConfusionNetworkLink, _Mapping]]] = ...) -> None: ...

class ConfusionNetworkLink(_message.Message):
    __slots__ = ("start_time_ms", "duration_ms", "arcs")
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ARCS_FIELD_NUMBER: _ClassVar[int]
    start_time_ms: int
    duration_ms: int
    arcs: _containers.RepeatedCompositeFieldContainer[ConfusionNetworkArc]
    def __init__(self, start_time_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., arcs: _Optional[_Iterable[_Union[ConfusionNetworkArc, _Mapping]]] = ...) -> None: ...

class ConfusionNetworkArc(_message.Message):
    __slots__ = ("word", "confidence", "features")
    WORD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    word: str
    confidence: float
    features: ConfusionNetworkArcFeatures
    def __init__(self, word: _Optional[str] = ..., confidence: _Optional[float] = ..., features: _Optional[_Union[ConfusionNetworkArcFeatures, _Mapping]] = ...) -> None: ...

class ConfusionNetworkArcFeatures(_message.Message):
    __slots__ = ("confidence",)
    class ConfidenceEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    confidence: _containers.ScalarMap[str, float]
    def __init__(self, confidence: _Optional[_Mapping[str, float]] = ...) -> None: ...
