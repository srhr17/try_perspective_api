import json 
import requests 
api_key = '###'
url = ('https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key=' + api_key)
data_dict = {
    'comment': {'text': 'what kind of idiot name is foo?'},
    'languages': ['en'],
    'requestedAttributes': {'TOXICITY': {},'IDENTITY_ATTACK':{},'INSULT':{},'PROFANITY':{},'THREAT':{},'SEXUALLY_EXPLICIT':{},'FLIRTATION':{},'INCOHERENT':{}}
}
data_dict['comment']['text']=input('Enter the sentence : ')
response = requests.post(url=url, data=json.dumps(data_dict)) 
response_dict = json.loads(response.content) 
# res=json.dumps(response_dict, indent=2)

toxicity_val=round(response_dict['attributeScores']['TOXICITY']['spanScores'][0]['score']['value'],2)
identity_attack_val=round(response_dict['attributeScores']['IDENTITY_ATTACK']['spanScores'][0]['score']['value']*100,2)
insult_val=round(response_dict['attributeScores']['INSULT']['spanScores'][0]['score']['value']*100,2)
profanity_val=round(response_dict['attributeScores']['PROFANITY']['spanScores'][0]['score']['value']*100,2)
threat_val=round(response_dict['attributeScores']['THREAT']['spanScores'][0]['score']['value']*100,2)
sexually_explicit_val=round(response_dict['attributeScores']['SEXUALLY_EXPLICIT']['spanScores'][0]['score']['value']*100,2)
filtration_val=round(response_dict['attributeScores']['FLIRTATION']['spanScores'][0]['score']['value']*100,2)
incoherent_val=round(response_dict['attributeScores']['INCOHERENT']['spanScores'][0]['score']['value']*100,2)
print('Your sentence is '+str(toxicity_val)+chr(37)+' toxic, '+str(identity_attack_val)+chr(37)+' attacking identity, '+str(insult_val)+chr(37)+' insulting, '+str(threat_val)+chr(37)+' contains threat, '+str(sexually_explicit_val)+chr(37)+' has lewd content, ' +str(incoherent_val)+chr(37)+' complex. ')
print('Your sentence has '+str(filtration_val)+chr(37)+' pick up lines.')

