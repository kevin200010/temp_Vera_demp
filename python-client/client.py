#!/usr/bin/env python3

# Copyright (2024 -- present) Cobalt Speech and Language Inc.
import requests
import grpc

import cobaltspeech.sentimo.v1.sentimo_pb2_grpc as stub
import cobaltspeech.sentimo.v1.sentimo_pb2 as sentimo

import cobaltspeech.transcribe.v5.transcribe_pb2 as transcribe

import json
from google.protobuf.json_format import MessageToDict

# VERN Endpoints

vern_server = "https://vernapi.com/analyze"
API_key = "RfMW5CJYxstUVc6pV8XRNq2kBp2lKyya:NNJyA3itTdrzor0OwO3xBoUEdR25PC9vTLJrgJh8KvYB3ccPXZD33hKoEBBbYWBx"

# Define the headers for VERN API
VERN_headers = {
    'Authorization': API_key,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}



###  Cobalt Code 
# Cobalt Endpoint/server
serverAddress = "localhost:2727"

# Using a channel without TLS enabled.
channel = grpc.insecure_channel(serverAddress)
client = stub.SentimoServiceStub(channel)

# Get server version.
versionResp = client.Version(sentimo.VersionRequest())
# print(versionResp)

# Get list of sentimo models on the server.
modelResp = client.ListModels(sentimo.ListModelsRequest())
# for model in modelResp.models:
#     print(model)

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
# Generate analysis table from JSON response
def generate_analysis_table(analysis):
    scores = analysis.get('scores', [])
    table = "<table><tr><th>Emotion</th><th>Value</th></tr>"
    for score in scores:
        table += f"<tr><td>{score['name']}</td><td>{score['value']}</td></tr>"
    table += "</table>"
    return table

def generate_cobalt_table(response):
    # Convert the JSON response to a dictionary if it's in string format
    if isinstance(response, str):
        response = json.loads(response)
    
    predictions = response.get('predictions', [])
    duration = response.get('duration_ms', 'N/A')

    # Start building the HTML table
    table = """
        <h3>Cobalt Response</h3>
        <table>
            <tr>
                <th>Label</th>
                <th>Probability</th>
            </tr>
    """
    
    # Add rows for each prediction
    for prediction in predictions:
        table += f"""
        <tr>
            <td>{prediction['label']}</td>
            <td>{prediction['probability']}</td>
        </tr>
        """
    
    # Close the table and add duration info
    table += """
        </table> 
    """
    
    return table
def processResponse(resp):
   res =MessageToDict(resp, preserving_proto_field_name=True)
   #print("Cobalt Analysis :")
   cobalt_results = res['sentimo']
   print(res)
   #print("__________________________________")
   html_output = """"""
   html_output += generate_cobalt_table(cobalt_results)
   html_output +=  """<hr style="width:100%;text-align:left;margin-left:0">"""
   for k in res["transcribe"]['result'].keys():
       for i in res["transcribe"]['result']["alternatives"]:
           #print(i)
           text = i['transcript_raw']
           # Define the body with the text to analyze
           data = {'text':text}

           # Make the POST request
           VERN_response= requests.post(vern_server, headers=VERN_headers, json=data)
            
           # Check if the request was successful
           if VERN_response.status_code == 200:
                # Parse the JSON response
                analysis = VERN_response.json()
                # print('VERN Response : ', analysis)
                html_output += """<h3>VERN Response</h3>"""
                analysis_table = generate_analysis_table(analysis)
                html_output += """
                <tr>
                    <td>Translations : {}</td>
                    <td>{}</td>
                </tr>
                """.format(text, analysis_table)
                # print(html_output)
           else:
                print('Failed to get response. Status code:', VERN_response.status_code)
                print('Response:', VERN_response)
   html_output +=  """<hr style="width:100%;text-align:left;margin-left:0">
                      <hr style="width:100%;text-align:left;margin-left:0">
                   """
   return html_output
#    print("__________________________________")
#    print("__________________________________")
#    print(f"{json.dumps(MessageToDict(resp, preserving_proto_field_name=True))}")
# def processResponse(resp):
#     res = MessageToDict(resp, preserving_proto_field_name=True)
    
#     # Start building the HTML table
#     html_output = """
#         <h2>Cobalt Analysis</h2>
#         <table>
#             <tr>
#                 <th>Sentimo</th>
#             </tr>
#             <tr>
#                 <td>{}</td>
#             </tr>
#         </table>
#         <h2>Transcriptions and VERN Responses</h2>
#         <table>
#             <tr>
#                 <th>Transcription</th>
#                 <th>VERN Analysis</th>
#             </tr>
#     """.format(res['sentimo'])

#     # Iterate over transcriptions and VERN responses
#     for k in res["transcribe"]['result'].keys():
#         for i in res["transcribe"]['result']["alternatives"]:
#             text = i['transcript_raw']
#             data = {'text': text}
#             VERN_response = requests.post(vern_server, headers=VERN_headers, json=data)
#             if VERN_response.status_code == 200:
#                 analysis = VERN_response.json()
#                 analysis_json = json.dumps(analysis, indent=2)
#                 html_output += """
#                 <tr>
#                     <td>{}</td>
#                     <td><pre>{}</pre></td>
#                 </tr>
#                 """.format(text, analysis_json)
#             else:
#                 error_message = f"Failed to get response. Status code: {VERN_response.status_code}. Response: {VERN_response.text}"
#                 html_output += """
#                 <tr>
#                     <td>{}</td>
#                     <td>{}</td>
#                 </tr>
#                 """.format(text, error_message)

#     # Close the HTML table and body
#     html_output += """
#         </table>
#     """

    # # Print the HTML output
    # print(html_output)

    # # Return the HTML output
    # return html_output

stream(cfg, audio)
# print(client.StreamingRecognize(stream(cfg, audio)))
# Streaming requests to the server.
result = """"""
for resp in client.StreamingRecognize(stream(cfg, audio)):
    result += processResponse(resp)

print(result)
# return result 