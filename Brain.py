import os 
import openai
import config

openai.api_key = "your api key"


def greet():
    
     prompt = f'''Act as a personel travel guide your name is 'Trivallo'.
                  you have to greet the user professionally your tone must be respectful.
                  ask them where they are planning to travel ask them to fill the cities of departure and arrival of the journey '''
     pro = {"role":"system","content":prompt}
     response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [pro],
                temperature=0.5,
                max_tokens=100,
                frequency_penalty=0.0,
                presence_penalty=0.0
                
     )
     
     Respo = response['choices'][0]['message']['content']
     
     return Respo
 
 
 
def routes(From,To):
     prompt = f'''Act as a personel travel guide your name is 'Trivallo' and you have travelled the whole world.
                  give the detailed information about the existing modes of transportation from {From} to {To}.
                  your information must include the distance between {From} and {To}.
                  your information must also include that what will the user experience if he/she travel from a specific mode of transport.
                  in the end also suggest the best time to travel {To}.
                  ask user to fill the number of days they want a travel plan for, in the below space '''
     
     pro = {"role":"system","content":prompt}
     response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [pro],
                temperature=0.5,
                max_tokens=500,
                frequency_penalty=0.0,
                presence_penalty=0.0
                
     )
     
     print(response)
     
     Respo = response['choices'][0]['message']['content']
     
     return Respo




def plan(From,To,days):
     prompt = f'''Plan a journey for me from {From} to {To}.
               i just have {days} to travel and have fun.
               make me a iternary so that i can explore maximum as possible of {To}.
               u must include the names of the  best places to visit in {To}.
               suggest the names of popular places to eat in {To} in the iternary provided by you'''
     
     pro = {"role":"system","content":prompt}
     response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [pro],
                temperature=0.5,
                max_tokens=500,
                frequency_penalty=0.0,
                presence_penalty=0.0
                
     )
     
     print(response)
     
     Respo = response['choices'][0]['message']['content']
     
     return Respo






