import requests
import json

headers = {"content-type": "application/json"}
url = 'http://localhost:8501/v1/models/saved_model:predict'

def get_values(request):
    param_dict = dict()
    string_params=["region","tenure","top_pack","mrg"]
    form_meta_values =['csrf_token', 'user_id', 'user_predict', 'user_add','add_prediction']

    for key,value in request.form.items():
        if key not in form_meta_values:
            # for blank number values
            if key not in string_params:
                try:
                    value = float(value)
                except ValueError:
                    value = 0
            # For blank string values        
            else:
                if not value:
                    value="not_given"
            
            param_dict[key]=value
    
    return param_dict



def get_prediction(request):
    param_values = get_values(request)
    data = {'instances':[param_values]}
    data = json.dumps(data)
    
    json_response = requests.post(url, data=data, headers=headers).json()
    print(json_response)
    json_response = json_response['predictions']
    prediction = round(json_response[0][0],3)
    
    return prediction