FROM public.ecr.aws/lambda/python:3.10

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir -r requirements.txt

# Set the CMD to your handler
CMD ["app.lambda_handler"]
