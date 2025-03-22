def lambda_handler(event, context):
    sm = boto3.client("sagemaker-runtime")
    
    # Get raw CSV data from request body
    data = event["body"]  # Directly use the CSV string
    
    # Call SageMaker endpoint
    response = sm.invoke_endpoint(
        EndpointName="wine-quality-prediction-2025-03-22-00-47-34",
        ContentType="text/csv",
        Body=data
    )
    
    # Return prediction
    prediction = response["Body"].read().decode("utf-8")
    return {
        "statusCode": 200,
        "body": json.dumps({"quality": float(prediction)})
    }