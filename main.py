import ollama

response = ollama.chat(model='llama2', messages=[{'role': 'user', 'content': 'Hello!'}])

print(response['message']['content'])

# {'model': 'llama2', 
#  'created_at': '2024-01-18T08:31:19.135713Z', 
#  'message': {'role': 'assistant', 'content': 'Hello there! How are you doing today?'}, 
#  'done': True, 
#  'total_duration': 1887857920, 
#  'load_duration': 2931998, 
#  'prompt_eval_duration': 386794000, 
#  'eval_count': 9, ]
#  'eval_duration': 1496661000}
