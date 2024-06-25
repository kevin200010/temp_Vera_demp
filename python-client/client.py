#!/usr/bin/env python3

# Copyright (2024 -- present) Cobalt Speech and Language Inc.

import grpc

import cobaltspeech.sentimo.v1.sentimo_pb2_grpc as stub
import cobaltspeech.sentimo.v1.sentimo_pb2 as sentimo

import cobaltspeech.transcribe.v5.transcribe_pb2 as transcribe

import json
from google.protobuf.json_format import MessageToDict

serverAddress = "localhost:2727"

# Using a channel without TLS enabled.
channel = grpc.insecure_channel(serverAddress)
client = stub.SentimoServiceStub(channel)

# Get server version.
versionResp = client.Version(sentimo.VersionRequest())
print(versionResp)

# Get list of sentimo models on the server.
modelResp = client.ListModels(sentimo.ListModelsRequest())
for model in modelResp.models:
    print(model)

# Select a model from the list above. Going with the first model
# in this example.
model = modelResp.models[0]

# Set the config. We don't set the audio format and let the server auto-detect
# the format from the file header.
cfg = sentimo.Config(
    model_id=model.id,
    recognition_config=transcribe.RecognitionConfig(
        model_id=model.attributes.available_transcribe_model_ids[0],
        audio_format_headered="AUDIO_FORMAT_HEADERED_UNSPECIFIED",
    ),
)

# Open audio file.
audio = open("C:\\Users\\kevin\\OneDrive\\Documents\\VERN.ai\\Cobalt\\End Point for VERA\\new deliverable\\deliverable-20240604\\web app\\public\\uploads\\converted_audio.wav", "rb")

# The first request to the server should only contain the recognition
# configuration. Subsequent requests should contain audio bytes. We can write a
# simple generator to do this.
def stream(cfg, audio, bufferSize=1024):
    yield sentimo.StreamingRecognizeRequest(config=cfg)
    
    data = audio.read(bufferSize)
    while len(data) > 0:
        yield sentimo.StreamingRecognizeRequest(
          audio=transcribe.RecognitionAudio(data=data),
        )
        data = audio.read(bufferSize)

# We also define a callback function to execute for each response. The example
# below just prints to stdout as json string.
def processResponse(resp):
   print(f"{json.dumps(MessageToDict(resp, preserving_proto_field_name=True))}")

stream(cfg, audio)
# print(client.StreamingRecognize(stream(cfg, audio)))
# Streaming requests to the server.
for resp in client.StreamingRecognize(stream(cfg, audio)):
    print(resp)
    processResponse(resp)

