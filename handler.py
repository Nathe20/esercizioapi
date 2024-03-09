import json
import boto3

dynamodb = boto3.resource("dynamodb")
table_name = "user"  # Nome della tabella DynamoDB


#logica creazione user

def create_user(event, context):
    data = json.loads(event["body"])
    user_id = data.get("user_id")
    name = data.get("name")

    if user_id and name:
        table = dynamodb.Table(table_name)
        table.put_item(Item={"user_id": user_id, "name": name})
        return {
            "statusCode": 201,
            "body": json.dumps({"message": f"Utente {user_id} creato con successo!"})
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Dati utente mancanti"})
        }
    

#logica get user
    
def get_user_by_id(event, context):
    user_id = event["pathParameters"]["user_id"]
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={"user_id": user_id})

    if "Item" in response:
        user = response["Item"]
        return {
            "statusCode": 200,
            "body": json.dumps(user)
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Utente non trovato"})
        }

