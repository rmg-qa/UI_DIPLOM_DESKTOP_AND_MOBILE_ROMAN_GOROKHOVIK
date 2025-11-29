import json


def logger_network(logs):
    network_requests = []
    for log_entry in logs:
        # Каждый log_entry - это словарь с ключами: 'level', 'message', 'timestamp', 'source'
        log_message = log_entry['message']
        parsed_message = json.loads(log_message)  # Парсим JSON

        message_data = parsed_message.get('message', {})
        method = message_data.get('method')

        if method == 'Network.requestWillBeSent':
            request_info = {
                'url': message_data.get('params', {}).get('request', {}).get('url'),
                'method': message_data.get('params', {}).get('request', {}).get('method'),
                'headers': message_data.get('params', {}).get('request', {}).get('headers', {}),
                'timestamp': log_entry.get('timestamp')
            }
            network_requests.append(request_info)
    return network_requests
